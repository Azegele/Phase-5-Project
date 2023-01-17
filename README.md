# Library Book Recommendation System

![numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)  ![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)   ![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)    ![scikitlearn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)    ![nlp](https://img.shields.io/badge/nlp-209117?style=for-the-badge&logo=nlp&logoColor=white)

![my-image jpg](https://c1.thejournal.ie/media/2022/10/shutterstock_1491910001-2-752x501.jpg)

> The Library Book Recommendation System project is for library patrons and staff who wish to find and recommend books for library patrons. The project provides an automated system for library patrons to find books based on their interests and for library staff to recommend books to library patrons. The system uses a combination of natural language processing, machine learning, and data mining techniques to identify books that best match the library patron's interests. The system also provides library staff with tools to recommend books to library patrons.

---

## Table Of Contents

- [Business Objectives](#business-objectives)
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgements](#acknowledgements)
    - [Institution](#institution)
    - [Technologies Used](#technologies-used)
    - [Data Sources](#data-sources)

---

### Business Objectives

---

> - Apply Natural Language Preprocessing on book description for implementation in the system.
> - Develop a library book recommendation system using different approaches.
> - Deploy the recommendation system using Streamlit.

---

### Project Overview

---

> This project followed the CRISP-DM process. The CRISP-DM process is a data mining process model that describes commonly used approaches that data mining experts use to tackle problems. The CRISP-DM process is divided into six phases; Business Understanding, Data Understanding, Data Preparation, Modelling, Evaluation, and Deployment. The following is a brief description of each phase:

---

- **Business Understanding**: Exploring the business reasons for our data mining effort and what the company hopes to gain from the project. This is done by attempting to come up with an information filtering technique that presents books according to user preferences to ensure increased library book circulation.

- **Data Understanding**: The datasets we utilized comprised of 4 datasets; Books.csv, Ratings.csv, User.csv, Books-extra.csv.

- **Data Preparation**: It mainly involved; selecting the data to discover the columns to be used, cleaning the data to correct and remove erroneous values, formatting the data to effectively perform mathematical operations and integrating the datasets to create a merged dataset for effective analysis.

- **Exploratory Data Analysis**: The goal of this procedure is to summarize the main characteristics of the dataset, which is often done visually.  

- **Modelling**: To further support and provide insight we built various recommender systems; popularity-based system, item-based system, content-based system and hybrid system.

- **Evaluation**: Mean Absolute Error was used to measure the average of absolute deviance between actual and predicted ratings given by users.

- **Recommendation and Conclusion**: It mainly involved interpreting our project findings, offering opinions based on the findings, proposing a solution to the gap discovered in the research that needs to be filled, and the next steps to be undertaken in future analysis.

---

### [Installation](#installation)

> To install the project, follow these steps:

1. Clone the repository

2. Install the requirements.txt file ( `pip install -r requirements.txt` )

3. Navigate to the deployment folder ( `cd deployment`)

4. Run the application ( `streamlit run Home.py` )

5. Open the application in your browser ( `http://localhost:8501` )

---

### [Usage](#usage)

> To use the book recommender, follow these steps:

1. Navigate to the sidebar and go to the `Search` tab

2. Open the expander called `instructions` and read the instructions

3. Once you have inputted all the required information, click the `Recommend` button

4. The results will be displayed below the `Recommend` button

---

### [Contributors](#contributors)
>
> The following people have contributed to this project:

- [Monicah Iwagit]()
- [Belinda Nyamai]()
- [Bradley Azegele]()
- [Emmanuel Kipkorir]()
- [Femi Kamau]()

---

### [License](#license)

---

### [Acknowledgements](#acknowledgements)

#### Institution

- [Moringa School](https://moringaschool.com/)

#### Technologies Used

- [Streamlit](https://streamlit.io/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [NLTK](https://www.nltk.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Google-Books-API](https://developers.google.com/books)

#### Data Sources

- [University of Freiburg](https://www.informatik.uni-freiburg.de/~cziegler/BX/)
- [Google-Books-API](https://developers.google.com/books)

---
---
> Thank you for reading this README.md file. If you have any questions, please contact the contributors of this project.
