#!/usr/bin/python3
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from models.Services import Services

# Begin i18n - Setup translator in derived class file
def i18n_noop(value): return value


i18n_translator = i18n_noop
# End i18n


class ServiceUI:
    def __init__(self, master=None):
        _ = i18n_translator  # i18n string marker.
        # build ui
        self.Service = tk.Tk() if master is None else tk.Toplevel(master)
        self.Service.configure(height=200, width=200)
        self.Service.geometry("1010x700")
        self.fondo = tk.Canvas(self.Service, name="fondo")
        self.fondo.configure(background="#fefac2")
        self.fondo.place(anchor="nw", height=150, width=1152, x=0, y=0)
        self.lblCodigo = ttk.Label(self.Service, name="lblcodigo")
        self.lblCodigo.configure(text=_('Codigo:\n'))
        self.lblCodigo.place(anchor="nw", relx=0.09, rely=0.32, x=0, y=0)
        self.codigo = ttk.Label(self.Service, name="codigo")
        self.codigo.configure(text=_('cod'))
        self.codigo.place(anchor="nw", relx=0.21, rely=0.32, x=0, y=0)
        self.lblUser = ttk.Label(self.Service, name="lbluser")
        self.lblUser.configure(text=_('Usuario:'))
        self.lblUser.place(anchor="nw", relx=0.09, rely=0.39, x=0, y=0)
        self.txtUsuario = ttk.Entry(self.Service, name="txtusuario")
        self.txtUsuario.place(anchor="nw", relx=0.21, rely=0.39, x=0, y=0)
        self.lblTipo = ttk.Label(self.Service, name="lbltipo")
        self.lblTipo.configure(text=_('Tipo:'))
        self.lblTipo.place(anchor="nw", relx=0.09, rely=0.48, x=0, y=0)
        self.txtTipo = ttk.Entry(self.Service, name="txttipo")
        self.txtTipo.place(anchor="nw", relx=0.21, rely=0.48, x=0, y=0)
        self.lblDes = ttk.Label(self.Service, name="lbldes")
        self.lblDes.configure(text=_('Descripción:'))
        self.lblDes.place(anchor="nw", relx=0.09, rely=0.58, x=0, y=0)
        self.txtDescri = ttk.Entry(self.Service, name="txtdescri")
        self.txtDescri.place(anchor="nw", relx=0.21, rely=0.58, x=0, y=0)
        self.lblPrecio = ttk.Label(self.Service, name="lblprecio")
        self.lblPrecio.configure(text=_('Precio'))
        self.lblPrecio.place(anchor="nw", relx=0.09, rely=0.68, x=0, y=0)
        self.txtPrecio = ttk.Entry(self.Service, name="txtprecio")
        self.txtPrecio.place(anchor="nw", relx=0.21, rely=0.68, x=0, y=0)
        self.button1 = ttk.Button(self.Service, command=self.save)
        self.button1.configure(text=_('Registrar Servicio'))
        self.button1.place(anchor="nw", relx=0.2, rely=0.8, x=0, y=0)
        self.Servicios = ttk.Label(self.Service, name="servicios")
        self.Servicios.configure(text=_('Servicios'))
        self.Servicios.place(anchor="nw", relx=0.28, rely=0.23, x=0, y=0)
        self.canvas2 = tk.Canvas(self.Service)
        self.canvas2.configure(background="#fefac2", confine=False)
        self.canvas2.place(
            anchor="nw",
            height=650,
            relx=0.45,
            rely=0.22,
            width=20,
            x=0,
            y=0)
        self.txtConsulta = ttk.Entry(self.Service, name="txtconsulta",command=self.list_by_category_tbl)
        self.txtConsulta.place(anchor="nw", relx=0.62, rely=0.27, x=0, y=0)
        self.button2 = ttk.Button(self.Service)
        self.button2.configure(text=_('Buscar'))
        self.button2.place(anchor="nw", relx=0.83, rely=0.27, x=0, y=0)
        self.treeview1 = ttk.Treeview(self.Service)
        self.treeview1.configure(selectmode="extended", show="headings")
        self.treeview1_cols = [
            'colCod',
            'colUser',
            'colTipo',
            'colDescripcion',
            'colPrecio']
        self.treeview1_dcols = [
            'colCod',
            'colUser',
            'colTipo',
            'colDescripcion',
            'colPrecio']
        self.treeview1.configure(
            columns=self.treeview1_cols,
            displaycolumns=self.treeview1_dcols)
        self.treeview1.column(
            "colCod",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.treeview1.column(
            "colUser",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.treeview1.column(
            "colTipo",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.treeview1.column(
            "colDescripcion",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.treeview1.column(
            "colPrecio",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.treeview1.heading("colCod", anchor="w", text=_('Cod'))
        self.treeview1.heading("colUser", anchor="w", text=_('Usuario'))
        self.treeview1.heading("colTipo", anchor="w", text=_('Tipos'))
        self.treeview1.heading(
            "colDescripcion",
            anchor="w",
            text=_('Descripcion'))
        self.treeview1.heading("colPrecio", anchor="w", text=_('Precio'))
        self.treeview1.place(anchor="nw", relx=0.49, rely=0.41, x=0, y=0)

        # Main widget
        self.mainwindow = self.Service

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

    def save(self):
        code="123"
        user=self.txtUsuario.get()
        price=self.txtPrecio.get()
        description=self.txtDescri.get()
        tipo=self.txtTipo.get()
        fecha_actual = datetime.now()
        fecha_string = fecha_actual.strftime("%Y-%m-%d")


        if not user or not price or not tipo or not description or not fecha_string :
            messagebox.showerror("Error", "Llene todos los campos de texto.",parent=self.Service)
            return
        
        try:
            Services.insert(code, user, tipo, description, price, fecha_string)
            self.list()
            self.txtUsuario.delete(0, tk.END)
            self.txtDescri.delete(0,tk.END)
            self.txtPrecio.delete(0, tk.END)
            self.txtTipo.delete(0, tk.END)
        
            messagebox.showinfo("Éxito", f"Se registro el servicio",parent=self.Service)
        except Exception as e:
            messagebox.showerror("Error de registro", f"Ocurrió un error: {e}",parent=self.Service)
    
    def list(self):
        Services = Services.list_all() 
        self.treeview1.delete(*self.treeview1.get_children()) 
        for pro in Services:
            self.treeview1.insert("", "end", values=(
            pro.service_id,      
            pro.client_id,    
            pro.service_type,        
            pro.description,    
            pro.price,
            pro.date      
        ))
    
    def list_by_category_tbl(self):
        service_id = self.txtConsulta.get()
        services=Services.find_by_service_id(service_id)
        self.treeview1.delete(*self.treeview1.get_children()) 
        for pro in services:
            self.treeview1.insert("", "end", values=(
            pro.service_id,      
            pro.client_id,    
            pro.service_type,        
            pro.description,    
            pro.price,
            pro.date     
        ))

if __name__ == "__main__":
    app = ServiceUI()
    app.run()
