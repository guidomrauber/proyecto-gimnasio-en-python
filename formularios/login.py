import tkinter 
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
import formularios.registrar2
import formularios.principal2 
def mostrar():
    global pantalla1
    pantalla1 = tk.Tk()
    pantalla1.geometry("1280x720")
    pantalla1.title("INICIO DE SESION")
    pantalla1.iconbitmap("images.ico")
    
    Label(pantalla1,text="").pack()
    Label(pantalla1,text="").pack()
    Label(pantalla1, text="POR FAVOR INGRESE SU USUARIO Y CONTRASEÑA",fg="navy",width="300",height="1", font=("calibri", 25)).pack()
    Label(pantalla1,text="").pack()

    nusuario_ver=StringVar()
    contr_ver=StringVar()

    global nusuario_entrar
    global contr_entrar
    Label(pantalla1).pack()
    Label(pantalla1, text="USUARIO").pack()
    Label(pantalla1,text="").pack()
    nusuario_entrar = Entry(pantalla1)
    nusuario_entrar.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="CONTRASEÑA").pack()
    Label(pantalla1,text="").pack()
    contr_entrar = Entry(pantalla1, show="*")
    contr_entrar.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text = "INICIAR SESION", command=validacion_datos).pack()
def validacion_datos():
    conexion1=pymysql.connect(host='localhost',
                                user='root',
                                passwd='',
                                db='bd3')
    cursor1=conexion1.cursor()
    sql="select * from login where usuario=%s and contrasena=%s"
    datos=(nusuario_entrar.get(),contr_entrar.get())
    global result 
    result=cursor1.execute(sql,datos)
    self=""
    if (result)>0:
           
       articulo1=formularios.principal2.app()
    else:
            messagebox.showinfo("Información", "USUARIO Y CONTRASEÑA INCORRECTO")
    conexion1.close()
    
