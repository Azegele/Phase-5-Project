import streamlit as st
import pandas as pd
from math import ceil
import src.utils
from PIL import Image


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


## Initialise Variables

# Drop duplicate titles from the books dataset
shelf = books.drop_duplicates(subset="Book-Title")

# Calculate the maximum page number
max = ceil(shelf.shape[0] / 100)


with sidebar:

    # Display the logo
    image = Image.open("./images/logo.png")
    st.markdown("\n\n")
    st.sidebar.image(image, use_column_width=True)

    # Separator
    st.sidebar.write("---\n")

    # Create a number input to change pages
    page = st.sidebar.number_input(
        label="Page:", min_value=1, max_value=max, value=1, step=1
    )

    # Separator
    st.sidebar.write("---\n")

    # Source code link
    st.sidebar.caption(
        "You can check out the source code [here](https://github.com/Azegele/Phase-5-Project)."
    )
    st.sidebar.write("---")


with header:
    # Page title
    st.title("Books")

    st.markdown("---")


with body:
    # Create a search bar
    search = st.text_input(
        "Search for a book:", help="Enter the title of a book", key="search"
    )

    st.markdown("---")

    if search:
        # Narrow down the dataset based on the search
        recs = books[books["Book-Title"].str.contains(search, case=False)]

        # Drop duplicate titles
        recs = recs.drop_duplicates(subset="Book-Title")

        # Display the books
        src.utils.display_books(recs=recs, columns=10)

    else:
        # Calculate the upper and lower bounds for the pages
        upper = page * 100
        lower = upper - 100

        # Slice the dataset based on the page number
        recs = shelf.iloc[lower:upper, :]

        # Pass the sliced dataset to the display_books function
        src.utils.display_books(recs=recs, columns=10)

        # Display the page number
        st.write(f"Page {page} of {max}")
