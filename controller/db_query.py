
"""
CONSULTAS CON LA BASE DE DATOS

:note Esta clase gestiona las consultas que se realizarán a la
        base de datos
:autor David Bermejo Simon
"""
import mysql.connector
from ProductoAlmacen import ProductoAlmacen
"""   
La conexion a la base de datos la realizaremos así:
    
db = mysql.connector.connect(
        host="localhost",
        database="db_sge",
        user="root",
        password=""
        )
"""


class DBQuery:
    
    def ver_todo_almacen1():
        db = mysql.connector.connect(
                host="localhost",
                database="db_sge",
                user="root",
                password=""
                )
        sql = "SELECT * FROM almacen1"
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            for row in res:
                pAux = ProductoAlmacen(row[0],row[1],row[2])
                print("\n____________________________________________")
                print(pAux)
                print("____________________________________________\n")
            db.commit()
        except:
            db.rollback()
        db.close()



    def ver_cod_almacen1():
        db = mysql.connector.connect(
                host="localhost",
                database="db_sge",
                user="root",
                password=""
                )
        print("\t INTRODUCE EL CODIGO DEL PRODUCTO QUE QUIERAS BUSCAR: ")
        codUser = input()
        sql = "SELECT * FROM almacen1 WHERE codigo='"+codUser+"'"
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            if len(res) == 0:
                print("\n--- No se han encontrado resultados ---")
            for row in res:    
                pAux = ProductoAlmacen(row[0],row[1],row[2])
                print("\n____________________________________________")
                print(pAux)
                print("____________________________________________\n")
            db.commit()
        except:
            print("Error en la base de datos")
            db.rollback()
        db.close()
        
    def ver_todo_almacen2():
        db = mysql.connector.connect(
                host="localhost",
                database="db_sge",
                user="root",
                password=""
                )
        sql = "SELECT * FROM almacen2"
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            for row in res:
                pAux = ProductoAlmacen(row[0],row[1],row[2])
                print("\n____________________________________________")
                print(pAux)
                print("____________________________________________\n")
            db.commit()
        except:
            db.rollback()
        db.close()



    def ver_cod_almacen2():
        db = mysql.connector.connect(
                host="localhost",
                database="db_sge",
                user="root",
                password=""
                )
        print("\t INTRODUCE EL CODIGO DEL PRODUCTO QUE QUIERAS BUSCAR: ")
        codUser = input()
        sql = "SELECT * FROM almacen2 WHERE codigo='"+codUser+"'"
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            if len(res) == 0:
                print("\n--- No se han encontrado resultados ---")
            for row in res:    
                pAux = ProductoAlmacen(row[0],row[1],row[2])
                print("\n____________________________________________")
                print(pAux)
                print("____________________________________________\n")
            db.commit()
        except:
            print("Error en la base de datos")
            db.rollback()
        db.close()


    
        