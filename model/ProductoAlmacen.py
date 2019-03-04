"""
PRODUCTO ALMACEN
En esta clase guarda la estructura para crear objetos productos de los almacenes 1 y 2

:author David Bermejo
"""


class ProductoAlmacen:

    def __init__(self, codigo:str, cantidad:int, descripcion:str):
        self.codigo = codigo
        self.cantidad = cantidad
        self.descripcion = descripcion

    def setValues(self,res):
        self.codigo = res[0]
        self.cantidad=res[1]
        self.descripcion=res[2]

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_codigo(self):
        return self.codigo

    def get_cantidad(self):
        return self.cantidad

    def __str__(self):
        return f"PRODUCTO\n\t Codigo: {self.codigo}\n\t Descripcion: {self.descripcion}\n\t Cantidad: {self.cantidad} "
