# Import libraries
import streamlit as st
import pandas as pd
from PIL import Image
import src.utils

# Configure the page settings
st.set_page_config(
    page_title="Library • Search",
    page_icon="🔎",
    layout="centered",
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

# Section containers:
header = st.container()
body = st.container()
sidebar = st.sidebar.container()

with sidebar:
    # Import the logo
    image = Image.open("./images/logo.png")

    st.markdown("\n")

    st.image(image, use_column_width=True)

    st.markdown("---")

    # Create a dropdown expander for the "Filter"
    expander = st.sidebar.expander("Filter:", expanded=False)

    # Create a slider for the number of books to display
    number_books = expander.slider(
        "Number of books", 1, 20, 5, help="Select the number of books to display"
    )

    # Create a button to display the most popular books
    most_popular = st.sidebar.button(
        "Most Popular", key="most_popular", help="Display the most popular books"
    )

with header:
    # Page title
    st.title("_Book Recommender_")

with body:
    st.markdown("---")

    # Create a grid for the different buttons
    grid = st.columns(5, gap="medium")

    with grid[0]:
        st.image(
            "https://img.icons8.com/clouds/512/repository.png",
            width=80,
        )
        book = st.button("Book", key="book", help="Similar book recommendations")

    with grid[1]:
        st.image(
            "https://img.icons8.com/clouds/512/walter-white.png",
            width=80,
        )
        author = st.button("Author", key="author", help="Most popular books by author")

    with grid[2]:
        st.image("https://img.icons8.com/clouds/512/calendar--v2.png", width=80)
        year = st.button("Year\t", key="year", help="Most popular books from that year")

    with grid[3]:
        st.image("https://img.icons8.com/clouds/512/organization.png", width=80)
        publisher = st.button(
            "Publisher", key="publisher", help="Most popular books by publisher"
        )

    with grid[4]:
        st.image("https://img.icons8.com/clouds/512/checklist.png", width=80)
        genre = st.button("Genre", key="genre", help="Most popular books in that genre")

    st.markdown("---")

    # Check if button has been clicked
    if book:
        pass

    if author:
        st.selectbox(
            "Type or select and author from the options below:",
            books["Book-Author"].unique(),
        )

        search = st.button("Search", key="search", help="Search for most popular books")

        if search:
            output = f"{number_books} Most Popular Books by {rec_option}"
            recs = src.utils.popularity_rec(author=rec_option, n=number_books)

            src.utils.display_recs(recs, output)

    if year:
        rec_option = st.number_input(
            "Type or select a year from the options below:",
            min_value=books["Year-Of-Publication"].min(),
            max_value=books["Year-Of-Publication"].max(),
        )

        output = f"{number_books} Most Popular Books from {rec_option}"
        recs = src.utils.popularity_rec(year=rec_option, n=number_books)

        src.utils.display_recs(recs, output)

    if publisher:
        rec_option = st.selectbox(
            "Type or select a publisher from the options below:",
            books["Publisher"].unique(),
        )

        output = f"{number_books} Most Popular Books published by {rec_option}"
        recs = src.utils.popularity_rec(publisher=rec_option, n=number_books)

        src.utils.display_recs(recs, output)

    if genre:
        rec_option = st.selectbox(
            "Type or select a genre from the options below:", books["Genre"].unique()
        )

        output = f"{number_books} Most Popular {str.title(rec_option)} Books"
        recs = src.utils.popularity_rec(genre=rec_option, n=number_books)

        src.utils.display_recs(recs, output)
