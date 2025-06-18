#  Language Detection Web Application

This is a web-based Language Detection App powered by **Flask** and **scikit-learn** on the backend, and a simple **HTML/CSS/JavaScript** frontend. It uses a trained **Naive Bayes classifier** on TF-IDF features with character-level n-grams to identify the language of a given text input.

---

##  Features

-  ML Model trained on multilingual dataset using `MultinomialNB`.
-  Accepts user input and predicts the language.
-  REST API endpoint to integrate with any frontend.
-  Secured using an API key.
-  CORS-enabled to work across domains.
-  Minimal and clean user interface.

---

##  Tech Stack

| Backend   | Frontend        | ML/NLP Libraries      |
|-----------|------------------|------------------------|
| Flask     | HTML, CSS, JS     | scikit-learn, pandas, numpy |
| Flask-CORS | Fetch API        | TfidfVectorizer, Naive Bayes |

---

##  Project Structure

language-detector/
│
├── app.py # Flask backend with ML model
├── dataset.csv # Training dataset with text and language
├── index.html # Frontend HTML page (optional if served via Flask)
└── README.md # Project documentation

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/language-detector.git
cd language-detector
2. Install Dependencies
Make sure you have Python 3 installed.

bash
Copy
Edit
pip install flask flask-cors scikit-learn pandas numpy
3. Place the Dataset
Ensure your dataset.csv file is placed in the project directory. The CSV should have at least two columns:

Text: the actual text sample.

language: the label indicating the language.

4. Run the Flask App
bash
Copy
Edit
python app.py
Your Flask server will start on http://127.0.0.1:5000.

5. Open the Frontend
Open the index.html file in your browser (via double-click or Live Server extension if using VS Code).

Enter text and click Detect Language — it will fetch the result from the Flask API and display it on the page.

 API Usage
 Authentication
You must provide a valid API key in the request header:

makefile
Copy
Edit
x-api-key: AP2024254000295
 Endpoint
bash
Copy
Edit
POST /predict
 Request Body (JSON)
json
Copy
Edit
{
  "text": "Bonjour tout le monde"
}
 Response
json
Copy
Edit
{
  "language": "French"
}
 Security
The backend uses an x-api-key header to restrict access to authorized clients.

CORS headers are configured to allow requests from different origins.

 Future Improvements
Use a larger and more diverse dataset for better accuracy.

Add more supported languages.

Deploy the app on platforms like Heroku, Render, or AWS.

Add a model accuracy endpoint or confidence score in the API response.

Enhance UI/UX for mobile support.

 Author
Vishwanath Tiwari

Feel free to reach out or contribute!

