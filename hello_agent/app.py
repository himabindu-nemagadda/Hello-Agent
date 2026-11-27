import pandas as pd
import streamlit as st

from agent import ask_question, build_agent

st.title("Hello Agent")
st.write(
    "Upload CSV files and ask questions about their contents. "
    "Hello Agent will use the uploaded data to answer."
)

uploaded_files = st.file_uploader(
    "Choose CSV files",
    type="csv",
    accept_multiple_files=True,
)

dataframes = {}

for uploaded_file in uploaded_files or []:
    try:
        dataframe = pd.read_csv(uploaded_file)
        dataframes[uploaded_file.name] = dataframe

        st.subheader(uploaded_file.name)
        st.dataframe(dataframe.head())
    except (
        pd.errors.EmptyDataError,
        pd.errors.ParserError,
        UnicodeDecodeError,
    ) as error:
        st.error(f"Could not read {uploaded_file.name}: {error}")

question = st.text_input("What would you like to ask?")

if st.button("Ask Agent"):
    if not uploaded_files:
        st.error("Please upload at least one CSV file.")
    elif not dataframes:
        st.error("No valid CSV files are available. Please upload a readable CSV.")
    elif not question.strip():
        st.error("Please enter a question.")
    else:
        try:
            with st.spinner("The agent is working on your question..."):
                agent = build_agent(dataframes)
                answer = ask_question(agent, question.strip())

            st.subheader("Answer")
            st.write(answer)
        except ValueError as error:
            st.error(str(error))