#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


# Begin i18n - Setup translator in derived class file
def i18n_noop(value): return value


i18n_translator = i18n_noop
# End i18n


class TransferenciaGuiUI:
    def __init__(self, master=None):
        _ = i18n_translator  # i18n string marker.
        # build ui
        self.TransferenciasGui = tk.Tk() if master is None else tk.Toplevel(master)
        self.TransferenciasGui.configure(cursor="arrow", width=200)
        self.TransferenciasGui.geometry("1060x600")
        self.lblTransferencias = ttk.Label(
            self.TransferenciasGui, name="lbltransferencias")
        self.lblTransferencias.configure(text=_('Transferencias'))
        self.lblTransferencias.place(
            anchor="nw", relx=0.2, rely=0.16, x=0, y=0)
        self.separador = tk.Canvas(self.TransferenciasGui, name="separador")
        self.separador.configure(background="#e6cec1", state="normal")
        self.separador.place(
            anchor="nw",
            height=600,
            relx=0.5,
            rely=0.13,
            width=10,
            x=0,
            y=0)
        self.lblRetiro = ttk.Label(self.TransferenciasGui, name="lblretiro")
        self.lblRetiro.configure(text=_('Retiro\n'))
        self.lblRetiro.place(anchor="nw", relx=0.7, rely=0.16, x=0, y=0)
        self.decoracion = tk.Canvas(self.TransferenciasGui, name="decoracion")
        self.decoracion.configure(background="#e6cec1")
        self.decoracion.place(anchor="nw", height=100, width=1060, x=0, y=0)
        self.lblIdTransferencias = ttk.Label(
            self.TransferenciasGui, name="lblidtransferencias")
        self.lblIdTransferencias.configure(
            text=_('Codigo de Transferencia:\n'))
        self.lblIdTransferencias.place(
            anchor="nw", relx=0.06, rely=0.24, x=0, y=0)
        self.lblCodigoTran = ttk.Label(
            self.TransferenciasGui, name="lblcodigotran")
        self.lblCodigoTran.configure(text=_('codigo aqui\n'))
        self.lblCodigoTran.place(anchor="nw", relx=0.24, rely=0.24, x=0, y=0)
        self.lblCuentaDestino = ttk.Label(
            self.TransferenciasGui, name="lblcuentadestino")
        self.lblCuentaDestino.configure(
            cursor="arrow",
            font="TkDefaultFont",
            justify="center",
            state="normal",
            text=_('Cuenta destino:'))
        self.lblCuentaDestino.place(
            anchor="nw", relx=0.06, rely=0.42, x=0, y=0)
        self.lblCuentaOrigen = ttk.Label(
            self.TransferenciasGui, name="lblcuentaorigen")
        self.lblCuentaOrigen.configure(text=_('Cuenta Origen:'))
        self.lblCuentaOrigen.place(anchor="nw", relx=0.06, rely=0.32, x=0, y=0)
        self.lblRetiroCu = ttk.Label(
            self.TransferenciasGui, name="lblretirocu")
        self.lblRetiroCu.configure(text=_('Cuenta para retirar:'))
        self.lblRetiroCu.place(anchor="nw", relx=0.55, rely=0.4, x=0, y=0)
        self.txtCuentaOrigen = ttk.Entry(
            self.TransferenciasGui, name="txtcuentaorigen")
        self.txtCuentaOrigen.place(anchor="nw", relx=0.16, rely=0.31, x=0, y=0)
        self.txtCuentaRetiro = ttk.Entry(
            self.TransferenciasGui, name="txtcuentaretiro")
        self.txtCuentaRetiro.place(anchor="nw", relx=0.69, rely=0.4, x=0, y=0)
        self.txtCuentaDestino = ttk.Entry(
            self.TransferenciasGui, name="txtcuentadestino")
        self.txtCuentaDestino.place(
            anchor="nw", relx=0.16, rely=0.42, x=0, y=0)
        self.lblCodigoR = ttk.Label(self.TransferenciasGui, name="lblcodigor")
        self.lblCodigoR.configure(text=_('Codigo de Retiro:'))
        self.lblCodigoR.place(anchor="nw", relx=0.55, rely=0.26, x=0, y=0)
        self.lblMonto = ttk.Label(self.TransferenciasGui, name="lblmonto")
        self.lblMonto.configure(text=_('Monto:'))
        self.lblMonto.place(anchor="nw", relx=0.06, rely=0.55, x=0, y=0)
        self.lblCodigoRetiro = ttk.Label(
            self.TransferenciasGui, name="lblcodigoretiro")
        self.lblCodigoRetiro.configure(text=_('codigo aqui'))
        self.lblCodigoRetiro.place(anchor="nw", relx=0.69, rely=0.26, x=0, y=0)
        self.lblMontoR = ttk.Label(self.TransferenciasGui, name="lblmontor")
        self.lblMontoR.configure(text=_('Monto:'))
        self.lblMontoR.place(anchor="nw", relx=0.55, rely=0.55, x=0, y=0)
        self.txtMontoT = ttk.Entry(self.TransferenciasGui, name="txtmontot")
        self.txtMontoT.place(anchor="nw", relx=0.16, rely=0.55, x=0, y=0)
        self.txtMontoR = ttk.Entry(self.TransferenciasGui, name="txtmontor")
        self.txtMontoR.place(anchor="nw", relx=0.69, rely=0.55, x=0, y=0)
        self.button1 = ttk.Button(self.TransferenciasGui)
        self.button1.configure(cursor="arrow", text=_('Transferir'))
        self.button1.place(
            anchor="nw",
            relx=0.16,
            rely=0.7,
            width=200,
            x=0,
            y=0)
        self.btnRetiro = ttk.Button(self.TransferenciasGui, name="btnretiro")
        self.btnRetiro.configure(text=_('Retiro'))
        self.btnRetiro.place(
            anchor="nw",
            relx=0.66,
            rely=0.7,
            width=200,
            x=0,
            y=0)

        # Main widget
        self.mainwindow = self.TransferenciasGui

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
    app = TransferenciaGuiUI()
    app.run()
