from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

class RegisterForm(Form):
    name = StringField('name', [validators.Length(min=1, max=50)])
    email = StringField('email', [validators.Length(min=6, max=50)])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
    cpf = StringField('cpf', [validators.Length(min=11, max=20)])
    birthDate = StringField('birthDate')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')
    return render_template('register.html', form=form)





if __name__ == '__main__':
    app.run(debug=True)
    