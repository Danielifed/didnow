from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
#from flask_mysqldb import Mysql
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

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

@app.route('/trig', methods=['POST'])
def trig():
     trig = request.form['trig']
     x = float(request.form['x'])
     y = float(request.form['y'])
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

     return render_template('trigonometry.html', result=result)

@app.route('/blog')
def blog():
    return render_template('blog.html')
##class RegisterForm(Form):
    FirstName = StringField('FirstName', [validators.Length(min=1, max=50)])
if __name__=='__main__':
    app.run(debug=True) 
