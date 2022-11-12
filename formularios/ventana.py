
from tkinter import *
from tkinter import ttk

from tkinter import messagebox
import formularios.countries

class Ventana(Frame):
    
    paises = formularios.countries.Countries()
        
    def __init__(self, master=None):
        super().__init__(master,width=1000, height=600)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenaDatos()
        self.habilitarCajas("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id=-1      
                   
    def habilitarCajas(self,estado):
        self.txtISO3.configure(state=estado)
        self.txtCapital.configure(state=estado)
        self.txtCurrency.configure(state=estado)
        self.txtName.configure(state=estado)
        
    def habilitarBtnOper(self,estado):
                        
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
        
    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)                
        self.btnCancelar.configure(state=estado)                
        
    def limpiarCajas(self):
        self.txtCapital.delete(0,END)
        self.txtCapital2.delete(0,END)
        self.txtCapital3.delete(0,END)
        self.txtCapital4.delete(0,END)
        self.txtCurrency.delete(0,END)
        self.txtISO3.delete(0,END)
        self.txtName.delete(0,END)
        
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
                
    def llenaDatos(self):
        datos = self.paises.consulta_paises()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],row[7]))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )
            
    def fNuevo(self):         
        self.habilitarCajas("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()        
        self.txtISO3.focus()
    
    def fGuardar(self): 
        if self.id ==-1:       
            self.paises.inserta_pais(self.txtISO3.get(),self.txtName.get(),self.txtCapital.get(),self.txtCapital2.get(),self.txtCapital3.get(),self.txtCapital4.get(),self.txtCurrency.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.paises.modifica_pais(self.id,self.txtISO3.get(),self.txtName.get(),self.txtCapital.get(),self.txtCapital2.get(),self.txtCapital3.get(),self.txtCapital4.get(),self.txtCurrency.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiaGrid()
        self.llenaDatos() 
        self.limpiarCajas() 
        self.habilitarBtnGuardar("disabled")      
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")
                    
    def fModificar(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave  
            self.habilitarCajas("normal")                         
            valores = self.grid.item(selected,'values')
            self.limpiarCajas()            
            self.txtISO3.insert(0,valores[0])
            self.txtName.insert(0,valores[1])
            self.txtCapital.insert(0,valores[2])
            self.txtCapital2.insert(0,valores[3])
            self.txtCapital3.insert(0,valores[4])
            self.txtCapital4.insert(0,valores[5])
            self.txtCurrency.insert(0,valores[6])            
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtISO3.focus()
                                        
    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.paises.elimina_pais(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def fCancelar(self):
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93, height=600)        
           
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)        
        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=0,width=150, height=600)                        
        lbl1 = Label(frame2,text="NOMBRE ")
        lbl1.place(x=3,y=5)        
        #self.txtISO3=Entry(frame2,textvariable = self.ISO3)
        self.txtISO3=Entry(frame2)
        self.txtISO3.place(x=3,y=25,width=50, height=20)                
        lbl2 = Label(frame2,text="APELLIDO ")
        lbl2.place(x=3,y=55)        
        self.txtName=Entry(frame2)
        self.txtName.place(x=3,y=75,width=100, height=20)        
        lbl3 = Label(frame2,text="DNI ")
        lbl3.place(x=3,y=105)        
        self.txtCapital=Entry(frame2)
        self.txtCapital.place(x=3,y=125,width=100, height=20)        
        lbl4 = Label(frame2,text="DOMICILIO")
        lbl4.place(x=3,y=155)   
        self.txtCapital2=Entry(frame2)
        self.txtCapital2.place(x=3,y=175,width=100, height=20)        
        lbl5 = Label(frame2,text="EMAIL")
        lbl5.place(x=3,y=200)
        self.txtCapital3=Entry(frame2)
        self.txtCapital3.place(x=3,y=225,width=100, height=20)        
        lbl6 = Label(frame2,text="TELEFONO")
        lbl6.place(x=3,y=250)
        self.txtCapital4=Entry(frame2)
        self.txtCapital4.place(x=3,y=275,width=100, height=20)        
        lbl7 = Label(frame2,text="MES CUOTA")
        lbl7.place(x=3,y=300)     
        self.txtCurrency=Entry(frame2)
        self.txtCurrency.place(x=3,y=325,width=50, height=20)        
        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10,y=375,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=375,width=60, height=30)         
        frame3 = Frame(self,bg="yellow" )
        frame3.place(x=247,y=0,width=800, height=600)                      
        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4","col5","col6","col7"))        
        self.grid.column("#0",width=60)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)
        self.grid.column("col5",width=90, anchor=CENTER)
        self.grid.column("col6",width=90, anchor=CENTER)
        self.grid.column("col7",width=90, anchor=CENTER)  
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="NOMBRE", anchor=CENTER)
        self.grid.heading("col2", text="APELLIDO", anchor=CENTER)
        self.grid.heading("col3", text="DNI", anchor=CENTER)
        self.grid.heading("col4", text="DOMICILIO", anchor=CENTER)   
        self.grid.heading("col5", text="EMAIL", anchor=CENTER)
        self.grid.heading("col6", text="TELEFONO", anchor=CENTER)
        self.grid.heading("col7", text="MES CUOTA", anchor=CENTER)             
        self.grid.pack(side=LEFT,fill = Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'        