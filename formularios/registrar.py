import tkinter 
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

def registrar():
    global pantalla2
    pantalla2 =tk.Tk()
    pantalla2.geometry("1280x720")
    pantalla2.title("REGISTRO")
    pantalla2.iconbitmap("images.ico")

    global nusuario2_ver
    global contr2_ver
    nusuario2_ver=StringVar()
    contr2_ver=StringVar()
    Label(pantalla2).pack()
    Label(pantalla2, text="POR FAVOR INGRESE UN USUARIO Y \n CONTRASEÑA PARA REGISTRARSE",fg="navy",width="300",height="3", font=("calibri", 25)).pack()
    Label(pantalla2,text="").pack()
    
    Label(pantalla2, text="USUARIO").pack()
    Label(pantalla2,text="").pack()
    nusuario2_ver = Entry(pantalla2)
    nusuario2_ver.pack()
    Label(pantalla2).pack()
    Label(pantalla2, text="CONTRASEÑA").pack()
    Label(pantalla2,text="").pack()
    contr2_ver = Entry(pantalla2, show="*")
    contr2_ver.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text = "REGISTRAR",command=inserta_datos).pack()
def inserta_datos():
    conexion1=pymysql.connect(host='localhost',
                                user='root',
                                passwd='',
                                db='bd3')
    cursor1=conexion1.cursor()
    sql="INSERT INTO login (usuario, contrasena) VALUES (%s,%s)"
    datos=(nusuario2_ver.get(),contr2_ver.get())
    
    try:
        cursor1.execute(sql,datos)
        conexion1.commit()
        messagebox.showinfo("AVISO","REGISTRO EXITOSO")
        
    except:
        conexion1.rollback()
        messagebox.showinfo("AVISO","NO REGISTRADO")
    conexion1.close()

