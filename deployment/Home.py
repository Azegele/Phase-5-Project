import streamlit as st
from PIL import Image
import pandas as pd

# Configure the page settings
st.set_page_config(
    page_title="Library • Home",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Import data
books = pd.read_csv("data/books.csv.gzip", compression="gzip", encoding="iso-8859-1")

# Section containers: header, body, and sidebar
header = st.container()
body = st.container()
sidebar = st.sidebar.container()

with header:
    # Page title
    st.title("_Library_ - Home")

    # Welcome message
    expander = st.expander("Message!", expanded=False)
    expander.markdown(
        """Dear User,\n\nWelcome to the ***Library Book Recommender System***!\n\nThis system is designed to help you find books that you will enjoy reading.\n\nYou are currently viewing the **Home** page.\n\nTo get started, click on the **Search** tab in the sidebar. You can also view the **Bookshelf** tab to view our books.\n\nRegards,\n\n*The Librarians*"""
    )

    # # Display the cover image
    # align = st.columns(3)

    # with align[0]:
    #     cover = Image.open("./images/cover.png")
    #     st.markdown("\n\n")
    #     st.image(cover, width=630)

    st.markdown("---")

with body:
    # Dashboard title
    align = st.columns(3)

    with align[1]:
        st.markdown("## Dashboard")

    st.markdown("---")

    # Create metric boxes for the library statistics
    col1, col2, col3, col4 = st.columns(4, gap="large")

    col1.image("https://img.icons8.com/clouds/512/repository.png", width=80)
    col1.metric("Books", books["ISBN"].nunique(), help="Total number of books")

    col2.image("https://img.icons8.com/clouds/512/walter-white.png", width=80)
    col2.metric("Authors", books["authors"].nunique(), help="Total number of authors")

    col3.image("https://img.icons8.com/clouds/512/organization.png", width=80)
    col3.metric(
        "Publishers", books["Publisher"].nunique(), help="Total number of publishers"
    )

    col4.image("https://img.icons8.com/clouds/512/checklist.png", width=80)
    col4.metric("Genres", books["categories"].nunique(), help="Total number of genres")

    st.markdown("---")

    ## Plots (Graphs)

    # Plot the number of books per author

    # Plot the number of books per year

    # Plot the number of books per publisher

    # Plot the number of books per genre


with sidebar:
    # Display the logo
    image = Image.open("./images/logo.png")
    st.markdown("\n\n")
    st.sidebar.image(image, use_column_width=True)

    # Separator
    st.sidebar.write("---\n")

    # Source code link
    st.sidebar.caption(
        "You can check out the source code [here](https://github.com/Azegele/Phase-5-Project)."
    )
    st.sidebar.write("---")
