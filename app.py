from flask import Flask, request, render_template
import joblib

# Load the saved model and vectorizer
model = joblib.load('logistic_regression_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define home route with input form
@app.route('/')
def home():
    return render_template('index.html')

# Define route to handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        # Transform the input review using the loaded TF-IDF vectorizer
        transformed_review = tfidf.transform([review])
        # Get the prediction from the model
        prediction = model.predict(transformed_review)
        sentiment = 'positive' if prediction[0] == 1 else 'negative'
        return render_template('index.html', prediction_text=f'Sentiment: {sentiment}')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
