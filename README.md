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
```
NLP_Web_App/
│
├── app.py # Main Flask app (routing & server setup)
├── api.py # Hugging Face API integration (sentiment, NER, summarization)
├── db.py # User management logic (login, registration, etc.)
├── users.json # JSON file to store registered user data
│
├── static/ # Static assets (CSS, favicon)
│ ├── favicon.ico # Favicon for the web app
│ └── style.css # Main stylesheet
│
├── templates/ # HTML templates for all web pages
│ ├── login.html # Login page
│ ├── register.html # Registration page
│ ├── profile.html # User dashboard with analysis options
│ ├── ner.html # Named Entity Recognition page
│ ├── sentiment.html # Sentiment Analysis page
│ └── summarize.html # Text Summarization page
│
└── README.md # Project documentation
```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
NLP_Web_App/
│
├── app.py # Main Flask app (routing & server setup)
├── api.py # Hugging Face API integration (sentiment, NER, summarization)
├── db.py # User management logic (login, registration, etc.)
├── users.json # JSON file to store registered user data
│
├── static/ # Static assets (CSS, favicon)
│ ├── favicon.ico # Favicon for the web app
│ └── style.css # Main stylesheet
│
├── templates/ # HTML templates for all web pages
│ ├── login.html # Login page
│ ├── register.html # Registration page
│ ├── profile.html # User dashboard with analysis options
│ ├── ner.html # Named Entity Recognition page
│ ├── sentiment.html # Sentiment Analysis page
│ └── summarize.html # Text Summarization page
│
└── README.md # Project documentation

