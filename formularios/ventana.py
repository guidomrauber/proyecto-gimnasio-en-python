from tkinter import *
from tkinter import ttk


    

class Ventana(Frame):
       
    def __init__(self, master=None):
        super().__init__(master,width=1280, height=720)
        self.master = master
        self.pack()
        self.create_widgets()
        
    def fNuevo(self):         
        pass
    
    def fGuardar(self):        
        pass
                 
    def fModificar(self):        
        pass
    
    def fEliminar(self):
        pass

    def fCancelar(self):
        pass

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=100, height=720)        
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)        
        
        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5","col6","col7"))        
        self.grid.column("#0",width=20)
        self.grid.column("col1",width=40, anchor=CENTER)
        self.grid.column("col2",width=80, anchor=CENTER)
        self.grid.column("col3",width=80, anchor=CENTER)
        self.grid.column("col4",width=80, anchor=CENTER)   
        self.grid.column("col5",width=80, anchor=CENTER)
        self.grid.column("col6",width=80, anchor=CENTER)
        self.grid.column("col7",width=20, anchor=CENTER)    
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="NOMBRE", anchor=CENTER)
        self.grid.heading("col2", text="APELLIDO", anchor=CENTER)
        self.grid.heading("col3", text="DNI", anchor=CENTER)
        self.grid.heading("col4", text="DOMICILIO", anchor=CENTER)     
        self.grid.heading("col5", text="EMAIL", anchor=CENTER)
        self.grid.heading("col6", text="TELEFONO", anchor=CENTER)
        self.grid.heading("col7", text="CUOTA", anchor=CENTER)   
        self.grid.place(x=101,y=0,width=1179, height=720)
        
        
        
        
        
        