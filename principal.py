import tkinter as tk
from tkinter import ttk

import formularios.login


class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("CONTROL DE UN GIMNASIO")        
        
        self.boton2=ttk.Button(self.ventana1, text="Mostrar formulario de login", command=self.mostrar_login)
        self.boton2.grid(column=0, row=1)
        self.ventana1.mainloop()

   
    def mostrar_login(self):
        formularios.login.mostrar()

aplicacion1=Aplicacion()