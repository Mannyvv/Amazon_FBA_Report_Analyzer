
import pandas as pds

from openpyxl import Workbook, load_workbook


def data_load():
    ##load the excel file data into a dataframe
    file = 'G:\My Drive\Amazon Trappin\Spoon_Lid_Holder\PPC-Keywords\Python_Script\Sponsored Products Search term report.xlsx'
    amazon_fba_sponsored_datasheet = pds.read_excel(file)

    ##CLEAN UP DATA

    #remove spaces, lower case all letters from column names
    amazon_fba_sponsored_datasheet.columns = amazon_fba_sponsored_datasheet.columns.str.lower().str.strip().str.replace(" ", "_")
    amazon_fba_sponsored_datasheet.columns = amazon_fba_sponsored_datasheet.columns.str.strip(")")
    amazon_fba_sponsored_datasheet.columns = amazon_fba_sponsored_datasheet.columns.str.replace("(", "")
    amazon_fba_sponsored_datasheet.rename({"total_advertising_cost_of_sales_acos": "Acos"}, axis = 1, inplace = True)
    ##amazon_fba_sponsored_datasheet.rename(columns={"total_advertising_cost_of_sales_acos" : 'Acos'})
   
    return amazon_fba_sponsored_datasheet

 