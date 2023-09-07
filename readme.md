# Amazon Sponsored Products Search Term Report Processor

This Python script is designed to process your Amazon Sponsored Products Search Term report, generating separate reports for Auto Campaigns, Broad Match, Exact Match, Phrase Match, and ASIN-targeted campaigns. These categorized reports aim to facilitate in-depth keyword analysis and optimization.

## Usage

1. **Prerequisites:**
   - Make sure you have Python installed on your system. If not, download and install it from [here](https://www.python.org/downloads/).
   - Install requirements.txt file with  
   ```
   pip install -r requirements.txt
   ```

2. **Set Up:**
   - Place your Amazon Sponsored Products Search Term report (CSV format) in the `input` directory.

3. **Run the Script:**
   - Open a terminal/command prompt and navigate to the project directory.
   - Run the script using the following command:
     ```
     python Amazon_FBA_Report_Analyzer.py
     ```

4. **Generated Reports:**
   - The categorized reports will be saved in the `output` directory.  
   - Output: Asin, AutoCampaign, BROAD, EXACT, PHRASE

## Directory Structure

- `input`: Place your Amazon Sponsored Products Search Term report in root directory.
- `output`: The categorized reports will be saved in root directory.

## Report Categories

- **Auto Campaigns**: This report contains search terms from auto-targeted campaigns.
- **Broad Match**: Includes search terms from broad match campaigns.
- **Exact Match**: Contains search terms from exact match campaigns.
- **Phrase Match**: Consists of search terms from phrase match campaigns.
- **ASIN-targeted Campaigns**: This report includes search terms from campaigns targeting specific ASINs.

## Disclaimer

This script is provided as-is without any warranties. Use it at your own risk. Always make sure to backup your original data before running any scripts.


## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per your requirements.


