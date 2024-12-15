#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import bank_cardui as baseui


class Bank_card(baseui.Bank_cardUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = Bank_card()
    app.run()
