#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class Bank_cardUI:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.img_user_color = tk.PhotoImage(file="user_color.png")
        toplevel1.configure(
            background="#ffffff",
            cursor="arrow",
            height=700,
            highlightbackground="#64ddd1",
            width=800)
        toplevel1.geometry("780x650")
        toplevel1.iconphoto(True, self.img_user_color)
        toplevel1.resizable(True, True)
        toplevel1.title("pruducto_registro")
        canvas3 = tk.Canvas(toplevel1)
        canvas3.configure(
            background="#f9f9f9",
            relief="raised",
            selectbackground="#c0c0c0",
            state="normal")
        canvas3.place(
            height=200,
            relheight=0.06,
            relwidth=0.13,
            relx=0.0,
            rely=0.0,
            width=500,
            x=100,
            y=300)
        self.txt_code = ttk.Entry(toplevel1, name="txt_code")
        self.txt_code.configure(style="info")
        self.txt_code.place(anchor="nw", height=30, width=150, x=200, y=110)
        self.txt_name = ttk.Entry(toplevel1, name="txt_name")
        self.txt_name.configure(style="info")
        self.txt_name.place(
            anchor="nw",
            height=30,
            relx=0.06,
            width=150,
            x=482,
            y=130)
        self.txt_numtarje = ttk.Entry(toplevel1, name="txt_numtarje")
        self.txt_numtarje.configure(style="info")
        self.txt_numtarje.place(
            anchor="nw",
            height=30,
            width=200,
            x=150,
            y=350)
        self.cbx_category = ttk.Combobox(toplevel1, name="cbx_category")
        self.cbx_category.configure(style="info", validate="none")
        self.cbx_category.place(
            anchor="nw",
            height=30,
            width=150,
            x=200,
            y=150)
        self.lbl_code = ttk.Label(toplevel1, name="lbl_code")
        self.lbl_code.configure(
            background="#ffffff",
            compound="left",
            cursor="based_arrow_down",
            justify="left",
            padding=5,
            text='Codigo Cliente:')
        self.lbl_code.place(anchor="nw", relx=0.0, rely=0.0, x=50, y=110)
        self.lbl_name = ttk.Label(toplevel1, name="lbl_name")
        self.lbl_name.configure(
            background="#ffffff",
            compound="bottom",
            padding=5,
            relief="flat",
            state="normal",
            text='Nombre')
        self.lbl_name.place(anchor="nw", x=475, y=100)
        self.lbl_category = ttk.Label(toplevel1, name="lbl_category")
        self.lbl_category.configure(
            background="#ffffff",
            compound="top",
            justify="left",
            padding=5,
            state="normal",
            takefocus=False,
            text='Apellidos')
        self.lbl_category.place(anchor="nw", rely=0.12, x=475, y=90)
        self.lbl_stock = ttk.Label(toplevel1, name="lbl_stock")
        self.lbl_stock.configure(
            background="#ffffff",
            compound="bottom",
            padding=5,
            takefocus=False,
            text='Tipo Tarjeta\n')
        self.lbl_stock.place(anchor="nw", x=50, y=150)
        self.lbl_nrocard = ttk.Label(toplevel1, name="lbl_nrocard")
        self.lbl_nrocard.configure(
            background="#f9f9f9",
            compound="top",
            cursor="arrow",
            padding=5,
            text='Numero Tarjeta:')
        self.lbl_nrocard.place(anchor="nw", relx=0.0, x=130, y=310)
        label8 = ttk.Label(toplevel1)
        label8.configure(
            background="#ffffff",
            compound="top",
            font="TkDefaultFont",
            state="normal",
            takefocus=True,
            text='Solicitar Tarjeta\n')
        label8.place(anchor="nw", relx=0.0, rely=0.04, x=200, y=40)
        label1 = ttk.Label(toplevel1)
        label1.configure(
            background="#ffffff",
            compound="left",
            font="TkTextFont",
            justify="left",
            relief="flat",
            state="normal",
            text='Informacion del cliente\n')
        label1.place(anchor="nw", relx=0.04, rely=0.04, x=500, y=40)
        self.txt_surname = ttk.Entry(toplevel1, name="txt_surname")
        self.txt_surname.configure(style="info")
        self.txt_surname.place(
            anchor="nw",
            height=30,
            relx=0.06,
            rely=0.11,
            width=150,
            x=482,
            y=130)
        label2 = ttk.Label(toplevel1)
        label2.configure(
            background="#ffffff",
            compound="top",
            font="TkDefaultFont",
            state="normal",
            takefocus=True,
            text='Informacion Tarjeta\n')
        label2.place(anchor="nw", relx=0.0, rely=0.04, x=100, y=240)
        button1 = ttk.Button(toplevel1)
        button1.configure(
            cursor="arrow",
            default="normal",
            text='SOLICITAR TARJETA')
        button1.place(anchor="nw", relx=0.25, rely=0.32, x=0, y=0)
        button3 = ttk.Button(toplevel1)
        button3.configure(cursor="arrow", default="normal", text='Consultar')
        button3.place(anchor="nw", relx=0.47, rely=0.17, x=0, y=0)
        self.txt = ttk.Label(toplevel1, name="txt")
        self.txt.configure(
            background="#f9f9f9",
            compound="top",
            cursor="arrow",
            padding=5,
            text='Fecha Expiracion:')
        self.txt.place(anchor="nw", rely=0.13, x=130, y=310)
        self.txt_exp = ttk.Entry(toplevel1, name="txt_exp")
        self.txt_exp.configure(style="info")
        self.txt_exp.place(
            anchor="nw",
            height=30,
            rely=0.13,
            width=150,
            x=150,
            y=350)
        self.label4 = ttk.Label(toplevel1, name="label4")
        self.label4.configure(
            background="#f9f9f9",
            compound="top",
            cursor="arrow",
            padding=5,
            text='Fecha Expiracion:')
        self.label4.place(anchor="nw", relwidth=0.0, rely=0.0, x=130, y=310)
        self.txt_tipocard = ttk.Entry(toplevel1, name="txt_tipocard")
        self.txt_tipocard.configure(style="info")
        self.txt_tipocard.place(
            anchor="nw",
            height=30,
            relx=0.38,
            rely=0.08,
            width=150,
            x=150,
            y=350)
        self.txt_tipotarj = ttk.Label(toplevel1, name="txt_tipotarj")
        self.txt_tipotarj.configure(
            background="#f9f9f9",
            compound="top",
            cursor="arrow",
            padding=5,
            text='Tipo Tarjeta:')
        self.txt_tipotarj.place(
            anchor="nw",
            relx=0.41,
            rely=0.08,
            x=130,
            y=310)
        toplevel1.pack_propagate(0)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = Bank_cardUI()
    app.run()
