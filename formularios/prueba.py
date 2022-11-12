import tkinter as tk
import tkinter as ttk
from tkinter import Label, scrolledtext as st
import pymysql   




def recuperar_todos():
        conexion1=pymysql.connect(host='localhost',
                                user='root',
                                passwd='',
                                db='bd3')
        cursor1=conexion1.cursor()
        sql="select nombre,apellido,dni,domicilio,email,telefono,cuota from clientes"
        cursor1.execute(sql)
        
        conexion1.close()
def Listado():
    scrolledtext1=st.ScrolledText(pantalla4, width=100, height=10)
    result=recuperar_todos()
    scrolledtext1.delete("1.0", tk.END)        
    for fila in result:
            scrolledtext1.insert(tk.END, "nombre:"+str(fila[0])+
                                              "\napellido:"+fila[1]+
                                              "\ndni"+str(fila[2])+
                                              "\ndomicilio:"+fila[3]+
                                              "\nemail:"+fila[4]+
                                              "\ntelefono:"+fila[5]+
                                              "\ncuota:"+str(fila[6])+"\n\n")
global pantalla4
pantalla4 = tk.Tk()
pantalla4.geometry("1280x720")
pantalla4.title("BIENVENIDOS")
pantalla4.iconbitmap("images.ico")
root = tk.Tk()
root.wm_title("Crud Python MySQL")
       

labelframe3=ttk.LabelFrame(pantalla4, text="LISTADO DE CLIENTES")  
labelframe3.grid(column=0, row=0, padx=5, pady=10)
boton1=ttk.Button(labelframe3, text="LISTADO COMPLETO DE CLIENTES", command=Listado)
boton1.grid(column=0, row=0, padx=4, pady=4)
scrolledtext1=st.ScrolledText(labelframe3, width=100, height=10)
scrolledtext1.grid(column=0,row=1, padx=10, pady=10)    


pantalla4.mainloop()