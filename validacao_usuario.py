import datetime
from flask import Flask,render_template,request, jsonify
import sqlite3
import jwt
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f748fb58f73d3d69a0e33225c10653ee81de9050a2b98c7c2c0389dec6cc03a7'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message' : 'Token is missing !'}) 
        try:
            token = jwt.decode(token, app.config['SECRET_KEY'],algorithms="HS256")  
        except:
            return  jsonify({'message' : 'Token is invalid'}) 
        return f(*args, **kwargs)
    return decorated

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        connection = sqlite3.connect('db/Bancotest.db')
        cursor = connection.cursor()

        email = request.form ['email']
        password = request.form ['password']

        query = "SELECT email,password FROM visitors where email= '"+email+"' and password = '"+password+"'"
        cursor.execute(query) 

        results = cursor.fetchall()

        if len(results) == 0:
            print ("Sorry, Wrong Password")             
        else:
            token = jwt.encode({'user': email, 'exp': datetime.datetime.utcnow()+ datetime.timedelta(minutes= 5)}, app.config['SECRET_KEY'], algorithm="HS256")     
            return token
            #return render_template('logged.html')
        
       

    return render_template('login.html')