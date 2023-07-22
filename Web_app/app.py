from flask import Flask
from flask_mysqldb import MySQL
from forms import RegisterForm
from calculator import calculator_app
from youtube_downloader import youtube_downloader_app
from blog import blog_app
from portfolio import portfolio_app

app = Flask(__name__)
app.secret_key = 'Ifedaniel@0704&6561'

# configure MySQL
app.config['MYSQL_HOST'] = 'aws.connect.psdb.cloud'
app.config['MYSQL_USER'] = 'e32m5rf7dwc2ekmhtp9x'
app.config['MYSQL_PASSWORD'] = 'pscale_pw_XXMMmJKrIbjSYlcNOeDXXweaGXLTy4zXVzUtTFtgz9S'
app.config['MYSQL_DB'] = 'didnow'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MySQL
mysql = MySQL(app)

app.register_blueprint(calculator_app)
app.register_blueprint(blog_app)
app.register_blueprint(portfolio_app)
app.register_blueprint(register_app)

# ... Add the remaining route registrations here ...

#this is for the registration page, here the form validation and length is structured
class RegisterForm(Form):
     first_name = StringField('First Name', [validators.Length(min=1, max=50)])
     middle_name = StringField('Middle Name', [validators.Length(min=1, max=50)])
     last_name = StringField('Last Name', [validators.Length(min=1, max=50)])
     username = StringField('Username', [validators.Length(min=4, max=25)])
     email = StringField('Email', [validators.Length(min=5, max=25)])
     password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords do not match')])
     confirm = PasswordField('Confirm Password')

     pass

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
