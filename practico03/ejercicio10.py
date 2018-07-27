from Conexion import *
base=Conexion()
base.conectar()
cur=base.conn.cursor()
js=[]

cur.execute("SELECT nombre,dni,fecha,peso,nacimiento FROM persona INNER JOIN personapeso ON persona.idpersona=personapeso.idpersona ORDER BY dni")

for nombre,dni,fecha,peso,nacimiento in cur.fetchall():
    str_json={'nombre':nombre,'dni':dni,'fecha':str(fecha),'peso':peso,'nacimiento':nacimiento}
    js.append(str_json)

for i in js:
    print(i)
