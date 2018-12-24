from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship

Base = declarative_base()

class Persona(Base):
	__tablename__ = 'persona'
	idpersona = Column(Integer, primary_key=True, autoincrement=True)
	nombre = Column(String)
	apellido = Column(String)
	dni = Column(String)

class Usuario(Base):
	__tablename__='usuario'
	idUsuario = Column(Integer, primary_key=True, autoincrement=True)
	nombreUsuario = Column(String)
	contrasena = Column(String)
	idpersona = Column(Integer,ForeignKey('persona.idpersona'))
	persona = relationship(Persona)

class Show(Base):
	__tablename__='show'
	id=Column(Integer,primary_key=True,autoincrement=True)
	idShow = Column(Integer)
	tipo = Column(Integer)
	#cero pelicula,1 serie
	nombre = Column(String)
	overview = Column(String)
	puntuacionIMDB = Column(Float)
	puntuacionUsuariosAcumulada = Column(Integer)
	cantidadPuntuaciones = Column(Integer)
	poster = Column(String)



class PersonaShow(Base):
	__tablename__='personashow'
	id=Column(Integer,primary_key=True, autoincrement=True)
	idpersona = Column(Integer)
	idshow = Column(Integer)
	tipo = Column(Integer)
	#cero pelicula,1 serie
	puntuado = Column(Integer)
	#no puntuado-1puntuado
	estado = Column(Integer)
	#0-vista 1-pendiente 2-proceso
