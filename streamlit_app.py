import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart Test Automation App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'Give me a use case and ask for test cases')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

st.markdown("[Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)")

st.sidebar.file_uploader("Upload Test Scripts", type=[".py"])


tab1, tab2 = st.tabs(["Test Results", "Logs"])

# Tab 1 - Test Results
with tab1:
  st.header("Real-time test results")
  # Add your results here
  st.write("Add your results here or files")

with tab2:
  st.header("Test Logs")
  st.write("Add something here... files or logs or whatever")


import streamlit as st
import pandas as pd
import io

# Function to modify the dataframe
def modify_dataframe(df):
    # Example operation: Adding a new column
    df['New Column'] = 'Example Data'
    return df

# File uploader widget
uploaded_file = st.file_uploader("Upload a CSV", type="csv")
if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    # Perform operations on the data
    modified_data = modify_dataframe(data)

    # Show the modified data
    st.write("Modified DataFrame:")
    st.dataframe(modified_data)

    # Convert DataFrame to CSV and offer it for download
    towrite = io.BytesIO()
    modified_data.to_csv(towrite, encoding='utf-8', index=False)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="modified_file.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)

