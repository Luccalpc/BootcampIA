import cv2

#Captura Face

classificador = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)
amostra = 1
numeroAmostras = 15
id = input('Digite seu id: ')
largura, altura = 220, 220
print("Capturando as faces...")

while(True):

    conectado, imagem = camera.read()

    # No caso para o processamento é indicado processar em uma escala de cinza para melhor precisão e desempenho      
    
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)      
    facesDetectadas = classificador.detectMultiScale(imagemCinza,scaleFactor=1.5,minSize=(150,150))

    for (x,y,l,a) in facesDetectadas:        
        cv2.rectangle(imagem,(x,y),(x+l,y+a),(0,0,255),2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
            cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
            print("[foto " + str(amostra) + " capturada com sucesso]")
            amostra+=1


    cv2.imshow("Face", imagem)
    cv2.waitKey(1)
    if(amostra >= numeroAmostras + 1):
        break

camera.release()
cv2.destroyAllWindows()