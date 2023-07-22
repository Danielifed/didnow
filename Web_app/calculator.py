from flask import Blueprint, render_template, request

calculator_app = Blueprint('calculator_app', __name__)

@calculator_app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/arithmetic')
def arithmetic():
    return render_template('arithmetic.html')

@calculator_app.route('/arithmetic', methods=['POST'])
def arithmetic():
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

    pass

@calculator_app.route('/pythagoras')
def pythagoras():
    return render_template('pythagoras.html')

@calculator_app.route('/pythagoras', methods=['POST'])
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
    pass

@calculator_app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html')

@calculator_app.route('/odd', methods=['POST'])
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

    pass

@calculator_app.route('/trigonometry')
def trigonometry():
    return render_template('trigonometry.html')

@calculator_app.route('/trigonometry', methods=['POST'])
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

    pass
