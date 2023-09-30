import streamlit as st
import pandas as pd
import base64

# Define the clean_column_names function
def clean_column_names(input_file, encoding='utf-8'):
    # Read the CSV file into a DataFrame with the specified encoding
    df = pd.read_csv(input_file, encoding=encoding)

    # Check for duplicated columns and drop the unwanted columns
    duplicates = set()
    columns_to_drop = []

    for column in df.columns:
        if column in duplicates:
            columns_to_drop.append(column)
        else:
            duplicates.add(column)

    # Drop the extra columns
    df = df.drop(columns=columns_to_drop)

    # Clean and standardize the column names
    df.columns = df.columns.str.strip()  # Remove trailing spaces
    df.columns = df.columns.str.replace(' ', '')  # Replace spaces with underscores
    df.columns = df.columns.str.lower()

    Items_to_drop = [
        'address2', 'address3', 'companyname', 'contactname', 'title', 'middlename',
        'executivename', 'jobtitle', 'siccode', 'industry', 'technology', 'employeesize',
        'revenue($m)', 'sic', 'industrytype', 'verificationresults', 'contactfirst',
        'annualsales', 'employeecount', 'directphone', 'contactfirst', 'contactlast',
        'lawfirm'
    ]

    # Loop through the DataFrame columns and drop columns if they are in Items_to_drop
    for column in Items_to_drop:
        if column in df.columns:
            df.drop(column, axis=1, inplace=True)

    df["source"] = "https://drive.google.com/drive/folders/1YIIn2o5s3933XyqMirCmiHSxoePYb_nq?usp=share_link"
    cols = {'url':'website',
             'webaddress':'website',
             'practicearea': 'practice_name', 
             'phonenumber':'phone',
             'address1':'address'}
    df = df.rename(columns=cols)

    return df

# Define the rearrange_and_insert_columns function
def rearrange_and_insert_columns(df):
    desired_order = [
        'firstname', 'lastname', 'email', 'phone', 'practice_name', 'specialty',
        'tagline', 'about', 'website', 'address', 'city', 'state', 'country', 'zipcode',
        'facebook', 'instagram', 'linkedin', 'google', 'source'
    ]

    # Create a new DataFrame with columns in the desired order
    reordered_df = pd.DataFrame(columns=desired_order)

    # Iterate through the columns in the desired order
    for column in desired_order:
        if column in df.columns:
            # If the column exists in the original DataFrame, copy it to the new DataFrame
            reordered_df[column] = df[column]
        else:
            # If the column is missing, insert it with empty values
            reordered_df[column] = ''

    return reordered_df

# Streamlit UI
st.title("Column Names Cleaner")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Display uploaded file
    st.write("Uploaded CSV file:")
    st.write(uploaded_file)

    # Check if a button is clicked to clean the column names
    if st.button("Clean Column Names"):
        # Clean column names and get the cleaned DataFrame
        cleaned_df = clean_column_names(uploaded_file, encoding='ISO-8859-1')

        # Rearrange and insert missing columns
        rearranged_df = rearrange_and_insert_columns(cleaned_df)

        # Display cleaned and rearranged DataFrame
        st.write("Cleaned and Rearranged DataFrame:")
        st.write(rearranged_df)

        # Create a download link for the cleaned CSV file
        cleaned_csv = rearranged_df.to_csv(index=False).encode('utf-8')
        b64 = base64.b64encode(cleaned_csv).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download=f"file_name_{file_number}.csv">Download cleaned CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)
