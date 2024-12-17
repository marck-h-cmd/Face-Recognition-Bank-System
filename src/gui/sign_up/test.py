import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import cv2
from datetime import datetime
from models.BAccount import BAccount
from functions.face_detection.face_detection_logic import detect_faces, register_face
from functions.utils import generate_baccount_code


class RegisterFaceUI:
    def _init_(self, master=None):
        self.master =  tk.Tk(master)
        self.master.title("Eureka Bank - Registro de Rostro")
        self.master.configure(background="#ffffff", height=800, width=1200)

        # Title Section
        self.bgTitle = tk.Canvas(self.master, background="#f1f18d", height=120, width=1200)
        self.bgTitle.place(anchor="nw", x=0, y=100)

        self.lblTitle = ttk.Label(self.master, background="#f1f18d", font="{NSimSun} 36 {bold}", text='EUREKA BANK')
        self.lblTitle.place(anchor="nw", x=420, y=130)

        # User Entry
        self.lblInformacion = ttk.Label(self.master, background="#ffffff", font="{NSimSun} 20 {}", text='Información de Cuenta')
        self.lblInformacion.place(anchor="nw", x=420, y=250)

        self.entryUser = ttk.Entry(self.master, font="{NSimSun} 12 {}")
        self.entryUser.insert("0", "Usuario")
        self.entryUser.place(anchor="nw", width=300, x=250, y=400)

        self.entryPassword = ttk.Entry(self.master, show="*", font="{NSimSun} 12 {}")
        self.entryPassword.insert("0", "Contraseña")
        self.entryPassword.place(anchor="nw", width=300, x=250, y=480)

        # Video Frame
        self.video_frame = tk.Canvas(self.master, width=400, height=300, background="#a0a0a0")
        self.video_frame.place(anchor="nw", x=685, y=320)

        # Label for Face Registration Status
        self.lblFaceStatus = ttk.Label(self.master, text="Estado del rostro: No registrado", font="{NSimSun} 14 {}", background="#ffffff", foreground="red")
        self.lblFaceStatus.place(anchor="nw", x=685, y=630)

        # Buttons
        self.btnRegisterFace = ttk.Button(self.master, text='Registrar Rostro', command=self.capture_face)
        self.btnRegisterFace.place(anchor="nw", width=300, x=650, y=580)

        self.btnRegister = ttk.Button(self.master, text='Crear Cuenta', command=self.register)
        self.btnRegister.place(anchor="nw", width=300, x=250, y=580)

        # Variables
        #self.customer = customer
        self.video_capture = cv2.VideoCapture(0)
        self.video_running = True
        self.face_encoding = None
        self.image_refs = []  # Lista para referencias de imágenes

        if not self.video_capture.isOpened():
            messagebox.showerror("Error", "No se pudo abrir la cámara.")
            self.video_running = False
        else:
            self.update_video()

    def update_video(self):
        """Actualiza el video en el Canvas."""
        if self.video_running:
            ret, frame = self.video_capture.read()
            if ret:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.display_frame(rgb_frame)
            self.master.after(10, self.update_video)

    def display_frame(self, frame):
        """Muestra el cuadro capturado en el Canvas."""
        try:
            img = tk.PhotoImage(data=cv2.imencode(".png", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))[1].tobytes())
            self.image_refs.append(img)  # Guardar referencia
            if len(self.image_refs) > 10:  # Limitar tamaño de la lista
                self.image_refs.pop(0)
            self.video_frame.create_image(0, 0, anchor="nw", image=img)
        except Exception as e:
            print(f"Error mostrando el cuadro: {e}")

    def capture_face(self):
        """Captura el rostro del usuario."""
        ret, frame = self.video_capture.read()
        if not ret:
            messagebox.showerror("Error", "No se pudo capturar el cuadro.")
            return

        faces, rgb_frame = detect_faces(frame)
        if faces:
            self.face_encoding = register_face(rgb_frame, faces)
            if self.face_encoding is not None:
                self.lblFaceStatus.configure(text="Estado del rostro: Registrado correctamente", foreground="green")
                messagebox.showinfo("Éxito", "Codificación facial registrada correctamente.")
            else:
                self.lblFaceStatus.configure(text="Estado del rostro: Error al registrar", foreground="red")
                messagebox.showwarning("Advertencia", "No se pudo registrar la codificación del rostro.")
        else:
            self.lblFaceStatus.configure(text="Estado del rostro: No detectado", foreground="red")
            messagebox.showinfo("Información", "No se detectaron rostros.")

    def register(self):
        """Crea una cuenta."""
        username = self.entryUser.get()
        acc_pass = self.entryPassword.get()

        if not username or not acc_pass or self.face_encoding is None:
            messagebox.showerror("Error", "Faltan campos obligatorios o no se ha registrado el rostro.")
            return

        acctcode = generate_baccount_code()
        clcode =  "CL-DEFAULT"
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        amount = 0.0
        state = "ACTIVE"

        face_id = self.face_encoding.tolist()
        result = BAccount.insert(
            acctcode=acctcode,
            face_id=face_id,
            clcode=clcode,
            created_at=created_at,
            amount=amount,
            state=state,
            mov_cont=0,
            acc_pass=acc_pass
        )

        if result:
            messagebox.showinfo("Éxito", "Cuenta registrada exitosamente.")
        else:
            messagebox.showerror("Error", "No se pudo registrar la cuenta.")

    def close(self):
        """Cierra la aplicación y libera recursos."""
        self.video_running = False
        self.video_capture.release()
        self.master.destroy()

    def run(self):
        """Inicia la interfaz de usuario."""
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        self.master.mainloop()


if __name__ == "__main__":
    app = RegisterFaceUI()
    app.run()
