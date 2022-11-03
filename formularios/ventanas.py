#IMPORTAMOS "tkinter"
from tkinter import *
import tkinter
from tkinter import ttk


def saludo():
    nombre = StringVar()
    
    print("Hola ",nombre.get())

def suma5():
    numero = IntVar()
    resultado=numero.get()+5
    print("RESULTADO: ",resultado)

def resta5():
    numero = IntVar()
    resultado=numero.get()-5
    print("RESULTADO: ",resultado)

def multi5():
    numero = IntVar()
    resultado=numero.get()*5
    print("RESULTADO: ",resultado)

def divid5():
    numero = IntVar()
    resultado=numero.get()/5
    print("RESULTADO: ",resultado)

#VENTANA PRINCIPAL.
def ventanas():
    global root
    root = tkinter.Tk()
    root.title("MANTENIMIENTO DE CLIENTES DEL GIMNASIO")
    root.geometry("1280x720")
    root.iconbitmap("images.ico")
    nombre = StringVar()
    apellido=StringVar()
    numero = IntVar()
    
#INCLUIMOS PANEL PARA LAS PESTAÑAS.
    nb = ttk.Notebook(root)
    nb.pack(fill='both',expand='yes')

#CREAMOS PESTAÑAS
    p1 = ttk.Frame(nb)
    p2 = ttk.Frame(nb)
    p3 = ttk.Frame(nb)
    p4 = ttk.Frame(nb)
    p5 = ttk.Frame(nb)

#ELEMENTOS PESTAÑA registro
    Label(p1, text="Nombre").place(x=50, y=50)
    Entry(p1, textvariable=nombre).place(x=190,y=50,width=200)
    Label(p1, text="Apellido").place(x=50, y=80)
    Entry(p1, textvariable=apellido).place(x=190,y=80,width=200)
    Label(p1, text="DNI Nº").place(x=50, y=110)
    dni=IntVar
    Entry(p1, textvariable=dni).place(x=190,y=110,width=200)
    Label(p1, text="Domicilio").place(x=50, y=140)
    domicilio=StringVar
    Entry(p1, textvariable=domicilio).place(x=190,y=140,width=200)
    Label(p1, text="Email").place(x=50, y=170)
    email=StringVar
    Entry(p1, textvariable=email).place(x=190,y=170,width=200)
    Label(p1, text="Telefono").place(x=50, y=200)
    telefono=StringVar
    Entry(p1, textvariable=telefono).place(x=190,y=200,width=200)
    Label(p1, text="Mes de cuota").place(x=50, y=230)
    cuota=StringVar
    Entry(p1, textvariable=cuota).place(x=190,y=230,width=200)
    
    Button(p1, text='REGISTRAR',bg='light blue',command=saludo).place(x=225,y=330)
    
#ELEMENTOS PESTAÑA Suma5.
    Button(p2, text='Suma5',bg='light blue',command=suma5).place(x=225,y=160)
    Entry(p2, textvariable=numero).place(x=190,y=70)
#ELEMENTOS PESTAÑA Resta5.
    Button(p3, text='Resta5',bg='light blue',command=resta5).place(x=225,y=160)
    Entry(p3, textvariable=numero).place(x=190,y=70)
#ELEMENTOS PESTAÑA Multi5.
    Button(p4, text='Multi5',bg='light blue',command=multi5).place(x=225,y=160)
    Entry(p4, textvariable=numero).place(x=190,y=70)
#ELEMENTOS PESTAÑA Divid5.
    Button(p5, text='Divid5',bg='light blue',command=divid5).place(x=225,y=160)
    Entry(p5, textvariable=numero).place(x=190,y=70)

#AGREGAMOS PESTAÑAS CREADAS
    nb.add(p1,text='REGISTRO DE CLIENTES')
    nb.add(p2,text='      CONSULTA POR NUMERO DE CLIENTE ')
    nb.add(p3,text='      LISTADO COMPLETO DE CLIENTES')
    nb.add(p4,text='      ELIMINAR CLIENTE')
    nb.add(p5,text='      MODIFICAR O ACTUALIZAR CLIENTE')

    
