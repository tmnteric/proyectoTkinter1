import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from logica.producto import ProductoLogica
from modelo.producto import ProductoModel

class ProdcutoVista(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.__logica = ProductoLogica()
        
        self.geometry('640x480')
        self.title('Productos')
        self.iconbitmap('02proyecto/producto.ico')
        
        self.columnconfigure(0 ,weight=2)
        self.columnconfigure(1, weight=1)
        
        izquierda =tk.Frame(self)
        self.__construirFrameIzquierdo(izquierda)
        izquierda.grid(column=0, row=0, )
        
        derecha = tk.Frame(self)
        self.__construirFrameDerecho(derecha)
        derecha.grid(column=1, row=0)
        
        self.__cargarTabla()
    
    def __construirFrameIzquierdo(self, frame):
        
        self.__tabla = ttk.Treeview(frame)
        self.__tabla.grid(column=0, row=0, columnspan=2)
        self.__tabla['columns'] = ('Código', 'Nombre', 'Precio')
        
        self.__tabla.heading('#0', text="", anchor=tk.CENTER)
        self.__tabla.heading('Código', text='Código', anchor=tk.CENTER)
        self.__tabla.heading('Nombre', text='Nombre', anchor=tk.CENTER)
        self.__tabla.heading('Precio', text='Precio', anchor=tk.CENTER)
        
        self.__tabla.column('#0', width=0, stretch=tk.NO) 
        self.__tabla.column('Código', anchor =tk.E, width=80 )
        self.__tabla.column('Nombre', anchor=tk.W, width=250)
        self.__tabla.column('Precio',anchor=tk.E, width=80)
        
        def selecionar_elemento(event):
            for item_selected in self.__tabla.selection():
                item = self.__tabla.item(item_selected)
                self.__codigo.set(item['values'][0])
                self.__nombre.set(item['values'][1])
                self.__precio.set(item['values'][2])

        self.__tabla.bind('<<TreeviewSelect>>', selecionar_elemento)
        
        def nuevo():
            #TODO limpiar la seleccion de la tabla
            self.__codigo.set(0)
            self.__nombre.set("")
            self.__precio.set(0.0)
        
        boton1 = ttk.Button(frame, text='Nuevo', command=nuevo)
        boton1.grid(column=0, row=1)
        
        def eliminar():
            opcion = tk.messagebox.askquestion('Eliminar producto', 'Esta seguro en eliminar el producto')
            
            if opcion == 'yes':
                #TODO seleccionar el codigo del elemento seleccionado en la tabla
                codigo = int(self.__codigo.get())
                # Enviar a eliminar el producto con ese id
                self.__logica.eliminar(codigo)
                messagebox.showinfo('Eliminar producto', 'Se ha elimado el producto')
                self.__cargarTabla()
                
        boton2 = ttk.Button(frame, text='Eliminar', command=eliminar)
        boton2.grid(column=1, row=1)
    
    def __construirFrameDerecho(self, frame):
        
        ttk.Label(frame, text='Datos del produto').grid(column=0, row=0, columnspan=2)
        ttk.Label(frame, text='Código').grid(column=0,row=1)
        self.__codigo = tk.IntVar()#indica que los datos que le entran por el Entry queden guardados en la variable
        ttk.Entry(frame, textvariable=self.__codigo).grid(column=1,row=1)  
        ttk.Label(frame, text='Nombre').grid(column=0, row=2)
        self.__nombre = tk.StringVar()
        ttk.Entry(frame, textvariable=self.__nombre).grid(column=1,row=2)
        ttk.Label(frame,text='Precio').grid(column=0,row=3)
        self.__precio= tk.DoubleVar()
        ttk.Entry(frame, textvariable=self.__precio).grid(column=1,row=3)
        
        def insertar():
            #TODO calidar que los campos esten llenos
            producto = ProductoModel()
            producto.setNombre(self.__nombre.get())
            producto.setPrecio(self.__precio.get())
            
            #Envio a guardar a la base de 
            try:
                self.__logica.insertar(producto)
                self.__cargarTabla()
                messagebox.showinfo('Guardado de producto', 'Guardado exitosamente')
            except Exception as e:
                messagebox.showerror('Guardado de producto', 'Error al guardar el producto', e)
            
        boton1 = ttk.Button(frame,text='Insertar', command=insertar).grid(column=0,row=4)
        def actualizar():
            #TODO calidar que los campos esten llenos
            producto = ProductoModel()
            producto.setCodigo(self.__codigo.get())
            producto.setNombre(self.__nombre.get())
            producto.setPrecio(self.__precio.get())
            
            #Envio a guardar a la base de datos
            try:
                self.__logica.actualizar(producto)
                self.__cargarTabla()
                messagebox.showinfo('Actualizar producto', 'Se actualizo de forma correcta')
            except Exception as e:
                messagebox.showerror('Actualizar producto', 'Error al actualizar el producto',e)
            
        boton2 = ttk.Button(frame,text='Actualizar', command=actualizar).grid(column=1,row=4)
    
    def __cargarTabla(self):
        productos = self.__logica.listar()
        
        #Eliminar los valores anteriores
        for item in self.__tabla.get_children(''):
            
            self.__tabla.delete(item)
        
        for i in productos:
            identicador = i.getCodigo()
            self.__tabla.insert(parent= '', index=identicador, iid=identicador, text='', values=(identicador, i.getNombre(), i.getPrecio()))

    def iniciarEjecucion(self):
        self.mainloop()
    
