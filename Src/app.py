import streamlit as st
from bedrock_client import invoke_model
from prompts import summarize_prompt, classify_prompt, extract_prompt

st.set_page_config(page_title="AWS Bedrock Prompt Lab", layout="centered")

st.title("AWS Bedrock Prompt Engineering Lab")
st.write("A simple AI web app for summarization, sentiment classification, and JSON extraction.")

tab1, tab2, tab3 = st.tabs(["Summarize", "Classify Sentiment", "Extract JSON"])

with tab1:
    st.header("Text Summarization")
    summary_input = st.text_area("Enter text to summarize", height=200, key="summary_input")

    if st.button("Summarize"):
        if summary_input.strip():
            try:
                prompt = summarize_prompt(summary_input)
                result = invoke_model(prompt)
                st.subheader("Summary")
                st.write(result)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter text first.")

with tab2:
    st.header("Sentiment Classification")
    classify_input = st.text_area("Enter text to classify", height=200, key="classify_input")

    if st.button("Classify"):
        if classify_input.strip():
            try:
                prompt = classify_prompt(classify_input)
                result = invoke_model(prompt)
                st.subheader("Sentiment")
                st.write(result)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter text first.")

with tab3:
    st.header("JSON Extraction")
    extract_input = st.text_area("Enter text to extract structured data from", height=200, key="extract_input")

    if st.button("Extract"):
        if extract_input.strip():
            try:
                prompt = extract_prompt(extract_input)
                result = invoke_model(prompt)
                st.subheader("Extracted JSON")
                st.code(result, language="json")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter text first.")

