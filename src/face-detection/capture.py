import face_recognition
import cv2
import numpy as np
from pymongo import MongoClient

    #pa guardar el rostro en la DB
def registrar_rostro(usuario_id):
    # Capturar imagen con la cámara
    webcam = cv2.VideoCapture(0)
    ret, frame = webcam.read()
    
    # Convertir la imagen a RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detectar rostros en la imagen
    face_locations = face_recognition.face_locations(rgb_frame)                  #coniverte la imagen a t,b,r y l pxles
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)  #codifica el rostro unico
    
    # Si se detecta un rostro
    if face_encodings:
        # Guardamos el primer rostro checkeado
        rostro_encoding = face_encodings[0]
        
        # Almacenamos el rostro en MongoDB    (SUPOSICIÓN DE GUARDADO)
        usuarios.insert_one({'usuario_id': usuario_id, 'rostro_encoding': rostro_encoding.tolist()})
        return True
    else:
        return False

    webcam.release()
    
    
    #pa luego verificarlo en cada transacción
def verificar_rostro(usuario_id):
    # Capturar imagen con la cámara
    webcam = cv2.VideoCapture(0)
    ret, frame = webcam.read()
    
    # Convertir la imagen a RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detectar rostros en la imagen
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    if face_encodings:
        # Cargar el rostro registrado de la base de datos
        usuario = usuarios.find_one({'usuario_id': usuario_id})
        
        if usuario:
            # Convertimos la lista a un array numpy para compararlo con face_recognition
            registrado_encoding = np.array(usuario['rostro_encoding'])
            
            # Comparamos los rostros
            result = face_recognition.compare_faces([registrado_encoding], face_encodings[0])
            if result[0]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    webcam.release()
