# Depression Detection Web Application

## Intro

This repository contains code for a web application designed to detect and assess depression levels based on user inputs. The application uses a combination of machine learning models and data analysis scripts to provide users with insights into their potential depression type and severity.

## Program

The program is a Flask-based web application that allows users to log in, fill out a questionnaire related to various factors that can contribute to depression, and then receive an assessment of their depression type and severity. The application is backed by a Firebase database for user authentication and data storage.

## Features

- User registration and login functionality
- Interactive questionnaire to gather user input
- Integration of machine learning model for depression type assessment
- Display of depression severity grade based on user inputs
- User-friendly web interface for seamless interaction

## About the Machine Learning Model

The machine learning model included in this project is designed to predict the type and severity of depression based on user-provided answers to the questionnaire. It utilizes a linear regression model trained on a dataset of depression-related factors. The model outputs a depression type and severity score that is used to generate a corresponding severity grade.

## About the Script

The Python script (`mlscript.py`) in this repository contains the function `calculate_depression_type`, which calculates the depression type and severity based on user input. The script utilizes a set of predefined factors and weights to determine the depression type and severity score. The output of this function is used in the web application for generating assessment results.

### Function

The `calculate_depression_type` function takes a row of user input, calculates the depression type and severity, and returns an updated row with the calculated values.

## Usage and Execution

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure the Firebase credentials in `app.py` to enable user authentication and database operations.
4. Run the Flask application using `python app.py`.
5. Access the application in your web browser by navigating to `http://localhost:5000`.

Follow the on-screen instructions to register, log in, and complete the depression assessment questionnaire. The application will provide you with an assessment of your depression type and severity.

## Web-App link
[https://depression-detector--shubhangigupta8.repl.co/](https://depression-detector--shubhangigupta8.repl.co/)
