import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Library • Bookshelf",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Import data
books = pd.read_csv(
    "./data/books.csv.gzip",
    compression="gzip",
    encoding="iso-8859-1",
)
combined = pd.read_csv(
    "./data/combined.csv.gzip", compression="gzip", encoding="iso-8859-1"
)

# Create the containers for the different pages and the different sections
header = st.container()
page = st.container()
body = st.container()
sidebar = st.sidebar.container()


with header:
    st.title("_Books_")
