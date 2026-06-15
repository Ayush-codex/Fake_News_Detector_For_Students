# Fake News Detector for Students

## Overview

Fake News Detector for Students is a Machine Learning-based web application that helps users identify whether a news article is real or fake. The system analyzes the text of news articles using Natural Language Processing (NLP) techniques and predicts the authenticity of the news.

The application is deployed using Streamlit and provides a simple, user-friendly interface for students and general users.

## Features

* Detects Fake and Real News Articles
* Text Preprocessing and Cleaning
* TF-IDF Vectorization
* Machine Learning-based Classification
* Interactive Streamlit Web Interface
* Fast and Easy Predictions

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Natural Language Processing (NLP)
* TF-IDF Vectorizer
* Logistic Regression
* Streamlit

## Dataset

The project uses a Fake News Dataset containing:

* Fake News Articles
* Real News Articles

Dataset Source:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

## System Architecture

Dataset
→ Data Preprocessing
→ TF-IDF Vectorization
→ Logistic Regression Model
→ Prediction Engine
→ Streamlit Web Application
→ Real/Fake News Result

## Project Structure

FakeNewsDetector/

├── app.py

├── fake_news_detector.ipynb

├── model.pkl

├── vectorizer.pkl

├── requirements.txt

├── Fake.csv

├── True.csv

└── README.md

## Installation

1. Clone the repository

git clone <repository-link>

2. Navigate to project directory

cd FakeNewsDetector

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run app.py

## Usage

1. Open the Streamlit application.
2. Enter a news article in the text box.
3. Click on "Check News".
4. The system predicts whether the news is Real or Fake.

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Feature Extraction using TF-IDF
4. Model Training using Logistic Regression
5. Model Evaluation
6. Model Deployment using Streamlit

## Results

The model achieves high accuracy in distinguishing between fake and real news articles by utilizing NLP and machine learning techniques.

## Future Scope

* Deep Learning-based Classification
* BERT and Transformer Models
* News Source Verification
* Multilingual Fake News Detection
* Browser Extension Integration
* Real-Time News Analysis

## Conclusion

The Fake News Detector for Students provides an effective solution for identifying misleading news content. By leveraging machine learning and natural language processing techniques, the system assists users in making informed decisions and promotes digital literacy.

## Author

Ayush Bajpai

B.Tech (Artificial Intelligence & Machine Learning)
