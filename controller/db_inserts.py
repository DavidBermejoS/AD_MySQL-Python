"""
INSERCIÓN DE MOVIMIENTOS
:note Esta clase gestiona el ingreso de nuevos movimientos de materiales
        a producción. Como parte de ese mismo movimiento, descontará los mate-
        riales necesarios para su producción del almacén 1.
:autor David Bermejo Simon
"""
import mysql.connector

from ProductoAlmacen import ProductoAlmacen


class DBInsertMovement:

    def insertar_movimiento(self):
        print("Inserta el codigo de producto que desee producir: ")
        materials = []
        codigo = input()
        res = self.getColumnAndCode("despiece", "C2")
        if res is not None:
            for row in res:
                materials += [row[1], row[2]]
            print(materials)
        else:
            print("---Cancelando operación de movimiento a producción---")
    def insertar_almacen1(self):
        db = mysql.connector.connect(
            host="localhost",
            database="db_sge",
            user="root",
            password=""
        )
        res, codigo = self.getColumnAndCode("almacen1", "codigo")
        if res is not None:
            cantidad = self.obtener_cantidad()
            cursor = db.cursor()
            cursor.execute("""
               UPDATE almacen1
               SET cantidad=cantidad+%s
               WHERE codigo=%s
            """, (cantidad, codigo))
            db.commit()
            db.close()
            print("---Cantidad introducida correctamente---")
        else:
            print("---No se ha encontrado el codigo introducido, volviendo al menú principal---")
    def getColumnAndCode(tabla, column):
        db = mysql.connector.connect(
            host="localhost",
            database="db_sge",
            user="root",
            password=""
        )
        print("---Introduce el codigo del material del que quieras introducir más unidades---")
        codigo = input()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM " + tabla + " WHERE " + column + "='" + codigo + "'")
        res = list(cursor)
        if len(res) == 0:
            print("Lo siento, ese codigo no se encuentra en la tabla ",tabla)
            return None, codigo
        else:
            product = ProductoAlmacen()
            product.setValues(res[0])
            print(product)
            return res, codigo
    def obtener_cantidad():
        print("---¿Cuantas unidades desea ingresar?---")
        cantidad = int(input())
        return cantidad
