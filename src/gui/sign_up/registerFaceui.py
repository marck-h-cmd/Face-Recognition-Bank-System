#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from models.BAccount import BAccount

class RegisterFaceUI:
    def __init__(self, customer,master=None):
        # build ui
        tk1 = tk.Tk(master)
        tk1.configure(background="#ffffff", height=800, width=1200)
        self.bgTitle = tk.Canvas(tk1, name="bgtitle")
        self.bgTitle.configure(background="#f1f18d")
        self.bgTitle.place(anchor="nw", height=120, width=1200, x=0, y=100)
        self.lblTitle = ttk.Label(tk1, name="lbltitle")
        self.lblTitle.configure(
            background="#f1f18d",
            font="{NSimSun} 36 {bold}",
            text='EUREKA BANK')
        self.lblTitle.place(anchor="nw", relx=0.0, rely=0.0, x=420, y=130)
        self.lblInformacion = ttk.Label(tk1, name="lblinformacion")
        self.lblInformacion.configure(
            background="#ffffff",
            font="{NSimSun} 20 {}",
            text='Información de Cuenta')
        self.lblInformacion.place(anchor="nw", x=420, y=250)
        separator1 = ttk.Separator(tk1)
        separator1.configure(orient="horizontal")
        separator1.place(anchor="nw", width=800, x=200, y=300)
        self.entryUser = ttk.Entry(tk1, name="entryuser")
        self.entryUser.configure(font="{NSimSun} 12 {}")
        _text_ = 'Usuario'
        self.entryUser.delete("0", "end")
        self.entryUser.insert("0", _text_)
        self.entryUser.place(anchor="nw", width=300, x=250, y=400)
        self.entryPassword = ttk.Entry(tk1, name="entrypassword")
        self.entryPassword.configure(font="{NSimSun} 12 {}")
        _text_ = 'Contraseña'
        self.entryPassword.delete("0", "end")
        self.entryPassword.insert("0", _text_)
        self.entryPassword.place(anchor="nw", width=300, x=250, y=480)
        self.btnRegisterFace = ttk.Button(tk1, name="btnregisterface", command=self.register_face)
        self.btnRegisterFace.configure(text='Registrar Rostro')
        self.btnRegisterFace.place(anchor="nw", width=300, x=650, y=580)
        self.lblImagerUser = ttk.Label(tk1, name="lblimageruser")
        self.img_user = tk.PhotoImage(file="src/img/user.png")
        self.lblImagerUser.configure(background="#a0a0a0", image=self.img_user)
        self.lblImagerUser.place(anchor="nw", x=685, y=320)
        separator2 = ttk.Separator(tk1)
        separator2.configure(orient="horizontal", takefocus=True)
        separator2.place(anchor="nw", height=400, x=600, y=300)
        self.btnRegister = ttk.Button(tk1, name="btnregister", command=self.register)
        self.btnRegister.configure(text='Crear Cuenta')
        self.btnRegister.place(anchor="nw", width=300, x=250, y=580)

        #customer object
        #params clcode, name, lastname, city, dni, phone, email
        self.customer=customer
        # Main widget
        self.mainwindow = tk1

    def run(self):
        self.mainwindow.mainloop()

    def register_face(self):
        
        pass
    
    def register():
        
        pass
        
        

if __name__ == "__main__":
    app = RegisterFaceUI()
    app.run()
