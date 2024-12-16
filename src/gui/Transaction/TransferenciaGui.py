#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import TransferenciaGuiui as baseui


# i18n - Setup yout translator function
# baseui.i18n_translator = mytranslator

class TransferenciaGui(baseui.TransferenciaGuiUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = TransferenciaGui()
    app.run()
