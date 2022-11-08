import tkinter 
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import formularios.registrar2 
import formularios.ventana
def app():
    global pantalla4
    pantalla4 = tk.Tk()
    pantalla4.geometry("1280x720")
    pantalla4.title("BIENVENIDOS")
    pantalla4.iconbitmap("images.ico")
    
    Label(pantalla4,text="ACCESO AL SISTEMA",  fg="navy",width="300",height="1", font=("calibri", 25)).pack()

    Label(pantalla4,text="DEL GYM",  fg="navy",width="300",height="1", font=("calibri", 25)).pack()
    Label(pantalla4,text="").pack()
    Label(pantalla4,text="").pack()
    Button(pantalla4,text="REGISTRAR CLIENTE", width="30",height="3",command = registro_datos).pack()
    Label(pantalla4,text="").pack()
    Label(pantalla4,text="").pack()
    Button(pantalla4,text="CONSULTAR POR NUMERO CLIENTE", width="30",height="3",command = registro_datos).pack()
    Label(pantalla4,text="").pack()
    Label(pantalla4,text="").pack()
    Button(pantalla4,text="INGRESAR MES PAGO", width="30",height="3",command = registro_datos).pack()
    Label(pantalla4,text="").pack()
    Label(pantalla4,text="").pack()
    Button(pantalla4,text="DAR DE BAJA AL CLIENTE", width="30",height="3",command = registro_datos).pack()
    Label(pantalla4,text="").pack()
    Label(pantalla4,text="").pack()
    Button(pantalla4,text="LISTADO COMPLETO DE CLIENTES", width="30",height="3",command = listado_completo).pack()


def registro_datos():
    formularios.registrar2.registrar()

def listado_completo():
    root = Tk()
    root.wm_title("LISTADO DE CLIENTES")
    app = formularios.ventana.Ventana(root)
    app.mainloop()
       









