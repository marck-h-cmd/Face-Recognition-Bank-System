import cv2
import dlib
import face_recognition
import numpy as np


detector = dlib.get_frontal_face_detector()

def detect_faces(frame):
  
    if frame is None or not isinstance(frame, np.ndarray):
        raise ValueError("El frame proporcionado es inválido o no es una matriz numpy.")

    try:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = detector(rgb_frame, 1)  
        return faces, rgb_frame
    except Exception as e:
        print(f"Error procesando el frame: {e}")
        return [], None

def register_face(rgb_frame, faces):
   
    if faces and rgb_frame is not None:
        try:
            face_encoding = face_recognition.face_encodings(rgb_frame, [(face.top(), face.right(), face.bottom(), face.left()) for face in faces])[0]
            return face_encoding
        except IndexError:
            print("No se pudo obtener la codificación del rostro.")
            return None
    print("No se detectaron rostros.")
    return None