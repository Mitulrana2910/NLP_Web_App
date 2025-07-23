# 🧠 NLP Web App

A simple Flask-based web application for performing various analytical procedures using Natural Language Processing (NLP). Users can enter text and get instant sentiment predictions like *Positive* or *Negative*.

## 🚀 Features

- ✅ Web-based user interface built with Flask and HTML.
- ✅ Clean UI with integrated CSS and favicon support.
- ✅ Real-time sentiment analysis on submitted text.
- ✅ Modular structure for easy extension (NER, summarization, etc.).

## 🧰 Tech Stack

- Python 3.11+
- Flask
- HTML + CSS
- NLP (basic logic or integration with models e.g., Hugging Face)

---

## 📁 Project Structure

NLP_Web_App/
│
├── app.py                  # Main Flask application (routes & server setup)
├── api.py                  # Hugging Face API interaction logic (sentiment, NER, summarization)
├── db.py                   # User management logic (e.g., login/register using users.json)
├── users.json              # JSON file to store registered users
│
├── static/                 # Static assets
│   ├── favicon.ico         # Favicon for the website
│   └── style.css           # Main stylesheet
│
├── templates/              # HTML templates for the Flask app
│   ├── login.html          # Login form
│   ├── register.html       # Registration form
│   ├── profile.html        # User profile with analysis tools
│   ├── ner.html            # Named Entity Recognition page
│   ├── sentiment.html      # Sentiment analysis page
│   └── summarize.html      # Text summarization page
│
└── README.md               # Project overview and documentation
