#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class Face_check_topUI:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Toplevel(master, container="false")
        toplevel1.configure(
            cursor="arrow",
            height=800,
            relief="sunken",
            width=950)
        canvas1 = tk.Canvas(toplevel1)
        canvas1.configure(background="#ffffbf", highlightbackground="#ff9664")
        canvas1.place(
            anchor="nw",
            height=500,
            relx=0.15,
            rely=0.03,
            width=650,
            x=0,
            y=0)
        self.video = tk.Canvas(toplevel1, name="video")
        self.video.configure(background="#fddb66", height=180, width=950)
        self.video.pack(expand=False, fill="both", side="bottom")
        self.check_btn = ttk.Button(toplevel1, name="check_btn")
        self.check_btn.configure(text='Check', width=30)
        self.check_btn.place(anchor="nw", relx=0.35, rely=0.87, x=0, y=0)
        self.check_btn.configure(command=self.check_face)
        separator2 = ttk.Separator(toplevel1)
        separator2.configure(orient="vertical")
        separator2.place(
            anchor="nw",
            bordermode="outside",
            height=2,
            relx=0.2,
            rely=0.85,
            width=500,
            x=0,
            y=0)
        self.lbl_identity = ttk.Label(toplevel1, name="lbl_identity")
        self.lbl_identity.configure(
            background="#fddb66",
            text='Verifique su identidad')
        self.lbl_identity.place(anchor="se", relx=0.52, rely=0.83, x=0, y=0)
        toplevel1.pack_propagate(0)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def check_face(self):
        pass


if __name__ == "__main__":
    app = Face_check_topUI()
    app.run()
