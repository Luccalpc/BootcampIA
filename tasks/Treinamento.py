import cv2
import os
import numpy as np

#Treinamento 2 - De fato treinando e gerando os classificadores para o sistema

eigenface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

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

fisherface.train(faces, ids)
fisherface.write('classificadores/classificadorFisher.yml')

lbph.train(faces, ids)
lbph.write('classificadores/classificadorLBPH.yml')

print('TREINAMENTO REALIZADO COM SUCESSO')
