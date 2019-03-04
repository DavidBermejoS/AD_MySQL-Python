
"""
MOVIMIENTOS

:note En esta clase guarda la estructura para crear objetos de movimiento entre un almacen y otro

:author David Bermejo
"""

class Movimientos:
    def __init__(self, cod_movimiento, fecha, cod_articulo, cantidad,nota):
        self.cod_mov = cod_movimiento
        self.fecha = fecha
        self.cod_articulo = cod_articulo
        self.cantidad = cantidad
        self.nota = nota

    def set_cod_movimiento(self,cod_mov):
        self.cod_mov = cod_mov

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_cod_articulo(self,cod_articulo):
        self.cod_articulo = cod_articulo

    def set_cantidad(self,cantidad):
        self.cantidad = cantidad

    def set_nota (self,nota):
        self.nota = nota

    def get_cod_movimiento(self,cod_movimiento):
        return self.cod_movimiento

    def __str__(self):
        return f"Movimiento: {self.cod_mov}\n\t Fecha: {self.fecha}\n\t Codigo: {self.cod_articulo} \n\t Cantidad: {self.cantidad} \n\t Nota: {self.nota}"
