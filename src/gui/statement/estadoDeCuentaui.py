#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


# Begin i18n - Setup translator in derived class file
def i18n_noop(value): return value


i18n_translator = i18n_noop
# End i18n


class estadoUI:
    def __init__(self, master=None):
        _ = i18n_translator  # i18n string marker.
        # build ui
        self.estados = tk.Toplevel(master, container="false")
        self.estados.configure(height=200, width=200)
        self.estados.geometry("1120x700")
        self.decoracion = tk.Canvas(self.estados, name="decoracion")
        self.decoracion.configure(background="#ede1ba")
        self.decoracion.place(anchor="nw", height=100, width=1120, x=0, y=0)
        self.lblUsuario = ttk.Label(self.estados, name="lblusuario")
        self.lblUsuario.configure(
            font="TkTextFont",
            justify="left",
            relief="flat",
            takefocus=False,
            text=_('Usuario:'))
        self.lblUsuario.place(anchor="nw", relx=0.14, rely=0.21, x=0, y=0)
        self.lblFecha = ttk.Label(self.estados, name="lblfecha")
        self.lblFecha.configure(text=_('Fecha de Creacion:'))
        self.lblFecha.place(anchor="nw", relx=0.14, rely=0.29, x=0, y=0)
        self.lblMonto = ttk.Label(self.estados, name="lblmonto")
        self.lblMonto.configure(
            compound="top",
            cursor="arrow",
            font="TkDefaultFont",
            justify="left",
            relief="flat",
            text=_('Monto:'))
        self.lblMonto.place(anchor="nw", relx=0.14, rely=0.38, x=0, y=0)
        self.lblMovimiento = ttk.Label(self.estados, name="lblmovimiento")
        self.lblMovimiento.configure(text=_('Cantidad de movimiento:'))
        self.lblMovimiento.place(anchor="nw", relx=0.14, rely=0.45, x=0, y=0)
        self.lblNombreUsuario = ttk.Label(
            self.estados, name="lblnombreusuario")
        self.lblNombreUsuario.configure(
            compound="bottom",
            cursor="arrow",
            font="TkDefaultFont",
            relief="flat",
            state="normal",
            text=_('aqui va usuario\n'))
        self.lblNombreUsuario.place(
            anchor="nw", relx=0.33, rely=0.21, x=0, y=0)
        self.lblFechaCreacion = ttk.Label(
            self.estados, name="lblfechacreacion")
        self.lblFechaCreacion.configure(text=_('Aqui va la fecha'))
        self.lblFechaCreacion.place(
            anchor="nw", relx=0.33, rely=0.28, x=0, y=0)
        self.lblMontoE = ttk.Label(self.estados, name="lblmontoe")
        self.lblMontoE.configure(
            compound="top",
            cursor="arrow",
            font="TkDefaultFont",
            relief="flat",
            text=_('aqui va el monto'))
        self.lblMontoE.place(anchor="nw", relx=0.33, rely=0.38, x=0, y=0)
        self.lblCantidadMov = ttk.Label(self.estados, name="lblcantidadmov")
        self.lblCantidadMov.configure(text=_('aqui va cantidad de movimiento'))
        self.lblCantidadMov.place(anchor="nw", relx=0.33, rely=0.45, x=0, y=0)
        self.tblTarjetas = ttk.Treeview(self.estados, name="tbltarjetas")
        self.tblTarjetas.configure(selectmode="none", show="headings")
        self.tblTarjetas_cols = [
            'colNumeroTarjeta',
            'colFechaExpiracion',
            'colTipoCuenta']
        self.tblTarjetas_dcols = [
            'colNumeroTarjeta',
            'colFechaExpiracion',
            'colTipoCuenta']
        self.tblTarjetas.configure(
            columns=self.tblTarjetas_cols,
            displaycolumns=self.tblTarjetas_dcols)
        self.tblTarjetas.column(
            "colNumeroTarjeta",
            anchor="w",
            stretch=False,
            width=100,
            minwidth=10)
        self.tblTarjetas.column(
            "colFechaExpiracion",
            anchor="w",
            stretch=False,
            width=200,
            minwidth=10)
        self.tblTarjetas.column(
            "colTipoCuenta",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=10)
        self.tblTarjetas.heading(
            "colNumeroTarjeta",
            anchor="w",
            text=_('Tarjeta\n'))
        self.tblTarjetas.heading(
            "colFechaExpiracion",
            anchor="w",
            text=_('Fecha de Expiracion'))
        self.tblTarjetas.heading("colTipoCuenta", anchor="w", text=_('Tipo'))
        self.tblTarjetas.place(anchor="nw", relx=0.06, rely=0.6, x=0, y=0)
        self.tblTransferencias = ttk.Treeview(
            self.estados, name="tbltransferencias")
        self.tblTransferencias.configure(
            selectmode="extended", show="headings")
        self.tblTransferencias_cols = [
            'colCodigo',
            'colOrigen',
            'colDestino',
            'colMonto',
            'colFecha',
            'colTipo']
        self.tblTransferencias_dcols = [
            'colCodigo',
            'colOrigen',
            'colDestino',
            'colMonto',
            'colFecha',
            'colTipo']
        self.tblTransferencias.configure(
            columns=self.tblTransferencias_cols,
            displaycolumns=self.tblTransferencias_dcols)
        self.tblTransferencias.column(
            "colCodigo",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.tblTransferencias.column(
            "colOrigen",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.tblTransferencias.column(
            "colDestino",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.tblTransferencias.column(
            "colMonto",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.tblTransferencias.column(
            "colFecha",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.tblTransferencias.column(
            "colTipo",
            anchor="w",
            stretch=False,
            width=100,
            minwidth=20)
        self.tblTransferencias.heading(
            "colCodigo", anchor="w", text=_('Codigo'))
        self.tblTransferencias.heading(
            "colOrigen", anchor="w", text=_('Origen'))
        self.tblTransferencias.heading(
            "colDestino", anchor="w", text=_('Destino'))
        self.tblTransferencias.heading("colMonto", anchor="w", text=_('Monto'))
        self.tblTransferencias.heading("colFecha", anchor="w", text=_('Fecha'))
        self.tblTransferencias.heading("colTipo", anchor="w", text=_('Tipo'))
        self.tblTransferencias.place(
            anchor="nw", relx=0.45, rely=0.6, x=0, y=0)
        self.txtBuscarTarjeta = ttk.Entry(
            self.estados, name="txtbuscartarjeta")
        self.txtBuscarTarjeta.place(
            anchor="nw", relx=0.13, rely=0.54, x=0, y=0)
        self.txtBuscarFeha = ttk.Entry(self.estados, name="txtbuscarfeha")
        self.txtBuscarFeha.place(anchor="nw", relx=0.62, rely=0.54, x=0, y=0)
        self.btnBuscarFecha = ttk.Button(self.estados, name="btnbuscarfecha")
        self.btnBuscarFecha.configure(text=_('Buscar Fecha'))
        self.btnBuscarFecha.place(anchor="nw", relx=0.79, rely=0.54, x=0, y=0)
        self.btnBuscarTarjeta = ttk.Button(
            self.estados, name="btnbuscartarjeta")
        self.btnBuscarTarjeta.configure(text=_('Buscar Tarjeta'))
        self.btnBuscarTarjeta.place(anchor="nw", relx=0.3, rely=0.54, x=0, y=0)

        # Main widget
        self.mainwindow = self.estados

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
    app = estadoUI()
    app.run()
