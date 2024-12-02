#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import Cliente_Guiui as baseui


# i18n - Setup yout translator function
# baseui.i18n_translator = mytranslator

class ClienteGUI(baseui.ClienteGUIUI):
    def __init__(self, master=None):
        super().__init__(master)

    def callback(self, event=None):
        pass


if __name__ == "__main__":
    app = ClienteGUI()
    app.run()
