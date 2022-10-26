from flask import Flask,jsonify, render_template,request, make_response
import sqlite3

app = Flask(__name__)

if __name__ == 'main':
    app.run(debug=True)

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


@app.route('unprotected')
def unprotected():
    return

@app.route('protected')
def protected():
    return