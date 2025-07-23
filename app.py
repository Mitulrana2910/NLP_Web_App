# login
# Register
# NER using API calls.
# Sentiment analysis
# Language detection
# from django.contrib.messages.context_processors import messages
import pyngrok
from flask import Flask,render_template,request,redirect,session
from db import Database
import api

app = Flask(__name__)
dbo = Database()

@app.route('/') # Route = Creating url
def index(): # Using "/" means whenever someone type '/' before url let say http://127.0.0.1:5000 the function below the decorator is executed.
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_reg',methods=['post'])
def perform_reg():
    name = request.form.get('u_name')
    email = request.form.get('u_email')
    pwd = request.form.get('u_pwd')

    response = dbo.insert(name, email, pwd)
    if response == 1:
        return render_template("login.html", message="Registration Successful. Kindly login to proceed.", message_type="success")

    else:
        return render_template("register.html", message="Email Already Exists.", message_type="error")


@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('u_email')
    pwd = request.form.get('u_pwd')

    response = dbo.search(email,pwd)

    if response == 1:
        return redirect('/profile')
    else:
        return render_template("login.html",message="Incorrect email/password")

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    text = request.form.get('ner_txt')
    response = api.ner(text)
    print(response)

    return render_template('ner.html',response=response)

@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')

@app.route('/perform_sent',methods=['post'])
def perform_sent():
    text = request.form.get('sent_txt')
    response = api.sent(text)
    print(response)
    result=''
    result = api.sent(text)
    return render_template('sentiment.html',result=result)

@app.route('/summarize')
def summarize():
    return render_template('summarize.html')



app.run(debug=True) # Using debug=True means you just have to refresh the page and changes will appear.


