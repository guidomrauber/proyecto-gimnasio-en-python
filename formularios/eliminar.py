import tkinter 
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
import formularios.countries
from formularios.countries import *
def mostrar():
    global paises
    paises=formularios.countries.Countries()
    global pantalla1
    pantalla1 = tk.Tk()
    pantalla1.geometry("300x300")
    pantalla1.title("ELIMINAR REGISTRO")
    pantalla1.iconbitmap("images.ico")
    
    Label(pantalla1,text="").pack()
    Label(pantalla1,text="").pack()
    Label(pantalla1, text="INGRESE DNI A ACTUALIZAR",fg="navy",width="100",height="1", font=("calibri", 15)).pack()
    Label(pantalla1,text="").pack()

    nusuario_ver=StringVar()
    contr_ver=StringVar()

    global nusuario_entrar
    
    Label(pantalla1).pack()
    Label(pantalla1, text="DNI Nº").pack()
    Label(pantalla1,text="").pack()
    nusuario_entrar= Entry(pantalla1)
    nusuario_entrar.pack()
    Label(pantalla1).pack()

    

    Button(pantalla1, text = "CONSULTA", command=consulta_datos).pack()
      
        
def validacion_datos():
    
    
    global result 
    
    result=modificacion(contr_entrar,nusuario_entrar)

    if result==1:
            messagebox.showinfo("Información", "Se modificó el artículo")
    else:
            messagebox.showinfo("Información", "No existe un artículo con dicho código")

def modificacion(contr_entrar,nusuario_entrar):
        datos2=(contr_entrar.get(),nusuario_entrar.get())
        conexion1=pymysql.connect(host='localhost',
                                user='root',
                                passwd='',
                                db='bd3')
        
        cursor1=conexion1.cursor()
        
        sql="update clientes set cuota=%s where dni=%s"
        cursor1.execute(sql, datos2)
        conexion1.commit()
        conexion1.close()
        return cursor1.rowcount # retornamos la cantidad de filas modificadas
def consulta_datos():
    conexion1=pymysql.connect(host='localhost',
                                user='root',
                                passwd='',
                                db='bd3')
    cursor1=conexion1.cursor()
    sql="select * from clientes where dni=%s "
    datos=(nusuario_entrar.get())
    global result 
    result=cursor1.execute(sql,datos)
    personas=cursor1.fetchall()
    self=""
    if (result)>0:
        for i in personas:
            n=i[7]
                        
            pantalla2 = tk.Tk()
            pantalla2.geometry("300x300")
            pantalla2.title("CONSULTA POR DNI")
            pantalla2.iconbitmap("images.ico")
            global contr_entrar
            Label(pantalla2,text="").pack()
            Label(pantalla2,text="").pack()
            Label(pantalla2, text="SU ULTIMA CUOTA PAGADA ES ",fg="navy",width="100",height="1", font=("calibri", 15)).pack()
            Label(pantalla2,text="").pack()
            Label(pantalla2,text=n,fg="navy",width="100",height="1", font=("calibri", 35)).pack()
            contr_entrar= Entry(pantalla2)
            contr_entrar.pack()
            Label(pantalla2).pack()
            Button(pantalla2, text = "ACTUALIZAR MES", command=validacion_datos).pack()
       
    else:
            messagebox.showinfo("Información", "USUARIO Y CONTRASEÑA INCORRECTO")
    conexion1.close()
     
    