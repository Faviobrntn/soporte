from DBase import Tablas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class conexion():
	def __init__(self):
		engine = create_engine('sqlite:///Basenueva.bd')
		Tablas.Base.metadata.bind = engine
		Tablas.Base.metadata.create_all(engine)
		db_session = sessionmaker()
		db_session.bind = engine
		self.session = db_session()

