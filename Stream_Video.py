import datetime
from datetime import datetime
import time
import cv2
import numpy as np
import sqlite3  
from tkinter import messagebox
from flask import Flask, render_template, Response, request


detector_face = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("classificadores/classificadorLBPH.yml")
width, height = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

app = Flask(__name__)
codigo: int = 0
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')




@app.route("/cadastro",methods = ["POST","GET"] )  
def my_form_post():
    msg = "msg"  
    if request.method == "POST":  
        try:  
            nome = request.form["nome"]  
            email = request.form["email"]
            senha = request.form["senha"]
            cpf = request.form["cpf"]
            dataNascimento = request.form["dataNascimento"]
            dataVisita = request.form["dataVisita"]
            motivoVisita = request.form["motivoVisita"] 
            with sqlite3.connect("db/visitante.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Employees (nome, email, ) values (?,?,?)",(nome,email,senha,cpf,dataNascimento,dataVisita,motivoVisita))  
                con.commit()  
                msg = "Employee successfully Added" 
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            con.close()  
    return render_template('cadastro.html')


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
                    cv2.imwrite("fotos/pessoa." + str(codigo) + "." + str(amostra) + ".jpg", imagemface) + amostra
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