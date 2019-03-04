"""
INTERFAZ DE CONTROL

:note Esta clase controlara el flujo del usuario a través del programa
:post Se intentará implementar una interfaz gráfica con tkinter
:autor David Bermejo Simon
"""

from controller.db_inserts import DBInsertMovement as dbInsert
from controller.db_query import DBQuery as dbQuery


class Interfaz:

    def interfaz_consultas(self):
        while True:
            print("\n----------------------------------------")
            print("\t Selecciona una opción: ")
            print("\t1) Ver todos los registros del Almacén de Materiales(almacén1)")
            print("\t2) buscar en el 1º Almacen por codigo")
            print("\t3) Ver todos los registros del Almacén de Producción (almacen 2)")
            print("\t4) buscar en el 2º Almacen por codigo")
            print("\t*) Salir del menú de consultas")
            print("----------------------------------------\n")

            selector = input()
            if selector == '1':
                print("\n---Mostrando todos los productos del 1º Almacen---")
                dbQuery.ver_todo_almacen1()
            if selector == '2':
                print("\n---Buscando producto por código en el 1º Almacen---")
                dbQuery.ver_cod_almacen1()
            if selector == '3':
                print("\n---Mostrando todos los productos del 2º Almacen---")
                dbQuery.ver_todo_almacen2()
            if selector == '4':
                print("\n---Buscando producto por código en el 2º Almacen---")
                dbQuery.ver_cod_almacen2()
            if selector == '*':
                print("---Saliendo del submenu---")
                break

    def interfaz_main(self):
        while True:
            print("\n----------------------------------------")
            print("\t Selecciona una opción ")
            print("\t1) Realizar un movimiento (Producir Bicicleta en el almacen 2)")
            print("\t2) Anular un movimiento(Esto insertará uno nuevo con sus cantidades negativas)")
            print("\t3) Insertar materiales en el Almacen 1 (Almacen de materiales)")
            print("\t4) Consultar registros")
            print("\t*) Salir del programa")
            print("----------------------------------------\n")
            selector = input()
            if selector == '1':
                print("INSERTANDO NUEVO MOVIMIENTO")
                dbInsert.insertar_movimiento()
            if selector == '2':
                print("Opcion 2")
            if selector == '3':
                print("INSERTANDO MATERIALES EN EL ALMACEN 1")
                dbInsert.insertar_almacen1(dbInsert)
            if selector == '4':
                print("---MOSTRANDO OPCIONES DE CONSULTAS---")
                self.interfaz_consultas()
            if selector == '*':
                print("---Saliendo del programa---")
                break;



aux= Interfaz()
aux.interfaz_main()