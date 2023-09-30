import streamlit as st
import pandas as pd
import base64

# Define the clean_column_names function
def clean_column_names(df):
    # Remove duplicated columns
    df = df.loc[:, ~df.columns.duplicated()]

    # Clean and standardize the column names
    df.columns = df.columns.str.strip().str.replace(' ', '').str.lower()

    # Items to drop
    items_to_drop = [
        'address2', 'address3', 'companyname', 'contactname', 'title', 'middlename',
        'executivename', 'jobtitle', 'siccode', 'industry', 'technology', 'employeesize',
        'revenue($m)', 'sic', 'industrytype', 'verificationresults', 'contactfirst',
        'annualsales', 'employeecount', 'directphone', 'lawfirm'
    ]

    # Drop specified columns
    df.drop(columns=items_to_drop, errors='ignore', inplace=True)

    # Rename columns
    cols = {'practicearea': 'practice_name', 'phonenumber': 'phone', 'address1': 'address'}
    df.rename(columns=cols)

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
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')

        # Clean column names and get the cleaned DataFrame
        cleaned_df = clean_column_names(df)

        # Define the desired order
        desired_order = [
            'firstname', 'lastname', 'email', 'phone', 'practice_name', 'specialty',
            'tagline', 'about', 'website', 'address', 'city', 'state', 'country', 'zipcode',
            'facebook', 'instagram', 'linkedin', 'google', 'source'
        ]

        # Rearrange columns based on the desired order
        cleaned_df = cleaned_df[desired_order]

        # Display cleaned DataFrame
        st.write("Cleaned DataFrame:")
        st.write(cleaned_df)

        # Create a download link for the cleaned CSV file
        cleaned_csv = cleaned_df.to_csv(index=False).encode('utf-8')
        b64 = base64.b64encode(cleaned_csv).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="cleaned_data.csv">Download cleaned CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)
