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
    global dni2_ver
    global domi2_ver
    global email
    global telefono
    global cuota
    domi2_ver=StringVar()
    dni2_ver=IntVar()
    nusuario2_ver=StringVar()
    contr2_ver=StringVar()
    email=StringVar()
    telefono=StringVar()
    cuota=IntVar()
    Label(pantalla2, text="POR FAVOR INGRESE DATOS PARA REGISTRAR AL CLIENTE",fg="navy",width="300",height="1", font=("calibri", 25)).pack()
    Label(pantalla2,text="").pack()
    Label(pantalla2, text="NOMBRE").pack()
    Label(pantalla2,text="").pack()
    nusuario2_ver = Entry(pantalla2,width=100)
    nusuario2_ver.pack()
    Label(pantalla2).pack()
    Label(pantalla2, text="APELLIDO").pack()
    Label(pantalla2,text="").pack()
    contr2_ver = Entry(pantalla2,width=100)
    contr2_ver.pack()
    Label(pantalla2).pack()
    Label(pantalla2, text="DNI Nº").pack()
    Label(pantalla2,text="").pack()
    dni2_ver = Entry(pantalla2,width=100)
    dni2_ver.pack()
    Label(pantalla2).pack()
    Label(pantalla2, text="DOMICILIO REAL").pack()
    Label(pantalla2,text="").pack()
    domi2_ver = Entry(pantalla2,width=100)
    domi2_ver.pack()
    Label(pantalla2).pack()
    Label(pantalla2, text="EMAIL").pack()
    Label(pantalla2,text="").pack()
    email = Entry(pantalla2,width=100)
    email.pack()
    Label(pantalla2).pack()
    Label(pantalla2, text="TELEFONO O CELULAR").pack()
    Label(pantalla2,text="").pack()
    telefono = Entry(pantalla2,width=100)
    telefono.pack()
    Label(pantalla2).pack()
    Label(pantalla2, text="MES CUOTA").pack()
    Label(pantalla2,text="").pack()
    cuota = Entry(pantalla2,width=100)
    cuota.pack()
    Label(pantalla2,text="").pack()
    Label(pantalla2,text="").pack()
    Button(pantalla2, text = "REGISTRAR",command=inserta_datos).pack()
def inserta_datos():
    conexion1=pymysql.connect(host='localhost',
                                user='root',
                                passwd='',
                                db='bd3')
    cursor1=conexion1.cursor()
    sql="INSERT INTO clientes (nombre, apellido, dni,domicilio, email,telefono) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    datos=(nusuario2_ver.get(),contr2_ver.get(),dni2_ver.get(),domi2_ver.get(),email.get(),telefono.get(),cuota.get())
    
    try:
        cursor1.execute(sql,datos)
        conexion1.commit()
        messagebox.showinfo("AVISO","REGISTRO EXITOSO")
        
    except:
        conexion1.rollback()
        messagebox.showinfo("AVISO","NO REGISTRADO")
    conexion1.close()

