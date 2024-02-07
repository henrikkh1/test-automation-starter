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

[Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

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
