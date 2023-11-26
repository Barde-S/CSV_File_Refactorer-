# Column Names Cleaner

This Streamlit application is designed to clean and organize column names in a CSV file. The tool provides functionalities to:

1. **Clean Column Names:**
   - Reads a CSV file with specified encoding.
   - Removes duplicated columns and drops unwanted columns.
   - Standardizes and cleans column names by removing trailing spaces, replacing spaces with underscores, and converting to lowercase.
   - Maps specific column name replacements for better clarity.

2. **Rearrange and Insert Columns:**
   - Rearranges the DataFrame columns to a desired order.
   - Inserts missing columns with empty values if they don't exist.

3. **Split and Save CSV:**
   - Splits the DataFrame into chunks of 1000 rows.
   - Saves each chunk as a separate CSV file.

## Usage

1. **Upload CSV File:**
   - Use the file uploader to upload a CSV file.

2. **Clean Column Names:**
   - Click the "Clean Column Names" button to initiate the cleaning process.
   - Duplicated and unwanted columns are removed, and the remaining columns are standardized.

3. **Rearrange and Insert Columns:**
   - The cleaned DataFrame is then rearranged and missing columns are inserted.

4. **Split and Save CSV:**
   - The rearranged DataFrame is split into chunks of 1000 rows.
   - Each chunk is available for download as a separate CSV file.

## Additional Information

- The source column is added to the DataFrame with a link to the source data.
- Specific columns are mapped for renaming, such as converting 'url' and 'webaddress' to 'website'.
- Unwanted columns, such as 'address2' and 'contactname', are dropped from the DataFrame.
- The cleaned and rearranged DataFrame is displayed in the Streamlit app for user verification.

Note: This program is for a specific purpose; if you want to use it, you might have to refactor it to meet your preference.

**Note:** Make sure to have Streamlit (`pip install streamlit`) and pandas (`pip install pandas`) installed before running the application.
