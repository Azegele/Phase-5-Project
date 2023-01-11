import streamlit as st

st.set_page_config(
    page_title="Library • Profile",
    page_icon="👤",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Create the containers for the different pages and the different sections
header = st.container()
sidebar = st.sidebar.container()

with header:
    st.title("_Profile_")
    st.sidebar.header("Profile")
    st.markdown("Coming Soon...")
