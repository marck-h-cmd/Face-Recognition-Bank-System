import face_recognition
import cv2
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import numpy as np
from bson import ObjectId
from models.BAccount import BAccount
# Asegúrate de importar la función BAccount desde el archivo donde tienes la conexión con MongoDB.
# from your_mongo_module import BAccount

class FaceRecognitionRegistrationApp:
    def __init__(self, root=None):
        self.root = root
        self.root.title("Registro de Usuario con Reconocimiento Facial")
        self.root.geometry("400x300")

        # Inicializar las variables
        self.face_encoding = None

        # Crear campos de entrada
        self.username_label = tk.Label(root, text="Nombre de Usuario")
        self.username_label.pack(pady=5)

        self.entry_user = tk.Entry(root)
        self.entry_user.pack(pady=5)

        self.password_label = tk.Label(root, text="Contraseña")
        self.password_label.pack(pady=5)

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        # Botón para capturar la cara
        self.capture_button = tk.Button(root, text="Capturar Cara", command=self.capture_face_encoding)
        self.capture_button.pack(pady=10)

        # Botón para registrar
        self.register_button = tk.Button(root, text="Registrar", command=self.register)
        self.register_button.pack(pady=10)

    def capture_face_encoding(self):
        # Usando OpenCV para capturar la cara desde la cámara
        cap = cv2.VideoCapture(0)  # Abre la cámara
        while True:
            ret, frame = cap.read()
            if not ret:
                messagebox.showerror("Error", "No se puede acceder a la cámara.")
                break

            # Detectar caras en el frame
            face_locations = face_recognition.face_locations(frame)
            if face_locations:
                face_encodings = face_recognition.face_encodings(frame, face_locations)
                if face_encodings:
                    self.face_encoding = face_encodings[0]
                    # Mostrar la cara en la ventana
                    cv2.rectangle(frame, (face_locations[0][3], face_locations[0][0]),
                                  (face_locations[0][1], face_locations[0][2]), (0, 255, 0), 2)
                    cv2.putText(frame, "Presione 'q' para guardar", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Captura facial", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def register(self):
        username = self.entry_user.get()
        acc_pass = self.entry_password.get()

        if not username or not acc_pass or self.face_encoding is None:
            messagebox.showerror("Error", "Faltan campos requeridos o codificación facial no capturada.")
            return

        # Generación de código de cuenta (simulado)
        acctcode = self.generate_account_code()
        clcode = "CL-DEFAULT"  # Puede ser modificado según se necesite
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        amount = 0.0
        state = "ACTIVE"
        mov_cont = 0

        # Convertir la codificación facial a lista para almacenamiento en MongoDB
        face_id = self.face_encoding.tolist()

        # Llamar a la función BAccount.insert() para registrar la cuenta
        result = BAccount.insert(
            acctcode=acctcode,
            face_id=face_id,
            clcode=clcode,
            created_at=created_at,
            amount=amount,
            state=state,
            mov_cont=mov_cont,
            acc_pass=acc_pass
        )

        if result:
            messagebox.showinfo("Éxito", "Cuenta registrada exitosamente.")
        else:
            messagebox.showerror("Error", "No se pudo registrar la cuenta.")

    def generate_account_code(self):
        # Generación de código de cuenta (simulación)
        return "ACCT-" + str(np.random.randint(1000, 9999))

# Iniciar la aplicación Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionRegistrationApp(root)
    root.mainloop()
