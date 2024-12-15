#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from gui.sign_up.sign_upui import sign_upUI as RegisterUI
from gui.menu.main_menuui import MenuUI
from models.User import User
from tkinter import messagebox
from functions.utils import *

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "login.ui"
RESOURCE_PATHS = [PROJECT_PATH]
class loginUI:
    def __init__(self, master=None):
        # build ui
        self.builder = pygubu.Builder()
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: ttk.Frame = self.builder.get_object("frame1", master)
        self.builder.connect_callbacks(self)

        # Main widget
        self.mainwindow = self.frame

    def center(self, event):
        wm_min = self.mainwindow.wm_minsize()
        wm_max = self.mainwindow.wm_maxsize()
        screen_w = self.mainwindow.winfo_screenwidth()
        screen_h = self.mainwindow.winfo_screenheight()
        """ `winfo_width` / `winfo_height` at this point return `geometry` size if set. """
        x_min = min(screen_w, wm_max[0],
                    max(self.main_w, wm_min[0],
                        self.mainwindow.winfo_width(),
                        self.mainwindow.winfo_reqwidth()))
        y_min = min(screen_h, wm_max[1],
                    max(self.main_h, wm_min[1],
                        self.mainwindow.winfo_height(),
                        self.mainwindow.winfo_reqheight()))
        x = screen_w - x_min
        y = screen_h - y_min
        self.mainwindow.geometry(f"{x_min}x{y_min}+{x // 2}+{y // 2}")
        self.mainwindow.unbind("<Map>", self.center_map)

    def open_register_window(self):
        self.mainwindow.destroy()
        RegisterUI()

    #login action event
    def login_action(self):

        username = self.entry_usuario.get()
        password1 = self.entry_contrasenia.get()

        if not username or not password1:
            messagebox.showwarning("Por favor ingresa tanto el usuario como la contraseña", self.mainwindow)
            return
        user_data = User.find_user(username) 
        if user_data:
           if decode_hash_function(password1, user_data.password):          
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            self.mainwindow.destroy()  
            MenuUI(user_name=username) 
           else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        else:
            messagebox.showerror("Error", "Usuario no registrado")


    def run(self, center=False):
        if center:
            """ If `width` and `height` are set for the main widget,
            this is the only time TK returns them. """
            self.main_w = self.mainwindow.winfo_reqwidth()
            self.main_h = self.mainwindow.winfo_reqheight()
            self.center_map = self.mainwindow.bind("<Map>", self.center)
        self.mainwindow.mainloop()

