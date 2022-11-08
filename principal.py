import tkinter 
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import formularios.login
import formularios.registrar
import formularios.registrar2
import formularios.articulos
import formularios.listado
import formularios.ventana
def inicio_sesion():
    formularios.login.mostrar() 
    

def registro_datos():
    formularios.registrar.registrar()
pantalla = tk.Tk()
pantalla.geometry("1280x720")
pantalla.title("BIENVENIDOS")
pantalla.iconbitmap("images.ico")

image = PhotoImage(file = "images.gif")
image = image.subsample(1,1)
label=Label(image=image)
label.pack()
Label(text="ACCESO AL SISTEMA",  fg="navy",width="300",height="1", font=("calibri", 25)).pack()

Label(text="DEL GYM",  fg="navy",width="300",height="1", font=("calibri", 25)).pack()
Label(text="").pack()
Button(text="INICIAR SESION", width="30",height="3",command =inicio_sesion).pack()
Label(text="").pack()
Button(text="REGISTRAR", width="30",height="3",command = registro_datos).pack()

pantalla.mainloop()





