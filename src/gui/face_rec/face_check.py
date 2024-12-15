import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import functions.face_detection as fr
import functions.utils as ut
from models.BAccount import BAccount 
import datetime

class FaceRecognitionApp:
    def __init__(self, master,BAccount):
        self.master = master
        self.master.title("Face Recognition Scanner")

        # UI Elements
        self.canva_video = tk.Canvas(master, width=650, height=500, bg="#ffffbf")
        self.canva_video.pack()

        self.footer = tk.Canvas(master, bg="#fddb66", height=180)
        self.footer.pack(fill="both", side="bottom")

        self.lbl_text = ttk.Label(self.footer, text='Verifique su identidad', background="#fddb66")
        self.lbl_text.pack(anchor="center", pady=5)

        self.btn_check = ttk.Button(self.footer, text='Check', command=self.verify_face)
        self.btn_check.pack(anchor="center", pady=10)

      
        self.cap = cv2.VideoCapture(0)
        self.registered_encoding = None
        self.video_running = True

      
        self.update_frame()

    def update_frame(self):
       
        ret, frame = self.cap.read()
        if ret:
          
            faces, rgb_frame = fr.detect_faces(frame)

            for face in faces:
                x, y, w, h = face.left(), face.top(), face.width(), face.height()
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            photo = ImageTk.PhotoImage(image)
            self.canva_video.create_image(0, 0, anchor=tk.NW, image=photo)
            self.master.photo = photo 

        if self.video_running:
            self.master.after(10, self.update_frame)

    def capture_face(self):
        """
        Captures the face and registers it.
        """
        ret, frame = self.cap.read()
        if ret:
            faces, rgb_frame = fr.detect_faces(frame)
            encoding = fr.register_face(rgb_frame, faces)
            if encoding is not None:
                self.registered_encoding = encoding
                print("Face Registered!")

             
                BAccount.insert(
                    acctcode=ut.generate_baccount_code(),
                    face_id=encoding.tolist(),  
                    clcode="CL001",
                    created_at=datetime.time,
                    amount=0.0,
                    state="active",
                    mov_cont=0,
                    acc_pass="securepassword123"
                )
            else:
                print("No face detected. Please try again.")

    def verify_face(self):
        
        if self.registered_encoding is None:
            print("No registered face. Please register a face first.")
            return

        ret, frame = self.cap.read()
        if ret:
            faces, rgb_frame = fr.detect_faces(frame)
            match = fr.verify_face(self.registered_encoding, rgb_frame, faces)
            if match:
                print("Face verified successfully!")
            else:
                print("Face verification failed.")

    def quit_app(self):
       
        self.video_running = False
        self.cap.release()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
