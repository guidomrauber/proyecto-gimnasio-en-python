import tkinter 
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mostrar():
    pantalla1 = tk.Tk()
    pantalla1.geometry("800x600")
    pantalla1.title("INICIO DE SESION")
    pantalla1.iconbitmap("images.ico")
    
    
    Label(pantalla1, text="POR FAVOR INGRESE SU USUARIO Y CONTRASEÑA",fg="navy",width="300",height="1", font=("calibri", 25)).pack()
    Label(pantalla1,text="").pack()

    global nusuario_ver
    global contr_ver
    nusuario_ver=StringVar()
    contr_ver=StringVar()

    global nusuario_entrar
    global contr_entrar

    Label(pantalla1, text="USUARIO").pack()
    Label(pantalla1,text="").pack()
    nusuario_entrar = Entry(pantalla1, textvariable=nusuario_ver)
    nusuario_entrar.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="CONTRASEÑA").pack()
    Label(pantalla1,text="").pack()
    contr_entrar = Entry(pantalla1, textvariable=contr_ver)
    contr_entrar.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text = "INICIAR SESION").pack()

    image = PhotoImage(file = "images.gif")
    image = image.subsample(1,1)
    label=Label(image=image)
    label.pack()
