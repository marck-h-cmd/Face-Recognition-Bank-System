#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


# Begin i18n - Setup translator in derived class file
def i18n_noop(value): return value


i18n_translator = i18n_noop
# End i18n


class ClienteGUIUI:
    def __init__(self, master=None):
        _ = i18n_translator  # i18n string marker.
        # build ui
        self.ClienteGUI = tk.Tk(master)
        self.ClienteGUI.configure(height=200, width=200)
        self.ClienteGUI.geometry("1131x768")
        self.ClienteGUI.resizable(True, True)
        self.fondo = tk.Canvas(self.ClienteGUI, name="fondo")
        self.fondo.configure(
            background="#f1e650",
            confine=False,
            cursor="arrow",
            relief="flat",
            state="normal",
            takefocus=True)
        self.fondo.place(
            anchor="nw",
            height=100,
            relx=0.0,
            rely=0.16,
            width=1127,
            y=0)
        self.fondo.bind("<1>", self.callback, add="")
        self.btnUsuario = ttk.Button(self.ClienteGUI, name="btnusuario")
        self.img_Usuario = tk.PhotoImage(file="src/img/Usuario.gif")
        self.btnUsuario.configure(image=self.img_Usuario, style="Toolbutton")
        self.btnUsuario.place(anchor="nw", relx=0.91, rely=0.06, x=0, y=0)
        self.lblFe = ttk.Label(self.ClienteGUI, name="lblfe")
        self.lblFe.configure(
            justify="left",
            relief="flat",
            state="normal",
            takefocus=False,
            text=_('fecha...\n'))
        self.lblFe.place(anchor="nw", relx=0.84, rely=0.07, x=0, y=0)
        self.btnLogo = ttk.Button(self.ClienteGUI, name="btnlogo")
        self.img_banco = tk.PhotoImage(file="src/img/banco.png")
        self.btnLogo.configure(image=self.img_banco, style="Toolbutton")
        self.btnLogo.place(anchor="nw", relx=0.04, rely=0.07, x=0, y=0)
        self.lblLogo = ttk.Label(self.ClienteGUI, name="lbllogo")
        self.lblLogo.configure(text=_('Nombre Del Banco\n'))
        self.lblLogo.place(anchor="nw", relx=0.1, rely=0.08, x=0, y=0)
        self.fondoMonto = tk.Canvas(self.ClienteGUI, name="fondomonto")
        self.fondoMonto.configure(background="#f4f4f4", cursor="arrow")
        self.fondoMonto.place(
            anchor="nw",
            height=150,
            relx=0.03,
            rely=0.30,
            width=250,
            x=0,
            y=0)
        self.fondoOp1 = tk.Canvas(self.ClienteGUI, name="fondoop1")
        self.fondoOp1.configure(background="#f4f4f4", cursor="arrow")
        self.fondoOp1.place(
            anchor="nw",
            height=150,
            relx=0.30,
            rely=0.30,
            width=150,
            x=0,
            y=0)
        self.fondoOp2 = tk.Canvas(self.ClienteGUI, name="fondoop2")
        self.fondoOp2.configure(background="#f4f4f4", cursor="arrow")
        self.fondoOp2.place(
            anchor="nw",
            height=150,
            relx=0.48,
            rely=0.30,
            width=150,
            x=0,
            y=0)
        self.fondoOp3 = tk.Canvas(self.ClienteGUI, name="fondoop3")
        self.fondoOp3.configure(background="#f4f4f4", cursor="arrow")
        self.fondoOp3.place(
            anchor="nw",
            height=150,
            relx=0.66,
            rely=0.30,
            width=150,
            x=0,
            y=0)
        self.fondoOp4 = tk.Canvas(self.ClienteGUI, name="fondoop4")
        self.fondoOp4.configure(background="#f4f4f4", cursor="arrow")
        self.fondoOp4.place(
            anchor="nw",
            height=150,
            relx=0.85,
            rely=0.30,
            width=150,
            x=0,
            y=0)
        self.btnMonto = ttk.Button(self.ClienteGUI, name="btnmonto")
        self.img_dinero = tk.PhotoImage(file="src/img/dinero.png")
        self.btnMonto.configure(image=self.img_dinero)
        self.btnMonto.place(anchor="nw", relx=0.06, rely=0.37, x=0, y=0)
        self.txtMonto = ttk.Entry(self.ClienteGUI, name="txtmonto")
        self.txtMonto.place(
            anchor="nw",
            relx=0.11,
            rely=0.37,
            width=120,
            x=0,
            y=0)
        self.btnTransferencias = ttk.Button(
            self.ClienteGUI, name="btntransferencias")
        self.img_transferenciadedinero = tk.PhotoImage(
            file="src/img/transferencia-de-dinero.png")
        self.btnTransferencias.configure(image=self.img_transferenciadedinero)
        self.btnTransferencias.place(
            anchor="nw", relx=0.34, rely=0.35, x=0, y=0)
        self.btnPagos = ttk.Button(self.ClienteGUI, name="btnpagos")
        self.img_metododepago = tk.PhotoImage(file="src/img/metodo-de-pago.png")
        self.btnPagos.configure(image=self.img_metododepago)
        self.btnPagos.place(anchor="nw", relx=0.52, rely=0.35, x=0, y=0)
        self.btnPagoVirtual = ttk.Button(
            self.ClienteGUI, name="btnpagovirtual")
        self.img_billeteradigital = tk.PhotoImage(file="src/img/billetera-digital.png")
        self.btnPagoVirtual.configure(image=self.img_billeteradigital)
        self.btnPagoVirtual.place(anchor="nw", relx=0.69, rely=0.35, x=0, y=0)
        self.btnEstado = ttk.Button(self.ClienteGUI, name="btnestado")
        self.img_impuesto = tk.PhotoImage(file="src/img/impuesto.png")
        self.btnEstado.configure(image=self.img_impuesto)
        self.btnEstado.place(anchor="nw", relx=0.89, rely=0.35, x=0, y=0)
        self.lblTransferencias = ttk.Label(
            self.ClienteGUI, name="lbltransferencias")
        self.lblTransferencias.configure(
            background="#f4f4f4", text=_('Transferencias'))
        self.lblTransferencias.place(
            anchor="nw", relx=0.33, rely=0.44, x=0, y=0)
        self.lblPagos = ttk.Label(self.ClienteGUI, name="lblpagos")
        self.lblPagos.configure(
            background="#f4f4f4",
            text=_('Pagos y Servicios'))
        self.lblPagos.place(anchor="nw", relx=0.50, rely=0.44, x=0, y=0)
        self.lblPagoVirtual = ttk.Label(self.ClienteGUI, name="lblpagovirtual")
        self.lblPagoVirtual.configure(
            background="#f4f4f4",
            text=_('Pago Virtual\n'))
        self.lblPagoVirtual.place(anchor="nw", relx=0.69, rely=0.44, x=0, y=0)
        self.lblEstado = ttk.Label(self.ClienteGUI, name="lblestado")
        self.lblEstado.configure(
            background="#f4f4f4",
            text=_('Estado De Cuenta\n'))
        self.lblEstado.place(anchor="nw", relx=0.87, rely=0.44, x=0, y=0)

        # Main widget
        self.mainwindow = self.ClienteGUI

    def run(self):
        self.mainwindow.mainloop()

    def callback(self, event=None):
        pass


if __name__ == "__main__":
    app = ClienteGUIUI()
    app.run()
