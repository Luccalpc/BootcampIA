import datetime
import time
import cv2
import numpy as np
import sqlite3  
from tkinter import messagebox
from flask import Flask, render_template, Response, request, jsonify
import jwt
from functools import wraps


detector_face = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("classificadores/classificadorLBPH.yml")
width, height = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f748fb58f73d3d69a0e33225c10653ee81de9050a2b98c7c2c0389dec6cc03a7'
codigo: int = 0

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            #return jsonify({'message' : 'Token is missing !'}) 
            return render_template('index.html')
        try:
            token = jwt.decode(token, app.config['SECRET_KEY'],algorithms="HS256")  
        except:
            return  jsonify({'message' : 'Token is invalid'}) 
        return f(*args, **kwargs)
    return decorated
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
@token_required
def admin():
    return render_template('admin-dashboard.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/user')
@token_required
def user():
    return render_template('user-dashboard.html')

@app.route('/verify', methods = ['GET', 'POST'])
def verify():
    if request.method == 'POST':
        connection = sqlite3.connect('db/bootcamp.db')
        cursor = connection.cursor()

        email = request.form ['email']
        password = request.form ['password']

        print(email,password)

        query = "SELECT email,password,isAdmin, name FROM visitors where email= '"+email+"' and password = '"+password+"'"
        
        cursor.execute(query) 
        res = cursor.fetchone()[2]
        print(res)
        
        cursor.execute(query) 
        name = cursor.fetchone()[3]
        print(name)
        
        cursor.execute(query) 
        results = cursor.fetchall()
        print(results)
        
        if len(results) == 0:
            print ("Sorry, Wrong Password")             
        else:
            token = jwt.encode({'user': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes= 5)}, app.config['SECRET_KEY'], algorithm="HS256")
            print(token)     
            if res == 0:
                return render_template('user-dashboard.html', name = name)
            else:
                return render_template('admin-dashboard.html', name = name)
                
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
            
@app.route("/cadastro",methods = ["POST","GET"] )  
def my_form_post():
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]
            password = request.form["password"]
            cpf = request.form["cpf"]
            birthDate = request.form["birthDate"]
            visitDate = request.form["visitDate"]
            visitReason = request.form["visitReason"] 
            with sqlite3.connect("db/bootcamp.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into visitors (name,email,password,cpf,birthDate,visitDate,visitReason, isAdmin ) values (?,?,?,?,?,?,?, ?)",(name,email,password,cpf,birthDate,visitDate,visitReason, 0))  
                con.commit()  
                msg = "Employee successfully Added" 
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            con.close()  
    return render_template('cadastroCam.html')


@app.route('/cadastro-camera')
def cadastroCamera():
    return render_template('cadastroCam.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')



@app.route('/consulta')
def consulta():
    try:
        con = sqlite3.connect("db/ponto.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        cur.execute("select * from Ponto")  
        rows = cur.fetchall()  
        return render_template("consulta.html",rows = rows) 
        con.close()   
        exit(0)
    
    except:  
            con.rollback()  
            return render_template("fail.html")  
            con.close()  
            exit(0) 

@app.route('/crud')
def crud():
    return render_template('crud.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route("/listaFuncionarios")  
def view():  
    try:
        con = sqlite3.connect("db/funcionario.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        cur.execute("select * from Employees")  
        rows = cur.fetchall()  
        return render_template("listaFuncionarios.html",rows = rows) 
        con.close()   
        exit(0)
    
    except:  
            con.rollback()  
            return render_template("fail.html")  
            con.close()  
            exit(0) 
                 
    
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            rgfuncional = request.form["rgfuncional"]
            name = request.form["name"]  
            email = request.form["email"]  
            with sqlite3.connect("db/funcionario.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Employees (rgfuncional,name, email) values (?,?,?)",(rgfuncional,name,email))  
                con.commit()  
        except:  
            con.rollback()                
        finally:  
            return render_template("success.html")  
            con.close()  

@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("db/funcionario.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Employees where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html",msg = msg) 


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/regponto')
def regponto():
    return Response(work(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_capture')
def video_capture():
    return Response(capture(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



def work():
    cap = cv2.VideoCapture(0)
    time.sleep(2)
    i = 0
    findface = False
    while cap.isOpened():
        i+=1
        ret, img = cap.read()

        if findface and i<10:
            msg = 'Registro de Ponto Gravado com Sucesso !!'
            cv2.putText(img, msg, (100, 25), font, 1, (0, 255, 0))
            
        

        image_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detected_faces = detector_face.detectMultiScale(image_grey, scaleFactor=1.5, minSize=(30, 30))
        if ret:
            for (x, y, l, a) in detected_faces:
                image_face = cv2.resize(image_grey[y:y + a, x:x + l], (width, height))
                cv2.rectangle(img, (x, y), (x + l, y + a), (0, 0, 255), 2)
                class_id, confidence = recognizer.predict(image_face)
                if i >= 30 and class_id==1 and confidence <65:
                    findface = True
                    i=0
                    nome='Lucca'
                    try:  
                        rgfuncional = 1
                        name = 'Lucca' 
                        data = datetime.now() 
                        with sqlite3.connect("db/ponto.db") as con:  
                            cur = con.cursor()  
                            cur.execute("INSERT into Ponto (rgfuncional,name, data) values (?,?,?)",(rgfuncional,name,data))  
                            con.commit()   
                            #messagebox.showinfo('Ponto registrado com sucesso')              
                    except:  
                        con.rollback()             
                    finally:  
                        con.close()  
                elif i >= 30 and class_id==6 and confidence <65:
                    findface = True
                    i=0
                    nome = 'Mbappe'
                    try:  
                        rgfuncional = 5
                        name = 'Mbappe' 
                        data = datetime.now() 
                        with sqlite3.connect("db/ponto.db") as con:  
                            cur = con.cursor()  
                            cur.execute("INSERT into Ponto (rgfuncional,name, data) values (?,?,?)",(rgfuncional,name,data))  
                            con.commit() 
                            #messagebox.showinfo('Ponto registrado com sucesso')                
                    except:  
                        con.rollback()             
                    finally:  
                        con.close()
                        
                elif i >=30:
                    i=0
                    findface = True
                    nome = 'Desconhecido'
                    try:  
                        rgfuncional = -1
                        name = 'Desconhecido' 
                        data = datetime.now()   
                        with sqlite3.connect("db/ponto.db") as con:  
                            cur = con.cursor()  
                            cur.execute("INSERT into Ponto (rgfuncional,name, data) values (?,?,?)",(rgfuncional,name,data))  
                            con.commit()   
                            #messagebox.showinfo('Funcionário não encontrado')              
                    except:  
                        con.rollback()             
                    finally:  
                        con.close()
                #cv2.putText(img, str(i), (x, y + (a + 50)), font, 1, (0, 255, 255))
                #cv2.putText(img, nome, (x, y + (a + 30)), font, 2, (0, 255, 0))
                #cv2.putText(img, str(confidence), (x, y + (a + 50)), font, 1, (0, 255, 255))

            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            time.sleep(0.1)
        else:
            break

def capture():
    connection = sqlite3.connect('db/bootcamp.db')
    cursor = connection.cursor()
    queryBuscaId = 'SELECT id FROM visitors ORDER BY id DESC LIMIT 1'
    cursor.execute(queryBuscaId)
    idVisitante = cursor.fetchone()[0]
    print(idVisitante)
    cap = cv2.VideoCapture(0)

    larg, alt = 220, 220
    amostra: int = 1
    id = 1

    while cap.isOpened():
        ret, img = cap.read()
        image_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detected_faces = detector_face.detectMultiScale(image_grey, scaleFactor=1.5, minSize=(100, 100))
        if ret:
            for (x, y, l, a) in detected_faces:
                cv2.rectangle(img, (x, y), (x + l, y + a), (0, 0, 255), 2)
                global codigo

                if np.average(image_grey) > 70:
                    imagemface = cv2.resize(image_grey[y:y + a, x:x + l], (larg, alt))
                    cv2.imwrite("fotos/pessoa." + str(idVisitante) + "." + str(amostra) + ".jpg", imagemface) + amostra
                    print("Foto capturada com sucesso - " + str(amostra))
                    amostra += 1

                    if amostra > 50:
                        exit(0)

            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            time.sleep(0.15)
        else: 
            break           


def gen():
    cap = cv2.VideoCapture(0)
    i = 0
    while cap.isOpened():

        i+=1
        ret, img = cap.read()
        image_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detected_faces = detector_face.detectMultiScale(image_grey, scaleFactor=1.5, minSize=(30, 30))
        if ret:
            for (x, y, l, a) in detected_faces:
                image_face = cv2.resize(image_grey[y:y + a, x:x + l], (width, height))
                cv2.rectangle(img, (x, y), (x + l, y + a), (0, 0, 255), 2)
                class_id, confidence = recognizer.predict(image_face)
                if class_id == 1 and confidence < 65:
                    nome = "Acesso Permitido"
                else:
                    nome = "Acesso Negado"
                cv2.putText(img, nome, (x, y + (a + 30)), font, 2, (255, 180, 0))
                cv2.putText(img, str(confidence), (x, y + (a + 50)), font, 1, (0, 255, 255))
                

            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            time.sleep(0.1)
        else:
            break