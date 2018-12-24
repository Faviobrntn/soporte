from DBase import Conexion
from DBase import Tablas
from sqlalchemy import and_

class ShowDB:
    def __init__(self):
        self.con = Conexion.conexion()

    def alta(self,show):
        try:
            show.cantidadPuntuaciones=0
            show.puntuacionUsuariosAcumulada=0
            self.con.session.add(show)
            self.con.session.commit()
            return True
        except Exception as e:
            print("No se pudo dar de alta el show: "+e)
            self.con.session.rollback()
            return False

    def listarShowsPorID(self,shows):
        showsEnc=[]
        for i in shows:
            show=self.con.session.query(Tablas.Show).filter(and_(Tablas.Show.idShow == i.idshow,Tablas.Show.tipo==i.tipo)).first()
            show.estado=i.estado
            show.puntuado=i.puntuado
            showsEnc.append(show)
        return showsEnc

    def buscarShowPorID(self,id):
        try:
            show=self.con.session.query(Tablas.Show).filter(Tablas.Show.idShow == id.idShow).first()
            return show
        except Exception as e:
            return None

    def buscarShowPorIdyTipo(self,show):
        try:
            show=self.con.session.query(Tablas.Show).filter(and_(Tablas.Show.idShow == show.idShow,Tablas.Show.tipo==show.tipo)).first()
            return show
        except Exception as e:
            return None

    def listarShows(self):
        shows = self.con.session.query(Tablas.Show).all()
        if(len(shows) == 0):
            self.con.session.close()
            return False
        else:
            self.con.session.close()
            return shows


    def puntuarShow(self,show):
        try:
            sho=self.con.session.query(Tablas.Show).filter(and_(Tablas.Show.idShow == show.idShow,Tablas.Show.tipo == show.tipo)).first()
            sho.puntuacionUsuariosAcumulada=sho.puntuacionUsuariosAcumulada+show.puntuacionUsuariosAcumulada
            sho.cantidadPuntuaciones=sho.cantidadPuntuaciones+1
            self.con.session.add(show)
            self.con.session.commit()
            return True
        except Exception as e:
            print("No se pudo dar de puntear el show: "+e)
            self.con.session.rollback()
            return False
