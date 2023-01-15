# Import libraries
import streamlit as st
import pandas as pd
from PIL import Image
from math import ceil
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


with header:

    # Page title
    st.title("Recommender")

    st.markdown("---")

    expander = st.expander("Instructions!", expanded=False)

    expander.markdown(
        """Please follow the instructions below to use the ***Recommender***.\n\n>1. Select what you are searching for from the radio button options.\n>2. Enter the term you are searching for.\n>3. Select the number of books to display.\n>4. Click the **Recommend** button.\n\nThank you for using the recommender system!\n\nRegards,\n\n*The Librarians*"""
    )

    expander.info(
        "If you select the **Book** option, you will only have 5 books recommended."
    )

    st.markdown("---")

with body:

    # Create a form to get the user input
    with st.form(key="search_form"):

        st.write(
            "<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>",
            unsafe_allow_html=True,
        )

        st.write(
            "<style>div.st-bf{flex-direction:column;} div.st-ag{padding-left:10px;}</style>",
            unsafe_allow_html=True,
        )

        # Create radio buttons to select the search type: (Book, Author, Publisher, Year, Category)
        search_type = st.radio(
            "Search Type:",
            ("Book", "Author", "Publisher", "Year", "Genre"),
            help="Select the type metadata you are searching for",
        )

        st.markdown("---")

        search_term = st.text_input(
            "Search:", help="Enter the term you are searching for"
        )

        st.markdown("---")

        number_books = st.slider(
            "Number of books:", 1, 10, 5, help="Select the number of books to display"
        )

        st.markdown("---")

        st.write(
            "<style>div.row-widget.stButton > div{justify-content: center;} </style>",
            unsafe_allow_html=True,
        )

        submit = st.form_submit_button("Recommend", help="Get recommendations")

        # Throw a warning if the search is left empty
        if submit and search_term == "":
            st.warning("Search term cannot be left empty")
            st.stop()

    if submit:
        if search_type == "Book":

            # Warn the user of the time
            st.warning("This may take a few seconds...")

            # Get the recommendations
            output, recs = src.utils.hybrid_recommender(search_term)

        elif search_type == "Author":
            # Get the most popular books by the author
            recs = src.utils.popularity_rec(author=search_term, n=number_books)

            if recs.shape[0] == 0:
                output = (
                    f"Sorry, no books by _{search_term}_ were found in the database."
                )

            elif recs.shape[0] == 1:
                output = f"The Most Popular Book by {search_term}:"

            else:
                output = f"The _{number_books}_ Most Popular Books by {search_term}:"

        elif search_type == "Publisher":
            # Get the most popular books by the publisher
            recs = src.utils.popularity_rec(publisher=search_term, n=number_books)

            if recs.shape[0] == 0:
                output = (
                    f"Sorry, no books from _{search_term}_ were found in the database."
                )

            elif recs.shape[0] == 1:
                output = f"The Most Popular Book from {search_term}:"

            else:
                output = f"The _{number_books}_ Most Popular Books by {search_term}:"

        elif search_type == "Year":

            # Raise an error message if an invalid year is entered
            if not search_term.isdigit() or len(search_term) != 4:
                st.error("Please enter a valid year")
                st.stop()

            # Convert the year to an integer
            search_term = int(search_term)

            # Get the most popular books by the year
            recs = src.utils.popularity_rec(year=search_term, n=number_books)

            if recs.shape[0] == 0:
                output = f"Sorry, no books written in _{search_term}_ were found in the database."

            elif recs.shape[0] == 1:
                output = f"The Most Popular Book from {search_term}:"

            else:
                output = (
                    f"The _{number_books}_ Most Popular Books from _{search_term}_:"
                )

        elif search_type == "Genre":
            # Get the most popular books from the category
            recs = src.utils.popularity_rec(category=search_term, n=number_books)

            if recs.shape[0] == 0:
                output = f"Sorry, no _{search_term}_ books were found in the database."

            elif recs.shape[0] == 1:
                output = f"The Most Popular {search_term} Book:"

            else:
                output = f"The _{number_books}_ Most Popular {search_term} Books:"

        # Display the recommendations
        src.utils.display_books(recs, output, columns=5, search=True)

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
