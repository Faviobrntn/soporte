from DBase import Conexion
from DBase import Tablas
from sqlalchemy import and_

class PersonaShowDB:
    def __init__(self):
        self.con = Conexion.conexion()

    def alta(self,pershow):
        try:
            self.con.session.add(pershow)
            self.con.session.commit()
            return True
        except Exception as e:
            print("No se pudo dar de alta el registro: "+e)
            self.con.session.rollback()
            return False

    def listarPersonaShow(self):
        personas = self.con.session.query(Tablas.PersonaShow).all()
        if(len(personas) == 0):
            self.con.session.close()
            return False
        else:
            self.con.session.close()
            return personas

    def modificarPerShow(self,pershow):
        try:
            persho = self.con.session.query(Tablas.PersonaShow).filter(and_(Tablas.PersonaShow.idpersona == pershow.idpersona, Tablas.PersonaShow.idshow == pershow.idshow,Tablas.PersonaShow.tipo==pershow.tipo)).first()
            persho.estado = pershow.estado
            persho.puntuado = pershow.puntuado
            self.con.session.add(persho)
            self.con.session.commit()
            return True
        except Exception as e:
            print("No se pudo dar modificar el registro: "+e)
            self.con.session.rollback()
            return False

    def bajaPerShow(self,pershow):
        try:
            persho = self.con.session.query(Tablas.PersonaShow).filter(and_(Tablas.PersonaShow.idpersona == pershow.idpersona, Tablas.PersonaShow.idshow == pershow.idshow,Tablas.PersonaShow.tipo==pershow.tipo)).first()
            persho.estado = pershow.estado
            persho.puntuado = pershow.puntuado
            self.con.session.delete(persho)
            self.con.session.commit()
            return True
        except Exception as e:
            print("No se pudo dar de baja el registro: "+e)
            self.con.session.rollback()
            return False

    def buscarPerShowsPorIdPersona(self,id):
        try:
            shows=self.con.session.query(Tablas.PersonaShow).filter(Tablas.PersonaShow.idpersona == id).all()
            return shows
        except Exception as e:
            return None

    def buscarPerShow(self,pershow):
        try:
            persho = self.con.session.query(Tablas.PersonaShow).filter(and_(Tablas.PersonaShow.idpersona == pershow.idpersona, Tablas.PersonaShow.idshow == pershow.idshow,Tablas.PersonaShow.tipo==pershow.tipo)).first()
            return persho
        except Exception as e:
            return None


