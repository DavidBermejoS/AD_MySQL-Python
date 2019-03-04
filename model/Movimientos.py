
"""
MOVIMIENTOS

:note En esta clase guarda la estructura para crear objetos de movimiento entre un almacen y otro

:author David Bermejo
"""

class Movimientos:
    def __init__(self, cod_movimiento, fecha, cod_articulo, cantidad):
        self.fecha = fecha
        self.cod_articulo = cod_articulo
        self.cantidad = cantidad

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_codigo_producto(self,codigo_producto):
        self.codigo_producto = codigo_producto

    def set_cantidad(self,cantidad):
        self.cantidad = cantidad

    def get_cod_movimiento(self,cod_movimiento):
        return self.cod_movimiento

    def __str__(self):
        return f"Movimiento: {self.cod_movimiento}\n\t Fecha: {self.fecha}\n\t Codigo: {self.codigo} \n\t Cantidad: {self.cantidad}"
