"""
INSERCIÓN DE MOVIMIENTOS
:note Esta clase gestiona el ingreso de nuevos movimientos de materiales
        a producción. Como parte de ese mismo movimiento, descontará los mate-
        riales necesarios para su producción del almacén 1.
:autor David Bermejo Simon
"""
import mysql.connector

from model.ProductoAlmacen import ProductoAlmacen
from model.Movimientos import Movimientos


class DBInsertMovement:

    def create_connection(self):
        db = mysql.connector.connect(
            host="localhost",
            database="db_sge",
            user="root",
            password=""
        )
        return db

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
                self.alter_materials(self, materials,type=0)
                self.alter_product(self, codigo, cantidad_solicitada, type=0)
                self.insert_log_movement(self, codigo, cantidad_solicitada, type=0)
            else:
                print("\n---Cancelando operación de movimiento a producción---")
        else:
            print("\n[Lo siento, ese codigo no se encuentra en la tabla de despiece]")
            print("---Cancelando operación de movimiento a producción---")

    def check_codigo(self, codigo):
        db = self.create_connection(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM despiece WHERE C2='" + codigo + "'")
        res = cursor.fetchall()
        res_list = list(res)
        if len(res_list) == 0:
            return None
        else:
            db.close()
            return res

    def check_materials(self, codigo, cantidad):
        db = self.create_connection(self)
        cursor = db.cursor()
        cursor.execute("SELECT cantidad FROM almacen1 WHERE codigo='" + codigo + "'")
        res = cursor.fetchone()
        cantidad_exist = int(res[0])
        if cantidad_exist >= cantidad:
            return True
        else:
            return False
        db.close()

    def alter_materials(self, materials, type):
        db = self.create_connection(self)
        if type is 0:
            print("\n DESCONTANDO UNIDADES DEL ALMACEN DE MATERIALES (ALMACEN 1)")
        else:
            print("\n RECUPERANDO UNIDADES DEL ALMACEN DE MATERIALES (ALMACEN 1)")
        for product in materials:
            cursor = db.cursor()
            if type is 0:
                cursor.execute("UPDATE almacen1 SET cantidad = cantidad - %s WHERE codigo=%s ",
                               (product.cantidad, product.codigo))
                print(
                    "\t[Descontadas " + str(product.cantidad) + " unidades del material con codigo " + product.codigo +
                    " del almacen1]")
            else:
                cursor.execute("UPDATE almacen1 SET cantidad = cantidad + %s WHERE codigo=%s ",
                               (product.cantidad, product.codigo))
                print(
                    "\t[Introducidas " + str(product.cantidad) + " unidades del material con codigo " + product.codigo +
                    " del almacen1]")

            db.commit()
        db.close()

    def alter_product(self, codigo, cantidad, type):
        db = self.create_connection(self)
        cursor = db.cursor()
        if type is 0:
            print("\n PRODUCIENDO UNIDADES EN EL ALMACEN DE PRODUCCION(ALMACEN 2)")
            cursor.execute("UPDATE almacen2 SET cantidad = cantidad + %s WHERE codigo=%s ", (cantidad, codigo))
        else:
            print("\n SUBSTRAYENDO UNIDADES EN EL ALMACEN DE PRODUCCION(ALMACEN 2)")
            cursor.execute("UPDATE almacen2 SET cantidad = cantidad - %s WHERE codigo=%s ", (cantidad, codigo))
        print("\t[Producidas " + str(cantidad) + " unidades del producto con codigo " + codigo)
        db.commit()
        db.close()

    def insert_log_movement(self, codigo, cantidad,type):
        db = self.create_connection(self)
        cursor = db.cursor()
        if type is 0:
            cursor.execute("INSERT INTO movimientos VALUES(null,SYSDATE(),'" + codigo + "'," + str(cantidad) + ", null)")
        else:
            cursor.execute("INSERT INTO movimientos VALUES(null,SYSDATE(),'" + codigo + "'," +
                           str(cantidad*(-1)) + ", 'Arreglo movimiento "+codigo+"')")
        print("\nREGISTRANDO MOVIMIENTO EN LA TABLA DE LOG")
        print("\t[Registrado movimiento satisfactoriamente]")
        db.commit()
        db.close()

    def insertar_almacen1(self):
        db = self.create_connection(self)
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

    def anular_movimiento(self):
        materials = []
        print("---Introduce el codigo de movimiento que quieras deshacer:---")
        cod_mov = int(input())
        check_cod, movement = self.check_cod_mov(self, cod_mov)
        cantidad_solicitada = movement.cantidad
        if check_cod is True:
            res = self.check_codigo(self, movement.cod_articulo)
            for row in res:
                product = ProductoAlmacen(row[1], row[2] * cantidad_solicitada, None)
                materials.append(product)
            self.alter_materials(self, materials, type=1)
            self.alter_product(self, movement.cod_articulo, movement.cantidad, type=1)
            self.insert_log_movement(self, movement.cod_articulo, movement.cantidad, type=1)
        else:
            print("[Lo siento, no se ha encontrado ningun movimiento con ese codigo]")

    def check_cod_mov(self, cod_mov):
        db = self.create_connection(self)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movimientos WHERE cod_movimiento=" + str(cod_mov))
        res = cursor.fetchone()
        res_list = list(res)
        if len(res_list) > 0 and res_list[4] is None:
            movement = Movimientos(res_list[0], res_list[1], res_list[2], res_list[3], res_list[4])
            return True, movement
        else:
            return False, None
