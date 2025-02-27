import streamlit as st  

# Page Title
st.set_page_config(page_title="TGT - Elevate Your IT Career", layout="wide")

# Load HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Display HTML in Streamlit
st.components.v1.html(html_code, height=800, scrolling=True)
