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
    def on_window_transaction(self):
        pass
    def on_window_card(self):
        pass
    def on_window_statement(self):
        pass
    def on_window_service(self):
        pass

if __name__ == "__main__":
    app = ClienteGUI()
    app.run()
