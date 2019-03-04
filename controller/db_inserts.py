"""
INSERCIÓN DE MOVIMIENTOS
:note Esta clase gestiona el ingreso de nuevos movimientos de materiales
        a producción. Como parte de ese mismo movimiento, descontará los mate-
        riales necesarios para su producción del almacén 1.
:autor David Bermejo Simon
"""
import mysql.connector

from model.ProductoAlmacen import ProductoAlmacen


class DBInsertMovement:

    def insertar_movimiento(self):
        print("Inserta el codigo de producto que desee producir (Debe existir en la tabla de despiece): ")
        codigo = input()
        print("Inserta la cntidad que quieres producir:")
        cantidad_solicitada = int(input())
        make_movement = True

        materials = []
        res = self.check_codigo(self, codigo)
        if res is not None:
            for row in res:
                if self.check_materials(self, row[1], row[2] * cantidad_solicitada) is True:
                    product = ProductoAlmacen(row[1], row[2] * cantidad_solicitada, None)
                    materials.append(product)
                else:
                    print("\n[Lo siento, no hay suficiente cantidad del material con codigo " + row[1] + "]")
                    make_movement = False

            if make_movement is True:
                self.discount_materials(self, materials)
                self.produce_product(self, codigo, cantidad_solicitada)
                self.insert_log_movement(self, codigo, cantidad_solicitada)
            else:
                print("\n---Cancelando operación de movimiento a producción---")
        else:
            print("\n[Lo siento, ese codigo no se encuentra en la tabla de despiece]")
            print("---Cancelando operación de movimiento a producción---")

    def check_materials(self, codigo, cantidad):
        db = mysql.connector.connect(
            host="localhost",
            database="db_sge",
            user="root",
            password=""
        )
        cursor = db.cursor()
        cursor.execute("SELECT cantidad FROM almacen1 WHERE codigo='" + codigo + "'")
        res = cursor.fetchone()
        cantidad_exist = int(res[0])
        if cantidad_exist >= cantidad:
            return True
        else:
            return False
        db.close()

    def discount_materials(self, materials):
        db = mysql.connector.connect(
            host="localhost",
            database="db_sge",
            user="root",
            password=""
        )
        print("\n DESCONTANDO UNIDADES DEL ALMACEN DE MATERIALES (ALMACEN 1)")
        for product in materials:
            cursor = db.cursor()
            cursor.execute("UPDATE almacen1 SET cantidad = cantidad - %s WHERE codigo=%s ",
                           (product.cantidad, product.codigo))
            print("\t[Descontadas " + str(product.cantidad) + " unidades del material con codigo " + product.codigo +
                  " del almacen1]")
            db.commit()
        db.close()

    def produce_product(self, codigo, cantidad):
        db = mysql.connector.connect(
            host="localhost",
            database="db_sge",
            user="root",
            password=""
        )
        cursor = db.cursor()
        print("\n PRODUCIENDO UNIDADES EN EL ALMACEN DE PRODUCCION(ALMACEN 2)")
        cursor.execute("UPDATE almacen2 SET cantidad = cantidad + %s WHERE codigo=%s ", (cantidad, codigo))
        print("\t[Producidas " + str(cantidad) + " unidades del producto con codigo " + codigo)
        db.commit()
        db.close()

    def insert_log_movement(self, codigo, cantidad):
        db = mysql.connector.connect(
            host="localhost",
            database="db_sge",
            user="root",
            password=""
        )
        cursor = db.cursor()
        cursor.execute("INSERT INTO movimientos VALUES(null,SYSDATE(),'"+codigo+"',"+str(cantidad)+")")
        print("\nREGISTRANDO MOVIMIENTO EN LA TABLA DE LOG")
        print("\t[Registrado movimiento satisfactoriamente]")
        db.commit()
        db.close()

    def insertar_almacen1(self):
        db = mysql.connector.connect(
            host="localhost",
            database="db_sge",
            user="root",
            password=""
        )
        print("---Introduce el codigo del material del que quieras introducir más unidades---")
        codigo = input()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM almacen1 WHERE codigo='" + codigo + "'")
        res = list(cursor)
        if res is not None:
            print("---¿Cuantas unidades desea ingresar?---")
            cantidad = int(input())
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
        db.close()

    def check_codigo(self, codigo):
        db = mysql.connector.connect(
            host="localhost",
            database="db_sge",
            user="root",
            password=""
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM despiece WHERE C2='" + codigo + "'")
        res = cursor.fetchall()
        res_list = list(res)
        if len(res_list) == 0:
            return None
        else:
            db.close()
            return res
