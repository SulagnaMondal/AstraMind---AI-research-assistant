import streamlit as st
import requests

# Title
st.title("AstraMind Research Assistant")

# Sidebar for navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Choose a page", ["Home", "Summarize", "Code Extraction", "Search"])

# Backend API URL
API_URL = "http://localhost:8000"

# Home Page
if page == "Home":
    st.header("Welcome to AstraMind!")
    st.write("Upload a PDF, enter a URL, or paste text to get started.")

# Summarize Page
elif page == "Summarize":
    st.header("Summarize Content")
    input_text = st.text_area("Paste your text here:")
    if st.button("Summarize"):
        response = requests.post(f"{API_URL}/summarize", json={"text": input_text})
        if response.status_code == 200:
            st.write("**Summary:**")
            st.write(response.json()["summary"])
        else:
            st.error("Failed to generate summary. Please try again.")

# Code Extraction Page
elif page == "Code Extraction":
    st.header("Extract Code")
    input_text = st.text_area("Paste your text here:")
    if st.button("Extract Code"):
        response = requests.post(f"{API_URL}/extract-code", json={"text": input_text})
        if response.status_code == 200:
            st.write("**Extracted Code:**")
            st.code(response.json()["code"], language="python")
        else:
            st.error("Failed to extract code. Please try again.")

# Search Page
elif page == "Search":
    st.header("Search Documents")
    query = st.text_input("Enter your search query:")
    if st.button("Search"):
        response = requests.post(f"{API_URL}/search", json={"query": query})
        if response.status_code == 200:
            results = response.json()["results"]
            st.write("**Search Results:**")
            for result in results:
                st.write(result)
        else:
            st.error("Failed to perform search. Please try again.")