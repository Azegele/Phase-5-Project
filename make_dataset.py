# %% Import Libraries
import aiohttp  # Aiohttp module used to send a request
import asyncio  # Asyncio module used to run the asynchronous code
import time  # Time module used to sleep the program for a few seconds
import pandas as pd  # Pandas module used to create a dataframe and store the data
import warnings  # Warnings module used to ignore warnings

# %% Library Settings
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)

# %% Create a new dataframe to store the data
data = pd.DataFrame(
    columns=[
        "authors",
        "published_date",
        "description",
        "isbn_10",
        "isbn_13",
        "page_count",
        "categories",
        "maturity_rating",
        "language",
        "join_isbn_10",
    ]
)

## The following code has been commented out so that the data is not overwritten when the program is run again
# data.to_csv("./data/books.csv", index=True)


# Define a function to return none if the input is empty
def return_none(isbn):
    """Function to return none if the isbn that is requested to the API is empty or does not exist"""

    # Return a dictionary with the values set to None
    return {
        "authors": None,
        "published_date": None,
        "description": None,
        "isbn_13": None,
        "page_count": None,
        "categories": None,
        "maturity_rating": None,
        "language": None,
        "join_isbn_10": isbn,
    }


# Define main async function to run the code
async def main():
    """Main async function to run the code"""

    # Load the data
    books = pd.read_csv(
        "./data/BX-Books.csv",
        sep=";",
        error_bad_lines=False,
        encoding="latin1",
        chunksize=40,
    )

    # Initialize an empty list to store the data from the API
    api_data = []

    # Loop through the chunks of data
    for index, chunk in enumerate(books, start=1):

        # --- The following section was written so that the program can continue from where it left off if it is interrupted ---

        # Read (or re-read) the csv file containing the extracted the book data from the API
        books = pd.read_csv("data/books.csv")

        # Get the total number of books that have been processed
        total_books = books.shape[0]

        # Check if the chunk has already been processed, if so, skip the chunk
        if index < (total_books / 40):
            continue

        # --- End of section ---

        # Extract the ISBN numbers from the chunk
        isbns = chunk["ISBN"].tolist()

        # Open a session that will be used to send a request to the API
        async with aiohttp.ClientSession() as session:

            # Initialize an empty list to store the tasks (requests) that will be sent to the API
            tasks = []

            # Loop through the ISBN numbers and create a task for each ISBN number
            for isbn in isbns:
                task = asyncio.ensure_future(get_data(session, isbn))
                tasks.append(task)

            # Await the tasks and store the data in the list "api_data"
            api_data.append(await asyncio.gather(*tasks))

        # Print the number of books that have been processed to the console to keep track of the progress
        print(f"Number of books: {total_books + 40}")

        # Read the csv file, append the data from the API to the dataframe, and save the dataframe to the csv file
        pd.read_csv("./data/books.csv").append(api_data[-1]).to_csv(
            "./data/books.csv", index=False
        )

        # Introduction of a sleep function of 1 minute (60 seconds) to avoid rate limit
        time.sleep(60)


# Define a function to get the data from the Google Books API
async def get_data(session, isbn):
    """Function to get the data from the Google Books API"""

    # Define the url to send a request to
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"

    # Set the rate limit to True so that the while loop can run at least once
    rate_limit = True

    # Initialize a while loop to handle any rate limit errors. The program will sleep for 10 seconds and then try again if the rate limit is exceeded.
    while rate_limit:

        # Send a request to the API using the session object
        async with session.get(url) as response:

            # Print the status of the response
            print(f"Status: {response.status}")

            # Check if the status is 200 (OK)
            if response.status == 200:

                # Set the rate limit to False so that the while loop can be exited because the rate limit is not exceeded
                rate_limit = False

                # Await the response and convert it to a json object
                result_data = await response.json()

                # Extract the volume information (book information) from the json object using the key "volumeInfo"
                try:
                    volume_info = result_data["items"][0][
                        "volumeInfo"
                    ]  # If the book exists, the volume information will be stored in the variable "volumeInfo"
                except:
                    return return_none(
                        isbn
                    )  # If the book does not exist, the function return_none will be called

                # Extract the author(s) names
                try:
                    authors = volume_info[
                        "authors"
                    ]  # If the book has an author, the author's name will be stored in the variable "authors"
                except:
                    authors = None  # If the book does not have an author, the variable "authors" will be set to None

                # Extract the published date
                try:
                    published_date = volume_info[
                        "publishedDate"
                    ]  # If the book has a published date, the published date will be stored in the variable "publishedDate"
                except:
                    published_date = None  # If the book does not have a published date, the variable "publishedDate" will be set to None

                # Extract the description
                try:
                    description = volume_info[
                        "description"
                    ]  # If the book has a description, the description will be stored in the variable "description"
                except:
                    description = None  # If the book does not have a description, the variable "description" will be set to None

                # Extract isbn-10 number
                try:
                    isbn_10 = volume_info["industryIdentifiers"][0][
                        "identifier"
                    ]  # If the book has an isbn-10 number, the isbn-10 number will be stored in the variable "industryIdentifiers"
                except:
                    isbn_10 = None  # If the book does not have an isbn-10 number, the variable "industryIdentifiers" will be set to None

                # Extract isbn-13 number
                try:
                    isbn_13 = volume_info["industryIdentifiers"][1][
                        "identifier"
                    ]  # If the book has an isbn-13 number, the isbn-13 number will be stored in the variable "industryIdentifiers"
                except:
                    isbn_13 = None  # If the book does not have an isbn-13 number, the variable "industryIdentifiers" will be set to None

                # Extract the page count
                try:
                    page_count = volume_info[
                        "pageCount"
                    ]  # If the book has a page count, the page count will be stored in the variable "pageCount"
                except:
                    page_count = None  # If the book does not have a page count, the variable "pageCount" will be set to None

                # Extract the categories
                try:
                    categories = volume_info[
                        "categories"
                    ]  # If the book has categories, the categories will be stored in the variable "categories"
                except:
                    categories = None  # If the book does not have categories, the variable "categories" will be set to None

                # Extract the maturity rating
                try:
                    maturity_rating = volume_info[
                        "maturityRating"
                    ]  # If the book has a maturity rating, the maturity rating will be stored in the variable "maturityRating"
                except:
                    maturity_rating = None  # If the book does not have a maturity rating, the variable "maturityRating" will be set to None

                # Extract the language
                try:
                    language = volume_info[
                        "language"
                    ]  # If the book has a language, the language will be stored in the variable "language"
                except:
                    language = None  # If the book does not have a language, the variable "language" will be set to None

                # Return the data as a dictionary
                return {
                    "authors": authors,
                    "published_date": published_date,
                    "description": description,
                    "isbn_10": isbn_10,
                    "isbn_13": isbn_13,
                    "page_count": page_count,
                    "categories": categories,
                    "maturity_rating": maturity_rating,
                    "language": language,
                    "join_isbn_10": isbn,
                }

            # Check if the status is 429 (Rate limit exceeded)
            elif response.status == 429:
                # Print a message to the console
                print("Rate limit exceeded. Sleeping for 10 seconds.")

                # Sleep the program for 10 seconds
                time.sleep(10)

            # If the status is not 200 or 429, return None for all the variables and set the rate limit to False so that the while loop can be exited
            else:
                rate_limit = False
                return return_none(isbn)


# %% Run the main function
await main()

# %% Load the different csv files into pandas DataFrames (The program was run from 5 different computers to more efficiently extract the data from the API)
books_1 = pd.read_csv("./data/books_1.csv", encoding="latin-1")
books_2 = pd.read_csv("./data/books_2.csv", encoding="latin-1")
books_3 = pd.read_csv("./data/books_3.csv", encoding="latin-1")
books_4 = pd.read_csv("./data/books_4.csv", encoding="latin-1")
books_5 = pd.read_csv("./data/books_5.csv", encoding="latin-1")

# %% Concatenate the DataFrames into one dataframe on the rows
books = pd.concat([books_1, books_2, books_3, books_4, books_5], axis=0)

# Drop the duplicate rows
books.drop_duplicates(inplace=True)
books

# %% Export the combined DataFrame to a csv file
books.to_csv("./data/books.csv", index=False)
