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
        sql="insert into login (usuario, contrasena) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select * from login where usuario=%s and contrasena=%s"
        cursor.execute(sql, datos)
        cone.close()	
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select *  from login"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
