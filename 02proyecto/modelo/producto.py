class ProductoModel:
    def __init__(self, codigo=None, nombre=None, precio=None):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    
    def getCodigo(self):
        return self.__codigo
    
    def setCodigo(self, codigo):
        self.__codigo = codigo
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, precio):
        self.__precio = precio