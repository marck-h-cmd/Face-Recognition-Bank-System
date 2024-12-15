import tkinter as tk
from tkinter import messagebox 
import tkinter.ttk as ttk
from pymongo.errors import DuplicateKeyError
from models import Customer
from functions.utils import *
from gui.sign_up.registerFaceui import RegisterFaceUI



class register_customerUI:
    def __init__(self, master=None):
        # Build UI
        tk1 = tk.Tk(master)
        tk1.configure(height=800, width=1200)
        self.bgForm = tk.Canvas(tk1, name="bgform")
        self.bgForm.configure(background="#ffffff")
        self.bgForm.place(anchor="nw", height=800, width=1200, y=0)
        self.bgTitle = tk.Canvas(tk1, name="bgtitle")
        self.bgTitle.configure(background="#eef08e")
        self.bgTitle.place(anchor="nw", height=120, width=1200, x=0, y=100)
        self.lblTitle = ttk.Label(tk1, name="lbltitle")
        self.lblTitle.configure(
            background="#eef08e",
            font="{NSimSun} 36 {bold}",
            text='EUREKA BANK')
        self.lblTitle.place(anchor="nw", x=420, y=130)
        self.lblRegister = ttk.Label(tk1, name="lblregister")
        self.lblRegister.configure(
            background="#ffffff",
            font="{NSimSun} 16 {bold}",
            text='Registro')
        self.lblRegister.place(anchor="nw", x=520, y=240)
        separator1 = ttk.Separator(tk1)
        separator1.configure(orient="horizontal")
        separator1.place(anchor="nw", width=800, x=200, y=290)
        self.entryUserName = ttk.Entry(tk1, name="entryusername")
        self.entryUserName.place(anchor="nw", width=300, x=450, y=320)
        self.entryName = ttk.Entry(tk1, name="entryname")
        self.entryName.place(anchor="nw", width=300, x=450, y=370)
        self.entryLastName = ttk.Entry(tk1, name="entrylastname")
        self.entryLastName.place(anchor="nw", width=300, x=450, y=420)
        self.entryCity = ttk.Entry(tk1, name="entrycity")
        self.entryCity.place(anchor="nw", width=300, x=450, y=470)
        self.entryDNI = ttk.Entry(tk1, name="entrydni")
        self.entryDNI.place(anchor="nw", width=300, x=450, y=520)
        self.entryPhone = ttk.Entry(tk1, name="entryphone")
        self.entryPhone.place(anchor="nw", width=300, x=450, y=570)
        self.entryEmail = ttk.Entry(tk1, name="entryemail")
        self.entryEmail.place(anchor="nw", width=300, x=450, y=620)
        separator2 = ttk.Separator(tk1)
        separator2.configure(orient="horizontal")
        separator2.place(anchor="nw", width=800, x=200, y=740)
        self.btnRegister = ttk.Button(tk1, name="btnregister")
        self.btnRegister.configure(text='Registrarse')
        self.btnRegister.place(anchor="nw", width=300, x=450, y=670)

        # Bind event
        self.btnRegister.config(command=self.register_customer)

        # Main widget
        self.mainwindow = tk1

    def register_customer(self):
        # Get values from entry fields
        clcode = generate_customer_code()
        name = self.entryName.get()
        lastname = self.entryLastName.get()
        city = self.entryCity.get()
        dni = self.entryDNI.get()
        phone = self.entryPhone.get()
        email = self.entryEmail.get()

        # Validate inputs (add more validations as needed)
        if not clcode or not name or not lastname or not dni or not email:
            tk.messagebox.showerror("Error", "Todos los campos obligatorios deben llenarse.")
            return


        try:
            # Insert customer into the database
            customer=Customer.insert(clcode, name, lastname, city, dni, phone, email)
            tk.messagebox.showinfo("Éxito", "Cliente registrado exitosamente.")
            
            RegisterFaceUI(customer=customer)
        except DuplicateKeyError:
            tk.messagebox.showerror("Error", "El código de cliente ya existe.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = register_customerUI()
    app.run()
