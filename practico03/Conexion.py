import pymysql
class Conexion():
    conn=pymysql
    def conectar(self):
        try:
            self.conn=pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="soporte")
        except Exception as f:
            print("no se puede conectar a la base de datos"+str(f))
