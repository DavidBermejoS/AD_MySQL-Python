

"""
DESPIECE
:see En esta clase guarda la estructura para crear objetos despiece

:author David Bermejo
"""

class Despiece:
    def __init__(self, c1, c2, cantidad):
        self.c1 = c1
        self.c2 = c2
        self.cantidad = cantidad

    def __str__(self):
        return f"Despiece:\n\t Codigo Almacen 1: {self.c1}\n\t Codigo Almacen 2: {self.c2}\n\t Cantidad: {self.cantidad}"
