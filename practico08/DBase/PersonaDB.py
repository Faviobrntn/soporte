from DBase import Conexion
from DBase import Tablas

class PersonaDB:
    def __init__(self):
        self.con = Conexion.conexion()

    def listar(self):
        personas = self.con.session.query(Tablas.Persona).all()
        if(len(personas) == 0):
            self.con.session.close()
            return False
        else:
            self.con.session.close()
            return personas


    def alta(self,pers,us):
        try:
            self.con.session.add(pers)
            self.con.session.add(us)
            self.con.session.commit()
            return True
        except Exception as e:
            print("No se pudo dar de alta el registro: "+e)
            self.con.session.rollback()
            return False

    def buscarPersonaPorDni(self,per):
        try:
            persona = self.con.session.query(Tablas.Persona).filter(Tablas.Persona.dni == per.dni).first()
            return persona
        except Exception as e:
            return None

    def buscarPersonaPorID(self,id):
        try:
            persona = self.con.session.query(Tablas.Persona).filter(Tablas.Persona.idpersona == id).first()
            return persona
        except Exception as e:
            return None


    def actualizarPersona(self,per):
        try:
            persona = self.con.session.query(Tablas.Persona).filter(Tablas.Persona.idpersona == per.idpersona).first()
            persona.nombre=per.nombre
            persona.apellido=per.apellido
            persona.dni=per.dni
            self.con.session.add(persona)
            self.con.session.commit()
            return True
        except Exception as e:
            self.con.session.rollback()
            return False
    
'''    
    def baja(idpersona):
        try:
            sq = session.query(Persona).filter(Persona.idpersona == idpersona).first()
            session.delete(sq)
            session.commit()
        except Exception as e:
            session.rollback()
'''
