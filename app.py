#libraries to be used
from flask import Flask, render_template, flash, redirect, url_for, session, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
from pytube import YouTube
import math

app = Flask(__name__)
app.secret_key = 'Ifedaniel@0704&6561'

#configure MySQL
app.config['MYSQL_HOST'] = 'aws.connect.psdb.cloud'
app.config['MYSQL_USER'] = 'e32m5rf7dwc2ekmhtp9x'
app.config['MYSQL_PASSWORD'] = 'pscale_pw_XXMMmJKrIbjSYlcNOeDXXweaGXLTy4zXVzUtTFtgz9S'
app.config['MYSQL_DB'] = 'didnow'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

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

#this functions as youtube video downloader
@app.route('/youtube_downloader', methods=['GET', 'POST'])
def youtube_downloader():
    if request.method == 'POST':
        url = request.form['url'].strip()
        save_path = "downloads"  # Set the default save path to "downloads"

        if not url:
            status = "Please provide a valid YouTube URL."
            return render_template('youtube_downloader.html', status=status)

        try:
            youtube = YouTube(url)
            video_streams = youtube.streams.filter(file_extension='mp4')

            if not video_streams:
                status = "No video formats available for download."
                return render_template('youtube_downloader.html', status=status)

            available_qualities = list(set([stream.resolution for stream in video_streams]))

            if available_qualities:
                available_qualities.sort(reverse=True)
            else:
                available_qualities = None

            return render_template('youtube_downloader.html', url=url, available_qualities=available_qualities)

        except Exception as e:
            status = "Invalid YouTube URL or error fetching video details."
            print(e)
            return render_template('youtube_downloader.html', status=status)

    return render_template('youtube_downloader.html', status=None, available_qualities=[])

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url'].strip()
    save_path = "downloads"  # Set the default save path to "downloads"
    quality = request.form['quality']

    try:
        youtube = YouTube(url)
        video_stream = youtube.streams.filter(file_extension='mp4', res=quality).first()

        if video_stream:
            filesize = video_stream.filesize / (1024 * 1024)  # Convert bytes to MB
            filesize = round(filesize, 2)  # Round to two decimal places

            # Download the video
            video_stream.download(save_path)
            status = f"Download completed! (Size: {filesize} MB)"
        else:
            status = "Format not found."

    except Exception as e:
        status = "Download failed."
        print(e)

    return render_template('youtube_downloader.html', status=status)

@app.route('/blog')
def blog():
    return render_template('blog.html')

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
    form = RegisterForm(request.form, meta={'csrf': False})
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        middle_name = form.middle_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO register(first_name, middle_name, last_name,username, email, password) VALUES(%s, %s, %s, %s, %s, %s)", (first_name, middle_name, last_name,username, email, password))

        #commit to DB
        mysql.connection.commit()

        #close connection
        cur.close()

        flash('You are now registered and can log in', 'Success')

        return redirect(url_for('index'))

    return render_template('register.html', form=form)

if __name__=='__main__':
    app.run(debug=True) 
