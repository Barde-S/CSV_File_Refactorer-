import streamlit as st
import pandas as pd
import base64

# Define the clean_column_names function
def clean_column_names(input_file, encoding='utf-8', desired_order=None):
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

    cols = {'practicearea': 'practice_name', 
             'phonenumber':'phone',
             'address1':'address'}
    df = df.rename(columns=cols)
# Columns to be rearranged
    desired_order = [
    'firstname', 'lastname', 'email', 'phone', 'practice_name', 'specialty',
    'tagline', 'about', 'website', 'address', 'city', 'state', 'country', 'zipcode',
    'facebook', 'instagram', 'linkedin', 'google', 'source'
]

    # Rearrange columns based on the desired order
    if desired_order:
        existing_columns = list(df.columns)
        for col in desired_order:
            if col not in existing_columns:
                df[col] = None  # Add missing columns with None values
        df = df[desired_order]

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
        cleaned_df = clean_column_names(uploaded_file, encoding='ISO-8859-1', desired_order=desired_order)

        # Display cleaned DataFrame
        st.write("Cleaned DataFrame:")
        st.write(cleaned_df)

        # Create a download link for the cleaned CSV file
        cleaned_csv = cleaned_df.to_csv(index=False).encode('utf-8')
        b64 = base64.b64encode(cleaned_csv).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="cleaned_data.csv">Download cleaned CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)
