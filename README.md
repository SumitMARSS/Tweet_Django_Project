# Django Tweet Management Project

## Overview

    This Django-based web application provides a platform for managing tweets, including CRUD operations, user authentication and authorization, and a search functionality to find specific tweets or comments.

## Features

## 1. CRUD Operations for Tweets

    Create: Users can create new tweets with a text description and an optional photo.
    Read: View all tweets in a paginated list or detailed view.
    Update: Edit existing tweets to modify text or replace the photo.
    Delete: Remove unwanted tweets securely.

## 2. Authorization and Authentication

    User Registration: Allows new users to register.
    Login/Logout: Secure login and logout functionality using Django's built-in authentication system.
    User-based Access Control: Users can only modify or delete their own tweets.
    CSRF Protection: Secures forms against Cross-Site Request Forgery attacks using Django's built-in CSRF token.

## 3. Search Bar
    Search Functionality: A search bar that allows users to search for tweets by keywords.
    Dynamic Results: Displays tweets matching the search term in real time.
    Technologies Used
    Backend: Django (Python)
    Frontend: HTML, CSS, Bootstrap
    Database: SQLite (default with Django)

# Installation

## Clone the repository:

    git clone <repository-url>
    cd <project-directory>

## Create a virtual environment and activate it:

    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate

## Install dependencies:

    pip install -r requirements.txt

## Apply migrations:

    python manage.py migrate

## Start the development server:

    python manage.py runserver

### Access the application in your browser at:  http://127.0.0.1:8000

How to Use

## Tweet Management
    Create: Navigate to the "Create Tweet" page to add a new tweet.
    View: Browse the list of tweets on the homepage.
    Edit: Click the "Edit" button on a tweet to modify it.
    Delete: Click the "Delete" button to remove a tweet.

## Authentication

    Register: Sign up for a new account using the "Register" page.
    Login: Log in using valid credentials.
    Logout: Click the "Logout" button to end the session.

## Search Functionality
    Use the search bar to find tweets containing specific keywords.

## Project Structure

    project-directory/
    ├── manage.py
    ├── db.sqlite3
    ├── app_name/
    │   ├── migrations/
    │   ├── static/
    │   ├── templates/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── templates/
    │   ├── base.html
    │   ├── tweet_list.html
    │   ├── tweet_detail.html
    │   ├── tweet_form.html
    │   └── tweet_confirm_delete.html
    └── requirements.txt

