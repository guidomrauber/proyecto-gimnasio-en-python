import pymysql

class Articulos:

    def abrir(self):
        conexion=pymysql.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="bd3")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into clientes (nombre,apellido,dni,domicilio,email,telefono,cuota) values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nombre,apellido,dni,domicilio,email,telefono,cuota from clientes"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas borradas

    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update articulos set descripcion=%s, precio=%s where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas modificadas