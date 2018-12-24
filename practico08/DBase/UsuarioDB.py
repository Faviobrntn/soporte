from DBase import Conexion
from DBase import Tablas
from sqlalchemy import and_

class UsuarioDB:
    def __init__(self):
        self.con = Conexion.conexion()

    def listar(self):
        usuarios = self.con.session.query(Tablas.Usuario).all()
        if(len(usuarios) == 0):
            self.con.session.close()
            return False
        else:
            self.con.session.close()
            return usuarios

    def buscarUsuario(self, usu):
        try:
            usuario = self.con.session.query(Tablas.Usuario).filter(and_(Tablas.Usuario.nombreUsuario == usu.nombreUsuario, Tablas.Usuario.contrasena == usu.contrasena)).first()
            return usuario
        except Exception as e:
            return None

    def buscarUsuarioPorID(self, id):
        try:
            usuario = self.con.session.query(Tablas.Usuario).filter(Tablas.Usuario.idpersona == id).first()
            return usuario
        except Exception as e:
            return None

    def actualizarUsuario(self,usu):
        try:
            usuario = self.con.session.query(Tablas.Usuario).filter(Tablas.Usuario.idpersona == usu.idpersona).first()
            usuario.nombreUsuario=usu.nombreUsuario
            usuario.contrasena=usu.contrasena
            self.con.session.add(usuario)
            self.con.session.commit()
            return True
        except Exception as e:
            self.con.session.rollback()
            print(str(e))
            return False
