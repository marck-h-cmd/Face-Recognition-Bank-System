import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import cv2
from datetime import datetime
from models.BAccount import BAccount
from functions.face_detection.face_detection_logic import detect_faces, register_face
from functions.utils import generate_baccount_code

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

        # Password entry
        self.entryPassword = ttk.Entry(self.master, name="entrypassword", show="*")
        self.entryPassword.configure(font="{NSimSun} 12 {}")
        self.entryPassword.insert("0", "Contraseña")
        self.entryPassword.place(anchor="nw", width=300, x=250, y=480)

        # Register face button
        self.btnRegisterFace = ttk.Button(self.master, name="btnregisterface", command=self.capture_face)
        self.btnRegisterFace.configure(text='Registrar Rostro')
        self.btnRegisterFace.place(anchor="nw", width=300, x=650, y=580)

        # Video frame for camera (replacing the static canvas)
        self.video_frame = tk.Canvas(self.master, width=400, height=300, background="#a0a0a0")
        self.video_frame.place(anchor="nw", x=685, y=320)

        # Register account button
        self.btnRegister = ttk.Button(self.master, name="btnregister", command=self.register)
        self.btnRegister.configure(text='Crear Cuenta')
        self.btnRegister.place(anchor="nw", width=300, x=250, y=580)

        self.customer = customer
        self.video_capture = cv2.VideoCapture(0)
        self.video_running = False
        self.face_encoding = None
        self.current_image = None

        if not self.video_capture.isOpened():
            print("Error: Unable to open camera.")
            self.video_running = False
        else:
            self.start_video()

    def start_video(self):
        self.video_running = True
        self.update_video()

    def update_video(self):
        if self.video_running:
            ret, frame = self.video_capture.read()
            if ret:
                try:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = Image.fromarray(frame)
                    imgtk = ImageTk.PhotoImage(image=img)

                    self.video_frame.delete("all") 
                    self.video_frame.create_image(0, 0, anchor="nw", image=imgtk)
                    self.video_frame.image = imgtk  
                except Exception as e:
                    print(f"Error al procesar el video: {e}")
            else:
                print("No se pudo leer el cuadro del video.")

            self.master.after(10, self.update_video)

    def capture_face(self):
        ret, frame = self.video_capture.read()
        if not ret:
            messagebox.showerror("Error", "No se pudo capturar el cuadro. Verifica la cámara.")
            return

        try:
            faces, rgb_frame = detect_faces(frame)
            if faces:
                self.face_encoding = register_face(rgb_frame, faces)
                if self.face_encoding is not None:
                    messagebox.showinfo("Éxito", "Codificación facial registrada correctamente.")
                else:
                    messagebox.showwarning("Advertencia", "Rostro detectado, pero no se pudo registrar la codificación.")
            else:
                messagebox.showinfo("Información", "No se detectaron rostros. Intenta nuevamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error procesando la captura facial: {e}")

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
