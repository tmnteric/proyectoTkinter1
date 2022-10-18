from logica.conexion import conectar
from modelo.producto import ProductoModel

class ProductoLogica:
    
    def listar(self):
        sql ='SELECT * FROM producto ORDER BY codigo asc'
        db = conectar()
        cursor = db.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall() # fetchall trae los resultados de una consulta, lo devuelve como una lista de tuplas
        db.close()
        
        salida = []
        for dato in resultado:
            # primera forma de realizarlo
            #producto = ProductoModel()
            #producto.setCodigo(dato[0])
            #producto.setNombre(dato[1])
            #producto.setPrecio(dato[2])
            
            #segunda forma de realizarlo
            producto = ProductoModel(dato[0], dato[1], dato[2])
            salida.append(producto)
        
        return salida
    
    def insertar(self, producto: ProductoModel):
        sql = 'INSERT INTO producto (nombre, precio) VALUES ("%s", %f)' % (producto.getNombre(), producto.getPrecio())
        # %s = str
        # %f = float
        # %d = int
        db = conectar()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
        pass
    
    def actualizar(self, producto: ProductoModel):
        sql = f'UPDATE producto SET nombre = "%s", precio = %f WHERE codigo = %d' %(producto.getNombre(), producto.getPrecio(), producto.getCodigo())
        db = conectar()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()

    
    def eliminar(self, codigo: int):
        sql = 'DELETE FROM producto WHERE codigo = %d '%(codigo)
        db = conectar()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()