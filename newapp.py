# pip install streamlit

import streamlit as st
import pandas as pd
import base64

# Define the clean_column_names function
def clean_column_names(input_file, encoding='utf-8'):
    # Read the CSV file into a DataFrame with the specified encoding
    df = pd.read_csv(input_file, encoding=encoding)

# Check for duplicated columns and drop the  unwanted columns 
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
        # Clean column names and get the cleaned DataFrame
        cleaned_df = clean_column_names(uploaded_file, encoding='ISO-8859-1')

        # Display cleaned DataFrame
        st.write("Cleaned DataFrame:")
        st.write(cleaned_df)

        # Create a download link for the cleaned CSV file
        cleaned_csv = cleaned_df.to_csv(index=False).encode('utf-8')
        b64 = base64.b64encode(cleaned_csv).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="cleaned_data.csv">Download cleaned CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)
