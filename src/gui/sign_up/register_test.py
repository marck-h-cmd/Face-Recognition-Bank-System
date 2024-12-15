import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from datetime import datetime
from functions.face_detection.face_detection_logic import detect_faces, register_face
from models.BAccount import BAccount
from functions.utils import generate_baccount_code

class RegisterFaceUI:
    def __init__(self, customer=None, master=None):
        # Build UI
        self.master = tk.Tk(master)
        self.master.configure(background="#ffffff", height=800, width=1200)

        self.video_frame = tk.Canvas(self.master, name="video_frame", background="#cccccc")
        self.video_frame.place(anchor="nw", height=400, width=600, x=300, y=100)

        self.entryUser = ttk.Entry(self.master, name="entryUser", font="{NSimSun} 12 {}")
        self.entryUser.place(anchor="nw", width=300, x=250, y=550)
        self.entryPassword = ttk.Entry(self.master, name="entryPassword", font="{NSimSun} 12 {}", show="*")
        self.entryPassword.place(anchor="nw", width=300, x=250, y=600)

        self.btnRegisterFace = ttk.Button(self.master, text='Registrar Rostro', command=self.start_video)
        self.btnRegisterFace.place(anchor="nw", width=300, x=650, y=550)

        self.btnRegister = ttk.Button(self.master, text='Crear Cuenta', command=self.register)
        self.btnRegister.place(anchor="nw", width=300, x=650, y=600)

        self.video_running = False
        self.face_encoding = None
        self.customer = customer
        self.video_capture = cv2.VideoCapture(0)

    def run(self):
        self.master.mainloop()

    def start_video(self):
        if not self.video_running:
            self.video_running = True
            self.update_video()

    def update_video(self):
        if self.video_running:
            ret, frame = self.video_capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_frame.create_image(0, 0, anchor="nw", image=imgtk)
                self.video_frame.imgtk = imgtk
            self.master.after(10, self.update_video)

    def capture_face(self):
        ret, frame = self.video_capture.read()
        if not ret:
            print("Error capturing frame.")
            return

        faces, rgb_frame = detect_faces(frame)
        if faces:
            self.face_encoding = register_face(rgb_frame, faces)
            if self.face_encoding is not None:
                print("Face encoding captured successfully.")
            else:
                print("Face detected, but encoding failed.")
        else:
            print("No face detected. Please try again.")

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
        self.video_capture.release()
        cv2.destroyAllWindows()
        self.master.destroy()


if __name__ == "__main__":
    app = RegisterFaceUI()
    try:
        app.run()
    except KeyboardInterrupt:
        app.close()
