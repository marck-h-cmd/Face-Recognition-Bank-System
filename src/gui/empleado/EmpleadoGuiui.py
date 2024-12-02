#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


# Begin i18n - Setup translator in derived class file
def i18n_noop(value): return value


i18n_translator = i18n_noop
# End i18n


class empleadoGuiUI:
    def __init__(self, master=None):
        _ = i18n_translator  # i18n string marker.
        # build ui
        self.EmpleadoGUI = tk.Tk(master)
        self.EmpleadoGUI.configure(height=200, width=200)
        self.EmpleadoGUI.geometry("1197x850")
        self.fondo = tk.Canvas(self.EmpleadoGUI, name="fondo")
        self.fondo.configure(background="#f1d0a9")
        self.fondo.place(
            anchor="nw",
            height=100,
            relx=0.0,
            rely=0.1,
            width=1197,
            y=0)
        self.fondo2 = tk.Canvas(self.EmpleadoGUI, name="fondo2")
        self.fondo2.configure(background="#f0f1ef")
        self.fondo2.place(
            anchor="nw",
            height=600,
            relx=0.02,
            rely=0.23,
            width=300,
            x=0,
            y=0)
        self.btnRegistrarUsuario = ttk.Button(
            self.EmpleadoGUI, name="btnregistrarusuario")
        self.btnRegistrarUsuario.configure(text=_('Registrar Usuario ->'))
        self.btnRegistrarUsuario.place(
            anchor="nw", relx=0.08, rely=0.29, x=0, y=0)
        self.btnRegistarCuenta = ttk.Button(
            self.EmpleadoGUI, name="btnregistarcuenta")
        self.btnRegistarCuenta.configure(text=_('Registrar Cuenta ->'))
        self.btnRegistarCuenta.place(
            anchor="nw", relx=0.08, rely=0.38, x=0, y=0)
        self.btnOperacion = ttk.Button(self.EmpleadoGUI, name="btnoperacion")
        self.btnOperacion.configure(text=_('Operancion ->'))
        self.btnOperacion.place(anchor="nw", relx=0.08, rely=0.46, x=0, y=0)
        self.btnInversion = ttk.Button(self.EmpleadoGUI, name="btninversion")
        self.btnInversion.configure(text=_('Inversion ->'))
        self.btnInversion.place(anchor="nw", relx=0.08, rely=0.55, x=0, y=0)
        self.btnMostrarIn = ttk.Button(self.EmpleadoGUI, name="btnmostrarin")
        self.btnMostrarIn.configure(text=_('Mostrar Inversion ->'))
        self.btnMostrarIn.place(anchor="nw", relx=0.08, rely=0.64, x=0, y=0)
        self.btnMostarCu = ttk.Button(self.EmpleadoGUI, name="btnmostarcu")
        self.btnMostarCu.configure(text=_('Mostrar Cuentas ->'))
        self.btnMostarCu.place(anchor="nw", relx=0.08, rely=0.74, x=0, y=0)
        self.btnMostrarOp = ttk.Button(self.EmpleadoGUI, name="btnmostrarop")
        self.btnMostrarOp.configure(text=_('Mostrar Operaciones ->'))
        self.btnMostrarOp.place(anchor="nw", relx=0.08, rely=0.83, x=0, y=0)
        self.separator1 = ttk.Separator(self.EmpleadoGUI)
        self.separator1.configure(orient="horizontal")
        self.separator1.place(
            anchor="nw",
            relx=0.29,
            rely=0.37,
            width=840,
            x=0,
            y=0)
        self.btnLogo = ttk.Button(self.EmpleadoGUI, name="btnlogo")
        self.img_banco = tk.PhotoImage(file="src/img/banco.png")
        self.btnLogo.configure(image=self.img_banco)
        self.btnLogo.place(anchor="nw", relx=0.02, rely=0.03, x=0, y=0)
        self.lblLogo = ttk.Label(self.EmpleadoGUI, name="lbllogo")
        self.lblLogo.configure(text=_('Nombre del banco\n'))
        self.lblLogo.place(anchor="nw", relx=0.07, rely=0.04, x=0, y=0)
        self.btnUsuario = ttk.Button(self.EmpleadoGUI, name="btnusuario")
        self.img_Usuario = tk.PhotoImage(file="src/img/Usuario.gif")
        self.btnUsuario.configure(image=self.img_Usuario)
        self.btnUsuario.place(anchor="nw", relx=0.94, rely=0.03, x=0, y=0)
        self.fondoOp1 = tk.Canvas(self.EmpleadoGUI, name="fondoop1")
        self.fondoOp1.configure(background="#f0f1ef")
        self.fondoOp1.place(
            anchor="nw",
            height=100,
            relx=0.28,
            rely=0.23,
            width=200,
            x=0,
            y=0)
        self.fondoOp2 = tk.Canvas(self.EmpleadoGUI, name="fondoop2")
        self.fondoOp2.configure(background="#f0f1ef")
        self.fondoOp2.place(
            anchor="nw",
            height=100,
            relx=0.46,
            rely=0.23,
            width=200,
            x=0,
            y=0)
        self.fondoOp3 = tk.Canvas(self.EmpleadoGUI, name="fondoop3")
        self.fondoOp3.configure(background="#f0f1ef")
        self.fondoOp3.place(
            anchor="nw",
            height=100,
            relx=0.64,
            rely=0.23,
            width=200,
            x=0,
            y=0)
        self.fondoOp4 = tk.Canvas(self.EmpleadoGUI, name="fondoop4")
        self.fondoOp4.configure(background="#f0f1ef")
        self.fondoOp4.place(
            anchor="nw",
            height=100,
            relx=0.82,
            rely=0.23,
            width=200,
            x=0,
            y=0)
        self.lblTrans = ttk.Label(self.EmpleadoGUI, name="lbltrans")
        self.lblTrans.configure(background="#f0f1ef", text=_('Transferencias'))
        self.lblTrans.place(anchor="nw", relx=0.33, rely=0.31, x=0, y=0)
        self.lblInversion = ttk.Label(self.EmpleadoGUI, name="lblinversion")
        self.lblInversion.configure(background="#f0f1ef", text=_('Inversion'))
        self.lblInversion.place(anchor="nw", relx=0.51, rely=0.31, x=0, y=0)
        self.lblMoneda = ttk.Label(self.EmpleadoGUI, name="lblmoneda")
        self.lblMoneda.configure(background="#f0f1ef", text=_('Moneda'))
        self.lblMoneda.place(anchor="nw", relx=0.69, rely=0.31, x=0, y=0)
        self.lblCliente = ttk.Label(self.EmpleadoGUI, name="lblcliente")
        self.lblCliente.configure(background="#f0f1ef", text=_('Cliente'))
        self.lblCliente.place(anchor="nw", relx=0.89, rely=0.31, x=0, y=0)
        self.btnTrans = ttk.Button(self.EmpleadoGUI, name="btntrans")
        self.img_transferenciadedinero = tk.PhotoImage(
            file="src/img/transferencia-de-dinero.png")
        self.btnTrans.configure(image=self.img_transferenciadedinero)
        self.btnTrans.place(anchor="nw", relx=0.34, rely=0.24, x=0, y=0)
        self.btnInver = ttk.Button(self.EmpleadoGUI, name="btninver")
        self.img_ganador = tk.PhotoImage(file="src/img/ganador.png")
        self.btnInver.configure(image=self.img_ganador)
        self.btnInver.place(anchor="nw", relx=0.51, rely=0.24, x=0, y=0)
        self.btnMoneda = ttk.Button(self.EmpleadoGUI, name="btnmoneda")
        self.img_dinero = tk.PhotoImage(file="src/img/dinero.png")
        self.btnMoneda.configure(image=self.img_dinero)
        self.btnMoneda.place(anchor="nw", relx=0.70, rely=0.26, x=0, y=0)
        self.btnCliente = ttk.Button(self.EmpleadoGUI, name="btncliente")
        self.img_Cliente = tk.PhotoImage(file="src/img/Cliente.png")
        self.btnCliente.configure(image=self.img_Cliente)
        self.btnCliente.place(anchor="nw", relx=0.88, rely=0.24, x=0, y=0)

        # Main widget
        self.mainwindow = self.EmpleadoGUI

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


if __name__ == "__main__":
    app = empleadoGuiUI()
    app.run()
