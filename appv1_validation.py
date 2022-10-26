from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        connection = sqlite3.connect('db/Bancotest.db')
        cursor = connection.cursor()

        name = request.form ['name']
        password = request.form ['password']

        print(name,password)

        query = "SELECT name,password FROM users where name= '"+name+"' and password = '"+password+"'"
        cursor.execute(query) 

        results = cursor.fetchall()

        if len(results) == 0:
            print ("Sorry, Wrong Password")             
        else:
            return render_template('logged.html')

    return render_template('login.html')