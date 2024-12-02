#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import EmpleadoGuiui as baseui


# i18n - Setup yout translator function
# baseui.i18n_translator = mytranslator

class empleadoGui(baseui.empleadoGuiUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = empleadoGui()
    app.run()
