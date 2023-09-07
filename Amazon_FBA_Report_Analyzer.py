from datetime import date, datetime
from math import frexp
from tkinter.tix import COLUMN
import time
from unicodedata import category
import os


from data_load import data_load
import pandas as pds


amazon_fba_sponsored_datasheet = data_load()


#Obtain unique names for various campaigns and products
all_portfolio_names = amazon_fba_sponsored_datasheet.portfolio_name.unique()
all_campaign_names = amazon_fba_sponsored_datasheet.campaign_name.unique()
all_match_types = amazon_fba_sponsored_datasheet.match_type.unique()

all_sheet_names = ["Over Acos", "Under Acos", "Ad Spend", "Clicks" ]
sub_category = [' - AutoCampaign_Keywords', ' - Asins', ' - BROAD' , ' - PHRASE', ' - EXACT']
query_for_match_type= ['~customer_search_term.str.startswith("b0")','customer_search_term.str.startswith("b0")', 'match_type == "BROAD"','match_type == "PHRASE"', 'match_type == "EXACT"' ]

##print(amazon_fba_sponsored_datasheet.columns)

def analyze_data(customer_search_term_datasheet):
    #Obtain dataframe with acos over profit margin
    all_dataframes = []
    acos_overprofitm_df = customer_search_term_datasheet[customer_search_term_datasheet.Acos > .38].sort_values('Acos', ascending=False).iloc[:,[2,4,8,15,9,10,11,12,13,14,18]]
    all_dataframes.append(acos_overprofitm_df)

    #Obtain dataframe with acos under profit margin
    acos_underprofitm_df = customer_search_term_datasheet[customer_search_term_datasheet.Acos < .38].sort_values('Acos', ascending=False).iloc[:,[2,4,8,15,9,10,11,12,13,14,18]]
    all_dataframes.append(acos_underprofitm_df)

    #Obtain dataframe with ad spend amounts(high to low)
    spend_amount_df = customer_search_term_datasheet[customer_search_term_datasheet.spend > 0].sort_values('spend', ascending=False).iloc[:,[2,4,8,15,9,10,11,12,13,14,18]]
    all_dataframes.append(spend_amount_df)

    #Obtain dataframe with keywords having 10 or more clicks (High to low). Might add 5 to 9 clicks with yellow for warning.
    clicks_above10_df = customer_search_term_datasheet[customer_search_term_datasheet.clicks > 9].sort_values('clicks', ascending=False).iloc[:,[2,4,8,15,9,10,11,12,13,14,18]]
    all_dataframes.append(clicks_above10_df)

    return all_dataframes

#Might move the excel sheet grooming into another page
def create_excel_files(all_dataframes,portfolio_name,category_type,folder_dir):

    #Create excel book based off portfolio name and category being requested i.e Exact, Broad, etc
    excel_file_name = folder_dir + "\\" + portfolio_name + category_type + '.xlsx'
    writer = pds.ExcelWriter(excel_file_name, engine='xlsxwriter') #add date range to name)

    #Change dataframe into excel sheet from book created above
    for count_df, dataframe in enumerate(all_dataframes):
        dataframe.to_excel(writer,sheet_name = all_sheet_names[count_df])

    #Formatting of each column for size, symbol, and visuals
    workbook = writer.book
    percent_format = workbook.add_format({'num_format':'0.00%'})
    percent_format_acos = workbook.add_format({'num_format':'0%'})
    decimal_format_impressions = workbook.add_format({'num_format' : '##,###'})
    dollar_format = workbook.add_format({'num_format' : '$0.00'}) #bg_color': 'green'
   
    #applying above formats to specific columns in the sheet
    for worksheet_name in all_sheet_names:
        worksheet = writer.sheets[worksheet_name]
        worksheet.set_column(0,11,20)
        worksheet.set_column(3,3,30)
        worksheet.set_column(7,7,None,percent_format)
        worksheet.set_column(4,4,None,percent_format_acos)
        worksheet.set_column(5,5,None,decimal_format_impressions)
        worksheet.set_column(8,10,None,dollar_format)

    writer.close()
    

#Creates an excel book for each portfolio with sheets for Autocampaign(Keyword and Asins), Broad, Phrase, and Exact

for pnames in all_portfolio_names:
    unique_portfolio_datasheet = amazon_fba_sponsored_datasheet[amazon_fba_sponsored_datasheet.portfolio_name == pnames  ]
    portfolio_name= pnames

    #create portfolio folder and obtain name
    current_directory = str(os.getcwd())
    now = datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    new_folder_name = portfolio_name +"_" + now
    os.mkdir(new_folder_name)
    new_folder_directory = current_directory + "\\" + new_folder_name

    #Start creating the excel files
    for mtype, scategory in enumerate(sub_category):
        category_type = sub_category[mtype]
        if scategory == ' - AutoCampaign_Keywords' or scategory == ' - Asins':
            auto_campaign_datasheet = unique_portfolio_datasheet[unique_portfolio_datasheet.targeting == "*"  ]
            customer_search_term_datasheet = auto_campaign_datasheet.query(query_for_match_type[mtype],engine = "python")
            all_df = analyze_data(customer_search_term_datasheet)
            create_excel_files(all_df, portfolio_name, category_type, new_folder_directory)
            
        else:
            customer_search_term_datasheet = unique_portfolio_datasheet.query(query_for_match_type[mtype],engine = "python")
            all_df = analyze_data(customer_search_term_datasheet)
            create_excel_files(all_df, portfolio_name, category_type, new_folder_directory)




