# Sentiment Analyser

## Overview

**Sentiment Analyser** is a web application developed using **Python**,
**Django**, and **TextBlob** that performs sentiment analysis on
user-entered text. The application identifies whether the input
expresses a **Positive**, **Negative**, or **Neutral** sentiment and
displays the corresponding **polarity** and **subjectivity** scores.

The project also includes user authentication and stores each user's
previous sentiment analyses, allowing users to review their analysis
history after logging in.

------------------------------------------------------------------------

## Features

-   User registration and login
-   Secure authentication using Django's `AbstractUser`
-   Text sentiment analysis using the TextBlob library
-   Automatic sentiment classification:
    -   Positive
    -   Negative
    -   Neutral
-   Displays:
    -   Sentiment
    -   Polarity
    -   Subjectivity
-   Stores previous analyses in the database
-   View previous analyses from the dashboard
-   Responsive and modern user interface
-   Built with Django and SQLite

------------------------------------------------------------------------

## Technology Stack

-   Python
-   Django
-   TextBlob
-   HTML5
-   CSS3
-   Bootstrap 5
-   SQLite

------------------------------------------------------------------------

## Project Structure

``` text
SentimentAnalyser/
│
├── analyzer/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── sentiment_project/
├── db.sqlite3
├── manage.py
└── README.md
```

------------------------------------------------------------------------

## Modules

### Home

Provides an introduction to the application and navigation to the login
and registration pages.

### User Authentication

Allows users to create an account, log in securely, and log out.

### Sentiment Analysis

Accepts user input, analyzes the text using TextBlob, and calculates: -
Sentiment - Polarity - Subjectivity

### Analysis History

Stores every analysis in the database and displays previous analyses for
the logged-in user.

------------------------------------------------------------------------

## Database

### User

Uses Django's custom `AbstractUser` model for authentication.

### Analysis

Each record stores: - User - Input text - Sentiment - Polarity -
Subjectivity - Date and time of analysis

------------------------------------------------------------------------

## How It Works

1.  Register a new account or log in.
2.  Enter text in the dashboard.
3.  Click **Analyze**.
4.  TextBlob processes the input text.
5.  The application displays the sentiment, polarity, and subjectivity
    scores.
6.  The analysis is stored in the database.
7.  Users can review previous analyses from the dashboard.

------------------------------------------------------------------------

## Sentiment Classification

-   **Positive** -- Polarity \> 0
-   **Negative** -- Polarity \< 0
-   **Neutral** -- Polarity = 0

------------------------------------------------------------------------

## Installation

``` bash
git clone <repository-url>
cd SentimentAnalyser

python -m venv venv

# Windows
venv\Scripts\activate

pip install django textblob

python -m textblob.download_corpora

python manage.py migrate

python manage.py runserver
```

Open:

    http://127.0.0.1:8000/

------------------------------------------------------------------------

## Future Enhancements

-   Export analysis reports
-   Advanced NLP models
-   Search and filter analysis history
-   Charts and analytics
-   Multi-language sentiment analysis

------------------------------------------------------------------------

## Author

Developed as an academic Django project demonstrating sentiment analysis
using Natural Language Processing (NLP) with TextBlob.
