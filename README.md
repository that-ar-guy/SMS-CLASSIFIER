# SMS-CLASSIFIER

## Overview
This is a simple spam classifier application built using Streamlit, NLTK, and a machine learning model. The application takes a user-inputted message and classifies it as spam or not spam (ham).

## Files
1. **P1.py**: This is the main application file that utilizes the Streamlit framework for creating the user interface. It also loads the pre-trained machine learning model (`model.pkl`) and the vectorizer (`vectorizer.pkl`) for text processing.

2. **model.pkl**: This file contains the pickled machine learning model trained to classify messages as spam or not spam. The model is loaded in the `app.py` file for making predictions.

3. **vectorizer.pkl**: This file contains the pickled vectorizer used to transform input text data into a format suitable for the machine learning model. It is loaded in the `app.py` file for preprocessing user-inputted messages.

## Text Preprocessing
The application performs text preprocessing on the user-inputted message before making predictions. The `stemming` function in `app.py` is responsible for converting the input text into a format suitable for the machine learning model. It involves removing non-alphabetic characters, converting to lowercase, tokenization, stemming, and removing English stopwords.

## How to Run the Application
To run the SMS Classifier app, make sure you have Python and the required libraries installed. You can install the necessary dependencies using the following command:
```bash
pip install streamlit nltk
