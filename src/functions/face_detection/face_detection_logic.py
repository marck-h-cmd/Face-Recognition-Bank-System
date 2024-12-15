import cv2
import dlib
import face_recognition
import numpy as np


detector = dlib.get_frontal_face_detector()

def detect_faces(frame):
  
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = detector(rgb_frame, 1)
    return faces, rgb_frame

def register_face(rgb_frame, faces):
    if faces:
        face_encoding = face_recognition.face_encodings(rgb_frame, faces)[0]
        return face_encoding
    return None

def verify_face(registered_encoding, rgb_frame, faces):
    if faces:
        face_encoding = face_recognition.face_encodings(rgb_frame, faces)[0]
        matches = face_recognition.compare_faces([registered_encoding], face_encoding)
        return matches[0]
    return False
