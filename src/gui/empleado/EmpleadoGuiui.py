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
        self.EmpleadoGui = tk.Tk(master)
        self.EmpleadoGui.configure(height=200, width=200)
        self.EmpleadoGui.geometry("1197x974")
        self.fondo = tk.Canvas(self.EmpleadoGui, name="fondo")
        self.fondo.configure(background="#f1d0a9")
        self.fondo.place(
            anchor="nw",
            height=100,
            relx=0.0,
            rely=0.07,
            width=1197,
            y=0)
        self.fondo2 = tk.Canvas(self.EmpleadoGui, name="fondo2")
        self.fondo2.configure(background="#e1e3df")
        self.fondo2.place(
            anchor="nw",
            height=700,
            relx=0.02,
            rely=0.19,
            width=300,
            x=0,
            y=0)
        self.btnRegistrarUsuario = ttk.Button(
            self.EmpleadoGui, name="btnregistrarusuario")
        self.btnRegistrarUsuario.configure(
            compound="top",
            takefocus=False,
            text=_('Registrar Usuario ->'))
        self.btnRegistrarUsuario.place(
            anchor="nw", relx=0.03, rely=0.23, width=279, x=0, y=0)
        self.btnTarjeta = ttk.Button(self.EmpleadoGui, name="btntarjeta")
        self.btnTarjeta.configure(
            compound="bottom",
            cursor="based_arrow_down",
            text=_('Registrar Tarjeta ->'))
        self.btnTarjeta.place(
            anchor="nw",
            relx=0.03,
            rely=0.33,
            width=279,
            x=0,
            y=0)
        self.btnOperacion = ttk.Button(self.EmpleadoGui, name="btnoperacion")
        self.btnOperacion.configure(text=_('Operancion ->'))
        self.btnOperacion.place(
            anchor="nw",
            relx=0.03,
            rely=0.43,
            width=279,
            x=0,
            y=0)
        self.btnInversion = ttk.Button(self.EmpleadoGui, name="btninversion")
        self.btnInversion.configure(text=_('Inversion ->'))
        self.btnInversion.place(
            anchor="nw",
            relx=0.03,
            rely=0.53,
            width=279,
            x=0,
            y=0)
        self.btnMostrarIn = ttk.Button(self.EmpleadoGui, name="btnmostrarin")
        self.btnMostrarIn.configure(text=_('Mostrar Inversion ->'))
        self.btnMostrarIn.place(
            anchor="nw",
            relx=0.03,
            rely=0.63,
            width=279,
            x=0,
            y=0)
        self.btnMostarCu = ttk.Button(self.EmpleadoGui, name="btnmostarcu")
        self.btnMostarCu.configure(text=_('Mostrar Cuentas ->'))
        self.btnMostarCu.place(
            anchor="nw",
            relx=0.03,
            rely=0.73,
            width=279,
            x=0,
            y=0)
        self.btnMostrarOp = ttk.Button(self.EmpleadoGui, name="btnmostrarop")
        self.btnMostrarOp.configure(text=_('Mostrar Operaciones ->'))
        self.btnMostrarOp.place(
            anchor="nw",
            relx=0.03,
            rely=0.83,
            width=279,
            x=0,
            y=0)
        self.separator1 = ttk.Separator(self.EmpleadoGui)
        self.separator1.configure(orient="horizontal")
        self.separator1.place(
            anchor="nw",
            relx=0.29,
            rely=0.31,
            width=840,
            x=0,
            y=0)
        self.btnLogo = ttk.Button(self.EmpleadoGui, name="btnlogo")
        self.img_banco = tk.PhotoImage(file="src/img/banco.png")
        self.btnLogo.configure(image=self.img_banco)
        self.btnLogo.place(anchor="nw", relx=0.02, rely=0.01, x=0, y=0)
        self.lblLogo = ttk.Label(self.EmpleadoGui, name="lbllogo")
        self.lblLogo.configure(text=_('Nombre del banco\n'))
        self.lblLogo.place(anchor="nw", relx=0.07, rely=0.02, x=0, y=0)
        self.btnUsuario = ttk.Button(self.EmpleadoGui, name="btnusuario")
        self.img_Usuario = tk.PhotoImage(file="src/img/Usuario.gif")
        self.btnUsuario.configure(image=self.img_Usuario)
        self.btnUsuario.place(anchor="nw", relx=0.94, rely=0.01, x=0, y=0)
        self.fondoOp1 = tk.Canvas(self.EmpleadoGui, name="fondoop1")
        self.fondoOp1.configure(background="#e1e3df")
        self.fondoOp1.place(
            anchor="nw",
            height=100,
            relx=0.28,
            rely=0.19,
            width=200,
            x=0,
            y=0)
        self.fondoOp2 = tk.Canvas(self.EmpleadoGui, name="fondoop2")
        self.fondoOp2.configure(background="#e1e3df")
        self.fondoOp2.place(
            anchor="nw",
            height=100,
            relx=0.46,
            rely=0.19,
            width=200,
            x=0,
            y=0)
        self.fondoOp3 = tk.Canvas(self.EmpleadoGui, name="fondoop3")
        self.fondoOp3.configure(background="#e1e3df")
        self.fondoOp3.place(
            anchor="nw",
            height=100,
            relx=0.64,
            rely=0.19,
            width=200,
            x=0,
            y=0)
        self.fondoOp4 = tk.Canvas(self.EmpleadoGui, name="fondoop4")
        self.fondoOp4.configure(background="#e1e3df")
        self.fondoOp4.place(
            anchor="nw",
            height=100,
            relx=0.82,
            rely=0.19,
            width=200,
            x=0,
            y=0)
        self.lblTrans = ttk.Label(self.EmpleadoGui, name="lbltrans")
        self.lblTrans.configure(background="#e1e3df", text=_('Transferencias'))
        self.lblTrans.place(anchor="nw", relx=0.33, rely=0.27, x=0, y=0)
        self.lblInversion = ttk.Label(self.EmpleadoGui, name="lblinversion")
        self.lblInversion.configure(background="#e1e3df", text=_('Inversion'))
        self.lblInversion.place(anchor="nw", relx=0.51, rely=0.27, x=0, y=0)
        self.lblMoneda = ttk.Label(self.EmpleadoGui, name="lblmoneda")
        self.lblMoneda.configure(background="#e1e3df", text=_('Moneda'))
        self.lblMoneda.place(anchor="nw", relx=0.69, rely=0.27, x=0, y=0)
        self.lblUsuarios = ttk.Label(self.EmpleadoGui, name="lblusuarios")
        self.lblUsuarios.configure(
            anchor="n",
            background="#e1e3df",
            cursor="arrow",
            takefocus=False,
            text=_('Usuario'))
        self.lblUsuarios.place(anchor="nw", relx=0.89, rely=0.27, x=0, y=0)
        self.btnTrans = ttk.Button(self.EmpleadoGui, name="btntrans")
        self.img_transferenciadedinero = tk.PhotoImage(
            file="src/img/transferencia-de-dinero.png")
        self.btnTrans.configure(image=self.img_transferenciadedinero)
        self.btnTrans.place(anchor="nw", relx=0.34, rely=0.2, x=0, y=0)
        self.btnInver = ttk.Button(self.EmpleadoGui, name="btninver")
        self.img_ganador = tk.PhotoImage(file="src/img/ganador.png")
        self.btnInver.configure(image=self.img_ganador)
        self.btnInver.place(anchor="nw", relx=0.51, rely=0.2, x=0, y=0)
        self.btnMoneda = ttk.Button(self.EmpleadoGui, name="btnmoneda")
        self.img_dinero = tk.PhotoImage(file="src/img/dinero.png")
        self.btnMoneda.configure(image=self.img_dinero)
        self.btnMoneda.place(anchor="nw", relx=0.70, rely=0.22, x=0, y=0)
        self.btnCliente = ttk.Button(self.EmpleadoGui, name="btncliente")
        self.img_Cliente = tk.PhotoImage(file="src/img/Cliente.png")
        self.btnCliente.configure(image=self.img_Cliente)
        self.btnCliente.place(anchor="nw", relx=0.88, rely=0.2, x=0, y=0)

        # Main widget
        self.mainwindow = self.EmpleadoGui

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
