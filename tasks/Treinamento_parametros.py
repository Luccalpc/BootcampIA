import cv2
import os
import numpy as np

#Treinamento 3 - Treinamento com Parametros

eigenface = cv2.face.EigenFaceRecognizer_create(num_components = 50)
lbph = cv2.face.LBPHFaceRecognizer_create(7,1,10,1,3)

def getImagemComId():
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    #print(caminhos)
    faces = []
    ids = []

    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)     
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1]) 
        ids.append(id)
        faces.append(imagemFace)
    return np.array(ids), faces

ids, faces = getImagemComId()

print('Treinando...')

# TREINAMENTO
eigenface.train(faces, ids)
eigenface.write('classificadores/classificadorEigen.yml')

lbph.train(faces, ids)
lbph.write('classificadores/classificadorLBPH.yml')

print('TREINAMENTO REALIZADO COM SUCESSO')
