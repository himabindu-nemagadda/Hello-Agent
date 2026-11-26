import pandas as pd
import streamlit as st

from agent import ask_question, build_agent

st.title("Hello Agent")
st.write(
    "Upload CSV files and ask questions about their contents. "
    "The agent answers using the uploaded data."
)

uploaded_files = st.file_uploader(
    "Upload one or more CSV files",
    type="csv",
    accept_multiple_files=True,
)

dataframes = {}

for uploaded_file in uploaded_files:
    try:
        dataframe = pd.read_csv(uploaded_file)
        dataframes[uploaded_file.name] = dataframe

        with st.expander(f"Preview: {uploaded_file.name}"):
            st.dataframe(dataframe.head())
    except (
        pd.errors.EmptyDataError,
        pd.errors.ParserError,
        UnicodeDecodeError,
    ) as error:
        st.error(f"Could not read {uploaded_file.name} as a CSV: {error}")

question = st.text_input("What would you like to know?")

if st.button("Ask Agent"):
    if not uploaded_files:
        st.error("Upload at least one CSV file before asking a question.")
    elif not dataframes:
        st.error("No valid CSV files are available to answer your question.")
    elif not question.strip():
        st.error("Enter a question before asking the agent.")
    else:
        try:
            with st.spinner("The agent is thinking..."):
                agent = build_agent(dataframes)
                answer = ask_question(agent, question.strip())

            st.subheader("Answer")
            st.write(answer)
        except ValueError as error:
            st.error(str(error))