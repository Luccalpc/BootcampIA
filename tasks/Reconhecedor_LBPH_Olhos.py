import cv2

#EigenFace

detectorFace = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
classificadorOlho = cv2.CascadeClassifier("haarcascade/haarcascade_eye.xml")

reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read("classificadores/classificadorLBPH.yml")

largura, altura = 220, 220

font = cv2.FONT_HERSHEY_COMPLEX_SMALL = 1

camera = cv2.VideoCapture(0)

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150,150))

    for (x,y,l,a) in facesDetectadas:

        cv2.rectangle(imagem,(x,y),(x+l,y+a),(0,0,255),2)
        regiao = imagem[y:y + a, x:x + l]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)

        for(ox, oy, ol, oa) in olhosDetectados:
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
            cv2.rectangle(regiao,(ox, oy),(ox+50,oy+50),(0,255,0),2) 
            id, confianca = reconhecedor.predict(imagemFace)
            nome = ''
            if(id==1):
                nome = "Renan Alcolea"
            else :
                nome = "Acesso Negado"
            cv2.putText(imagem, nome, (x, y+(a+30)), font, 2, (255,225,0))
            cv2.putText(imagem,str(confianca),(x,y+(a+65)),font,2,(0,255,255))
    cv2.imshow("Face", imagem)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()