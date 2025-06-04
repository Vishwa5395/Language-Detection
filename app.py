from flask import Flask,request,jsonify
from flask_cors import CORS

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\tiwar\Downloads\dataset.csv")

x = np.array(df['Text'])
y = np.array(df['language'])

vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 3))  # Character n-grams help with space-less languages
X = vectorizer.fit_transform(x)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=3) 

model = MultinomialNB()
model.fit(X_train, y_train)

app = Flask(__name__) 
CORS(app, resources={r"/": {"origins": "*"}}, supports_credentials=True)

API_KEY="AP2024254000295" #API key to fetch data random

@app.route('/predict',methods=['POST'])
def predict():
    
    if request.headers.get('x-api-key')!=API_KEY:
        return jsonify({'error':'Unauthorized'}),401 #If API is not same then unauthorization error status code 401
    
    data=request.json
    text=data.get('text','')

    if not text:
        return jsonify({'error':'No text provided'}),400
    
    text_transformed=vectorizer.transform([text])
    predicted_lang=model.predict(text_transformed)[0]

    return jsonify({"language":predicted_lang})


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, x-api-key'
    return response


if __name__=='__main__':
    app.run(debug=True)







# # Check accuracy
# score = model.score(X_test, y_test)
# print(f"Model Accuracy: {score * 100:.2f}%")

# Function to Detect Language from User Input
# def detect_language(text):
#     text_transformed = vectorizer.transform([text])  # Convert input text to numerical features
#     predicted_language = model.predict(text_transformed)[0]  # Predict language
#     return predicted_language

# Get user input and predict the language
# while True:
#     user_text = input("Enter a sentence or paragraph (or type 'exit' to stop): ")
#     if user_text.lower() == "exit":
#         break
#     predicted_lang = detect_language(user_text)
#     print(f"Predicted Language: {predicted_lang}")
