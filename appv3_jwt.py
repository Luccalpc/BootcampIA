from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'topsecret'

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

@app.route('/unprotected')
def unprotected():
    return  jsonify({'message' : 'EVERYBODY CAN ACESS'}) 


@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'LOGGED PEOPLE CAN ACESS'}) 

@app.route('/')
def login():
   auth = request.authorization
   if auth and auth.password == 'senha':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow()+ datetime.timedelta(seconds = 30)}, app.config['SECRET_KEY'], algorithm="HS256")      
        return jsonify({'token' : token})
       
   return make_response('Could not verify !', 401, {'WWW-Authenticate': 'Basic realm=Login Required"'}) 

if __name__ == '__main__':
    app.run(debug=True)