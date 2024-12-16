#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import login_bankui as baseui


class Login_bank(baseui.Login_bankUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    root = tk.Tk()
    app = Login_bank(root)
    app.run()
