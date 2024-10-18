# Movie Sentiment Analysis Application 🎬

This is a simple web application that performs sentiment analysis on movie reviews. It uses a pre-trained machine learning model (Logistic Regression) to predict whether the sentiment of a given movie review is positive or negative.

**Features ✨**

->Submit a movie review and get a sentiment prediction (positive or negative).

->Built with Flask for the backend.

->Model is trained using Logistic Regression and TF-IDF vectorization.

->Easy deployment using Render.

**Demo 🚀**

A live version of the web application is available at: https://movie-review-sentimentanalysis.onrender.com

**Installation and Setup Instructions 🛠️**

->Dataset : https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews/data

->Clone the repository: https://github.com/roshi45/Movie_review_SentimentAnalysis.git

->Navigate to the project directory: cd Movie_review_SentimentAnalysis

->Install the dependencies: pip install -r requirements.txt

->Run the Flask app locally: python app.py

**Deployment 🖥️**

To deploy the app on Render, follow these steps:


->Ensure that you have a requirements.txt file with all the dependencies (including Gunicorn for production).

->Create a Procfile with the following content:web: gunicorn app:app

->Push the repository to GitHub and connect it to Render. Render will automatically detect and build the project.

->Set the Build Command to:pip install -r requirements.txt

->Set the Start Command to:gunicorn app:app


**File Structure 📁**

├── app.py               # Main Flask application

├── templates

│    └── index.html       # Frontend HTML page

├── logistic_regression_model.pkl  # Saved machine learning model

├── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer

├── requirements.txt     # Project dependencies

└── README.md            # This file


**Model Details 🧠**

The sentiment analysis model is a Logistic Regression classifier trained on a dataset of movie reviews. The model takes in a review, transforms it using a TF-IDF Vectorizer, and predicts whether the review has a positive or negative sentiment.


Preprocessing:Text data is preprocessed using TF-IDF (Term Frequency-Inverse Document Frequency).


Model:Logistic Regression model trained on labeled movie reviews.


