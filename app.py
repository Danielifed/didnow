#libraries to be used
from flask import Flask, render_template, flash, redirect, url_for, session, request
import mysql.connector
from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
from pytube import YouTube
import math
from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb

app = Flask(__name__)
picFolder = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = picFolder


#configure MySQL

app.config['MYSQL_HOST'] = 'didnow.cncqfkr0v2be.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'didnowtech'
app.config['MYSQL_PASSWORD'] = 'Ifedaniel6561'
app.config['MYSQL_DB'] = 'didnow'

#init MySQL
mysql = MySQL(app)

#route to the index
@app.route('/')
def index():
    return render_template('index.html')


#route to the about page
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

#route to the calculator section
@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

#this performs simple arithmetc
@app.route('/arithmetic')
def arithmetic():
    return render_template('arithmetic.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = int(request.form['num1'])
    opp = request.form['operator']
    num2 = int(request.form['num2'])
    if opp == "+":
       result = num1 + num2
    elif opp == "-":
        result = num1 - num2
    elif opp == "/":
        result = num1 / num2
    elif opp == "*":
        result = num1 * num2
    else:
        print("%s is not operable. Try '+', '-', '/' or '*'" % opp)

    return render_template('result.html', result=result)

#this performs pythogoras
@app.route('/pythagoras')
def pythagoras():
    return render_template('pythagoras.html')

@app.route('/pythagoras', methods=['POST'])
def pythagoras_calculate():
    side = request.form['side']
    a = float(request.form['a'])
    b = float(request.form['b'])
    result = None

    if side == "hyp":
        result = math.sqrt((a ** 2) + (b ** 2))
    elif side == "adj" or side == "opp":
        if a > b:
            result = math.sqrt((a ** 2) - (b ** 2))
        elif a < b:
            result = math.sqrt((b ** 2) - (a ** 2))
    else:
        error_message = f"{side} is not operable. Try 'hyp', 'opp', or 'adj'"
        return render_template('pythagoras.html', error_message=error_message)

    return render_template('result.html', result=result)

#this gives you the total number in an odd or even range
@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html')

@app.route('/odd', methods=['POST'])
def odd():
     total = 0
     opp = request.form['operator']
     x = int(request.form['start'])
     y = int(request.form['stop'])
     z = y + 1
     
     if opp == "odd":
        for i in range(x, z):
            if i % 2 == 1:
                total += i
     elif opp == "even":
        for i in range(x, z):
            if i % 2 == 0:
                total += i
     else:
        error_message = f"{opp} is not operable. Try 'odd' or 'even'"
        return render_template('odd_even.html', error_message=error_message)

     return render_template('result.html', result=total)

#this calculates trignonometry
@app.route('/trigonometry')
def trigonometry():
    return render_template('trigonometry.html')

@app.route('/trigonometry', methods=['POST'])
def trig():
     trig = request.form['trig']
     x = int(request.form['x'])
     y = int(request.form['y'])
     result = None

     if trig == "sin":
        result = x / y
     elif trig == "cos":
        result = x / y
     elif trig == "tan":
        result = x / y
     else:
        error_message = f"{trig} trig not operable, try 'sin', 'cos', or 'tan'"
        return render_template('trigonometry.html', error_message=error_message)

     return render_template('result.html', result=result)



@app.route('/blog')
def blog():
    wetland = os.path.join(app.config['UPLOAD_FOLDER'], 'wetland.png')
    return render_template('blog.html', user_image = wetland )

#this is for the registration page, here the form validation and length is structured
class RegisterForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=50)])
    middle_name = StringField('Middle Name', [validators.Length(min=1, max=50)])
    last_name = StringField('Last Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=5, max=25)])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        middle_name = form.middle_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        
        #Creating a connection cursor
        cursor = mysql.connection.cursor()

        cursor.execute("INSERT INTO register (first_name, middle_name, last_name,username, email, password) VALUES(%s, %s, %s, %s, %s, %s)", (first_name, middle_name, last_name,username, email, password))

        #commit to DB
        mysql.connection.commit()

        #close connection
        cursor.close()

        flash('You are now registered and can log in', 'Success')

        redirect(url_for('index'))

    return render_template('register.html', form=form)

if __name__=='__main__':
    app.run(debug=False)

