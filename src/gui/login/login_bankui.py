import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

from functions.utils import *
from models.BAccount import BAccount

class Login_bankUI:
    def __init__(self, master=None):
        # Set fixed geometry for the main window
       
        
        

        # Build UI
        frame1 = ttk.Frame(master)
        frame1.configure(height=800, relief="sunken", width=1200)
        self.bgPrincipal = tk.Canvas(frame1, name="bgprincipal")
        self.bgPrincipal.configure(background="#ffffff")
        self.bgPrincipal.place(anchor="nw", height=800, width=1200, y=0)
        self.bgTitle = tk.Canvas(frame1, name="bgtitle")
        self.bgTitle.configure(
            background="#ece693",
            confine=False,
            cursor="arrow")
        self.bgTitle.place(anchor="nw", height=80, width=1200, y=120)
        self.lblLogin = ttk.Label(frame1, name="lbllogin")
        self.lblLogin.configure(
            background="#ffffff",
            font="{NSimSun} 20 {bold}",
            justify="center",
            text='Iniciar Sesion')
        self.lblLogin.place(anchor="nw", relx=0.0, x=470, y=250)
        self.entryUser = ttk.Entry(frame1, name="entryuser")
        self.entryUser.configure(font="{NSimSun} 12 {}")
        _text_ = 'Usuario'
        self.entryUser.delete("0", "end")
        self.entryUser.insert("0", _text_)
        self.entryUser.place(anchor="nw", width=300, x=450, y=360)
        separator7 = ttk.Separator(frame1)
        separator7.configure(orient="horizontal", takefocus=True)
        separator7.place(anchor="nw", width=800, x=200, y=320)
        separator8 = ttk.Separator(frame1)
        separator8.configure(orient="horizontal")
        separator8.place(anchor="nw", width=800, x=200, y=550)
        self.entryPassword = ttk.Entry(frame1, name="entrypassword")
        self.entryPassword.configure(font="{NSimSun} 12 {}")
        _text_ = 'Contraseña'
        self.entryPassword.delete("0", "end")
        self.entryPassword.insert("0", _text_)
        self.entryPassword.place(anchor="nw", width=300, x=450, y=420)
        self.btnLogin = ttk.Button(frame1, name="btnlogin", command=self.login_action)
        self.btnLogin.configure(
            default="active",
            state="normal",
            text='Iniciar Sesion')
        self.btnLogin.place(anchor="nw", width=300, x=450, y=480)
        separator9 = ttk.Separator(frame1)
        separator9.configure(orient="horizontal")
        separator9.place(anchor="nw", width=200, x=200, y=715)
        separator10 = ttk.Separator(frame1)
        separator10.configure(orient="horizontal")
        separator10.place(anchor="nw", width=200, x=800, y=715)
        self.lblRegister = ttk.Label(frame1, name="lblregister")
        self.lblRegister.configure(
            background="#ffffff",
            font="{NSimSun} 14 {}",
            text='  Crear una nueva cuenta')
        self.lblRegister.place(anchor="nw", width=300, x=450, y=700)
        self.btnRegister = ttk.Button(frame1, name="btnregister")
        self.btnRegister.configure(text='Registrarse')
        self.btnRegister.place(anchor="nw", width=300, x=450, y=740)
        self.lblTitle = ttk.Label(frame1, name="lbltitle")
        self.lblTitle.configure(
            background="#ece693",
            font="{NSimSun} 36 {bold}",
            text=' EUREKA BANK')
        self.lblTitle.place(anchor="nw", width=400, x=400, y=130)
        self.btnFaceId = ttk.Button(frame1, name="btnfaceid")
        self.btnFaceId.configure(text='Face ID')
        self.btnFaceId.place(anchor="nw", width=300, x=450, y=640)
        separator11 = ttk.Separator(frame1)
        separator11.configure(orient="horizontal")
        separator11.place(anchor="nw", width=200, x=200, y=605)
        self.lblLoginFaceId = ttk.Label(frame1, name="lblloginfaceid")
        self.lblLoginFaceId.configure(
            background="#ffffff",
            font="{@SimSun} 14 {}",
            text='Iniciar sesión con Face ID')
        self.lblLoginFaceId.place(anchor="nw", width=315, x=445, y=590)
        separator12 = ttk.Separator(frame1)
        separator12.configure(orient="horizontal")
        separator12.place(anchor="nw", width=200, x=800, y=605)
        separator13 = ttk.Separator(frame1)
        separator13.configure(orient="horizontal")
        separator13.place(anchor="nw", width=200, x=800, y=605)

        
        self.btnIrRegistro = ttk.Button(frame1, name="btnirregistro", command=self.open_register_ui)
        self.btnIrRegistro.configure(text='Ir a Registro')
        self.btnIrRegistro.place(anchor="ne", x=1180, y=20)

        frame1.place(anchor="nw", x=0, y=0)

        # Main widget
        self.mainwindow = frame1

    def open_register_ui(self):
        from gui.sign_up.register_customerui import register_customerUI
        self.mainwindow.destroy()
        register_customerUI()
       

    def run(self):
        self.mainwindow.mainloop()

    def login_action(self):
        username = self.entryUser.get()
        password1 = self.entryPassword.get()

        if not username or not password1:
            messagebox.showwarning("Advertencia", "Por favor ingresa tanto el usuario como la contraseña")
            return

        data = BAccount.find_baccount(username=username)
        if data:
            if decode_hash_function(password1, data.acc_pass):
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
                self.mainwindow.destroy()
                # MenuUI(user_name=username)
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        else:
            messagebox.showerror("Error", "Usuario no registrado")

if __name__ == "__main__":
    root = tk.Tk()
    app = Login_bankUI(root)
    app.run()
