#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from gui.Transaction.TransferenciaGuiui import TransferenciaGuiUI

# Begin i18n - Setup translator in derived class file
def i18n_noop(value): return value


i18n_translator = i18n_noop
# End i18n


class ClienteGUIUI:
    def __init__(self,baccount, master=None,):
        _ = i18n_translator  # i18n string marker.
        # build ui
        self.ClienteGui = tk.Tk(master)
        self.ClienteGui.configure(height=200, width=200)
        self.ClienteGui.geometry("1131x967")
        self.ClienteGui.resizable(True, True)
        self.fondo = tk.Canvas(self.ClienteGui, name="fondo")
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
            rely=0.09,
            width=1128,
            y=0)
        self.fondo.bind("<1>", self.callback, add="")
        self.btnUsuario = ttk.Button(self.ClienteGui, name="btnusuario")
        self.img_usuario = tk.PhotoImage(file="src/img/usuario.png")
        self.btnUsuario.configure(
            cursor="arrow",
            default="normal",
            image=self.img_usuario,
            style="Toolbutton")
        self.btnUsuario.place(anchor="nw", relx=0.91, rely=0.03, x=0, y=0)
        self.lblFe = ttk.Label(self.ClienteGui, name="lblfe")
        self.lblFe.configure(
            justify="left",
            relief="flat",
            state="normal",
            takefocus=False,
            text=_('fecha...\n'))
        self.lblFe.place(anchor="nw", relx=0.85, rely=0.04, x=0, y=0)
        self.btnLogo = ttk.Button(self.ClienteGui, name="btnlogo")
        self.img_banco = tk.PhotoImage(file="src/img/banco.png")
        self.btnLogo.configure(image=self.img_banco, style="Toolbutton")
        self.btnLogo.place(anchor="nw", relx=0.04, rely=0.03, x=0, y=0)
        self.lblLogo = ttk.Label(self.ClienteGui, name="lbllogo")
        self.lblLogo.configure(text=_('Nombre Del Banco\n'))
        self.lblLogo.place(anchor="nw", relx=0.1, rely=0.04, x=0, y=0)
        self.fondoMonto = tk.Canvas(self.ClienteGui, name="fondomonto")
        self.fondoMonto.configure(background="#f4f4f4", cursor="arrow")
        self.fondoMonto.place(
            anchor="nw",
            height=150,
            relx=0.03,
            rely=0.21,
            width=250,
            x=0,
            y=0)
        self.fondoOp1 = tk.Canvas(self.ClienteGui, name="fondoop1")
        self.fondoOp1.configure(background="#f4f4f4", cursor="arrow")
        self.fondoOp1.place(
            anchor="nw",
            height=150,
            relx=0.30,
            rely=0.21,
            width=150,
            x=0,
            y=0)
        self.fondoOp2 = tk.Canvas(self.ClienteGui, name="fondoop2")
        self.fondoOp2.configure(background="#f4f4f4", cursor="arrow")
        self.fondoOp2.place(
            anchor="nw",
            height=150,
            relx=0.48,
            rely=0.21,
            width=150,
            x=0,
            y=0)
        self.fondoOp3 = tk.Canvas(self.ClienteGui, name="fondoop3")
        self.fondoOp3.configure(background="#f4f4f4", cursor="arrow")
        self.fondoOp3.place(
            anchor="nw",
            height=150,
            relx=0.66,
            rely=0.21,
            width=150,
            x=0,
            y=0)
        self.fondoOp4 = tk.Canvas(self.ClienteGui, name="fondoop4")
        self.fondoOp4.configure(background="#f4f4f4", cursor="arrow")
        self.fondoOp4.place(
            anchor="nw",
            height=150,
            relx=0.85,
            rely=0.21,
            width=150,
            x=0,
            y=0)
        self.btnMonto = ttk.Button(self.ClienteGui, name="btnmonto")
        self.img_dinero = tk.PhotoImage(file="src/img/dinero.png")
        self.btnMonto.configure(image=self.img_dinero)
        self.btnMonto.place(anchor="nw", relx=0.06, rely=0.26, x=0, y=0)
        self.btnTransferencias = ttk.Button(
            self.ClienteGui, name="btntransferencias",command=self.on_window_transaction)
        self.img_transferenciadedinero = tk.PhotoImage(
            file="src/img/transferencia-de-dinero.png")
        self.btnTransferencias.configure(image=self.img_transferenciadedinero)
        self.btnTransferencias.place(
            anchor="nw", relx=0.34, rely=0.24, x=0, y=0)
        self.btnPagos = ttk.Button(self.ClienteGui, name="btnpagos")
        self.img_metododepago = tk.PhotoImage(file="src/img/metodo-de-pago.png")
        self.btnPagos.configure(image=self.img_metododepago)
        self.btnPagos.place(anchor="nw", relx=0.52, rely=0.24, x=0, y=0)
        self.btnTarjeta = ttk.Button(self.ClienteGui, name="btntarjeta", command=self.on_window_card)
        self.img_tarjeta = tk.PhotoImage(file="src/img/tarjeta.png")
        self.btnTarjeta.configure(compound="top", image=self.img_tarjeta)
        self.btnTarjeta.place(
            anchor="nw",
            height=60,
            relx=0.69,
            rely=0.24,
            width=70,
            x=0,
            y=0)
        self.btnEstado = ttk.Button(self.ClienteGui, name="btnestado")
        self.img_impuesto = tk.PhotoImage(file="src/img/impuesto.png")
        self.btnEstado.configure(image=self.img_impuesto)
        self.btnEstado.place(anchor="nw", relx=0.89, rely=0.24, x=0, y=0)
        self.lblTransferencias = ttk.Label(
            self.ClienteGui, name="lbltransferencias")
        self.lblTransferencias.configure(
            background="#f4f4f4", text=_('Transferencias'))
        self.lblTransferencias.place(
            anchor="nw", relx=0.33, rely=0.31, x=0, y=0)
        self.lblPagos = ttk.Label(self.ClienteGui, name="lblpagos")
        self.lblPagos.configure(
            background="#f4f4f4",
            text=_('Pagos y Servicios'))
        self.lblPagos.place(anchor="nw", relx=0.50, rely=0.31, x=0, y=0)
        self.lblTarjeta = ttk.Label(self.ClienteGui, name="lbltarjeta")
        self.lblTarjeta.configure(
            background="#f4f4f4",
            compound="top",
            cursor="arrow",
            state="normal",
            text=_('Tarjetas\n'))
        self.lblTarjeta.place(anchor="nw", relx=0.70, rely=0.31, x=0, y=0)
        self.lblEstado = ttk.Label(self.ClienteGui, name="lblestado")
        self.lblEstado.configure(
            background="#f4f4f4",
            text=_('Estado De Cuenta\n'))
        self.lblEstado.place(anchor="nw", relx=0.87, rely=0.31, x=0, y=0)
        self.lblSaldo = ttk.Label(self.ClienteGui, name="lblsaldo")
        self.lblSaldo.configure(
            anchor="n",
            background="#f4f4f4",
            cursor="arrow",
            font="TkDefaultFont",
            relief="flat",
            state="normal",
            text=_('Saldo\n'))
        self.lblSaldo.place(anchor="nw", relx=0.11, rely=0.26, x=0, y=0)

        # Main widget
        self.mainwindow = self.ClienteGui

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

    def run(self, center=False):
        if center:
            """ If `width` and `height` are set for the main widget,
            this is the only time TK returns them. """
            self.main_w = self.mainwindow.winfo_reqwidth()
            self.main_h = self.mainwindow.winfo_reqheight()
            self.center_map = self.mainwindow.bind("<Map>", self.center)
        self.mainwindow.mainloop()

    def callback(self, event=None):
        pass
    
    def on_window_card(self):
        from gui.bank.bank_cardui import Bank_cardUI
        Bank_cardUI(self.mainwindow )
    def on_window_transaction(self):
        from gui.Transaction.TransferenciaGuiui import TransferenciaGuiui 
        TransferenciaGuiUI(self.mainwindow )

if __name__ == "__main__":
    app = ClienteGUIUI()
    app.run()
