import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import formularios.articulos

class FormularioArticulos:
    def __init__(self):
        self.articulo1=formularios.articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Mantenimiento de artículos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    
   
    
    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de artículos")
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Artículo")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe4, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.codigoborra.get(), )
        cantidad=self.articulo1.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar artículo")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Artículo")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe5, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe5, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcionmod=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe5, textvariable=self.descripcionmod)
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe5, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe5, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton2.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):
        datos=(self.descripcionmod.get(), self.preciomod.get(), self.codigomod.get())
        cantidad=self.articulo1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def consultar_mod(self):
        datos=(self.codigomod.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcionmod.set(respuesta[0][0])
            self.preciomod.set(respuesta[0][1])
        else:
            self.descripcionmod.set('')
            self.preciomod.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")


aplicacion1=FormularioArticulos()