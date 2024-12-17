import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import cv2
from datetime import datetime
from models.BAccount import BAccount
from functions.utils import generate_baccount_code
import face_recognition
import dlib
import numpy as np

class RegisterFaceUI:
    def __init__(self, customer, master=None):
        self.master = master or tk.Tk()
        self.master.title("Eureka Bank - Registro de Rostro")
        self.master.configure(background="#ffffff", height=800, width=1200)

        # Canvas for title
        self.bgTitle = tk.Canvas(self.master, name="bgtitle")
        self.bgTitle.configure(background="#f1f18d")
        self.bgTitle.place(anchor="nw", height=120, width=1200, x=0, y=100)

        # Title label
        self.lblTitle = ttk.Label(self.master, name="lbltitle")
        self.lblTitle.configure(
            background="#f1f18d",
            font="{NSimSun} 36 {bold}",
            text='EUREKA BANK')
        self.lblTitle.place(anchor="nw", relx=0.0, rely=0.0, x=420, y=130)

        self.lblInformacion = ttk.Label(self.master, name="lblinformacion")
        self.lblInformacion.configure(
            background="#ffffff",
            font="{NSimSun} 20 {}",
            text='Información de Cuenta')
        self.lblInformacion.place(anchor="nw", x=420, y=250)

        self.entryUser = ttk.Entry(self.master, name="entryuser")
        self.entryUser.configure(font="{NSimSun} 12 {}")
        self.entryUser.insert("0", "Usuario")
        self.entryUser.place(anchor="nw", width=300, x=250, y=400)

        self.entryPassword = ttk.Entry(self.master, name="entrypassword", show="*")
        self.entryPassword.configure(font="{NSimSun} 12 {}")
        self.entryPassword.insert("0", "Contraseña")
        self.entryPassword.place(anchor="nw", width=300, x=250, y=480)

        self.btnRegisterFace = ttk.Button(self.master, name="btnregisterface", command=self.capture_face)
        self.btnRegisterFace.configure(text='Registrar Rostro')
        self.btnRegisterFace.place(anchor="nw", width=300, x=650, y=580)

        self.btnRegister = ttk.Button(self.master, name="btnregister", command=self.register)
        self.btnRegister.configure(text='Crear Cuenta')
        self.btnRegister.place(anchor="nw", width=300, x=250, y=580)

        self.customer = customer
        self.video_capture = cv2.VideoCapture(0)
        self.video_running = True
        self.face_encoding = None

        self.detector = dlib.get_frontal_face_detector()

        # Crear una ventana de OpenCV para mostrar el video
        cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)

        self.start_video()

    def start_video(self):
        self.update_video()

    def update_video(self):
        if self.video_running:
            ret, frame = self.video_capture.read()
            if ret:
                # Verificar que el frame no sea None
                if frame is not None:
                    # Convertir el frame a tipo uint8 (8 bits por canal)
                    frame = np.asarray(frame, dtype=np.uint8)

                    # Detecta las caras en el frame
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    faces = self.detector(rgb_frame, 1)

                    # Muestra el video en la ventana de OpenCV
                    self.show_video_on_opencv_window(frame)

                else:
                    print("Error: El frame no es válido.")
            
            # Establece un pequeño retraso para la siguiente actualización del video
            self.master.after(10, self.update_video)

    def show_video_on_opencv_window(self, frame):
        """ Muestra el video en una ventana independiente de OpenCV """
        # Verifica que el frame sea del tipo correcto (8 bits, 3 canales, uint8)
        if isinstance(frame, np.ndarray) and frame.dtype == np.uint8:
            # Convierte el frame a BGR antes de mostrarlo en OpenCV
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            cv2.imshow("Camera", frame_bgr)
        else:
            print("Error: El frame tiene un formato no compatible.")

    def capture_face(self):
        ret, frame = self.video_capture.read()
        if not ret:
            messagebox.showerror("Error", "No se pudo capturar el cuadro. Verifica la cámara.")
            return

        # Convertir el frame a uint8
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = self.detector(rgb_frame, 1)

        if faces:
            face_encoding = face_recognition.face_encodings(rgb_frame, [(f.top(), f.right(), f.bottom(), f.left()) for f in faces])[0]
            self.face_encoding = face_encoding
            messagebox.showinfo("Éxito", "Codificación facial registrada correctamente.")
        else:
            messagebox.showinfo("Información", "No se detectaron rostros. Intenta nuevamente.")

    def register(self):
        username = self.entryUser.get()
        acc_pass = self.entryPassword.get()

        if not username or not acc_pass or self.face_encoding is None:
            print("Error: Missing required fields or face encoding.")
            return

        acctcode = generate_baccount_code()
        clcode = self.customer.clcode if self.customer else "CL-DEFAULT"
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        amount = 0.0
        state = "ACTIVE"
        mov_cont = 0

        face_id = self.face_encoding.tolist()
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
            print("Account registered successfully.")
        else:
            print("Error: Could not register the account.")

    def close(self):
        self.video_running = False
        if self.video_capture.isOpened():
            self.video_capture.release()
        cv2.destroyAllWindows()
        self.master.destroy()

    def run(self):
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        self.master.mainloop()


if __name__ == "__main__":
    app = RegisterFaceUI(customer=None)
    app.run()
