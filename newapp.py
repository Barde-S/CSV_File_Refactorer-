# pip install streamlit

import streamlit as st
import pandas as pd
import base64

# Define the clean_column_names function
def clean_column_names(df):
    # Clean and standardize the column names
    df.columns = df.columns.str.strip()  # Remove trailing spaces
    df.columns = df.columns.str.replace(' ', '')  # Replace spaces with underscores
    df.columns = df.columns.str.lower()

    # Replace column names based on specific criteria
    df.columns = df.columns.str.replace(r'(?!practice_name)practice', 'practice_name', regex=True)
    df.columns = df.columns.str.replace('URL|webaddress', 'website', regex=True)
    df.columns = df.columns.str.replace('address1', 'address')
    df.columns = df.columns.str.replace('phonenumber|contact', 'phone', regex=True)

    # Columns to drop
    columns_to_drop = [
        'address2', 'address3', 'companyname', 'contactname', 'title', 'middlename',
        'executivename', 'jobtitle', 'siccode', 'industry', 'technology', 'employeesize',
        'revenue($m)', 'sic', 'industrytype', 'verificationresults', 'contactfirst',
        'annualsales', 'employeecount', 'directphone', 'contactfirst', 'contactlast',
        'lawfirm'
    ]

    # Drop unwanted columns
    df = df.drop(columns=columns_to_drop, errors='ignore')

    # Check for the existence of both "address" and "address1" columns and drop "address1" if necessary
    if 'address' in df.columns and 'address1' in df.columns:
        df = df.drop(columns='address1')

    # Add the "source" column
    df["source"] = "https://drive.google.com/drive/folders/1YIIn2o5s3933XyqMirCmiHSxoePYb_nq?usp=share_link"

    return df

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
        # Clean column names using the provided function
        df = clean_column_names(df)

        # Display cleaned DataFrame
        st.write("Cleaned DataFrame:")
        st.write(df)

        # Create a download link for the cleaned CSV file
        cleaned_csv = df.to_csv(index=False).encode('utf-8')
        b64 = base64.b64encode(cleaned_csv).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="cleaned_data.csv">Download cleaned CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)
