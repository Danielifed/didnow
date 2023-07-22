from wtforms import Form, StringField, PasswordField, validators
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

    pass
