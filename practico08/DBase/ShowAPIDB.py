from tmdbv3api import TMDb, TV, Movie,Season, Discover
from DBase import Tablas




class ShowAPIDB():
    def __init__(self):
        self.tmdb= TMDb()
        self.tmdb.api_key="e00b72174e4ae097af808f34a8f220fc"
        self.tv=TV()
        self.season=Season()
        self.movie= Movie()
        self.discover = Discover()


    def buscarSerie(self,nombre):
        resultado = self.tv.search(nombre)
        series=[]
        for i in resultado:
            serie=Tablas.Show()
            serie.nombre = i.name
            serie.idShow = i.id
            serie.overview = i.overview
            serie.poster = i.poster_path
            serie.puntuacionIMDB = i.vote_average
            serie.tipo=1
            series.append(serie)
        return series



    def buscarPelicula(self,nombre):
        resultado = self.movie.search(nombre)
        pelis=[]
        for i in resultado:
            peli = Tablas.Show()
            peli.tipo = 0
            peli.nombre = i.title
            peli.idShow = i.id
            peli.overview = i.overview
            peli.poster = i.poster_path
            peli.puntuacionIMDB = i.vote_average
            pelis.append(peli)
        return pelis

    def buscarPeliculaPorID(self,id):
        resultado=self.movie.details(id)
        peli=Tablas.Show()
        peli.tipo = 0
        peli.nombre = resultado.title
        peli.idShow = resultado.id
        peli.overview = resultado.overview
        peli.poster = resultado.poster_path
        peli.puntuacionIMDB = resultado.vote_average
        return peli


    def buscarSeriePorID(self,id):
        i = self.tv.details(id)
        serie=Tablas.Show()
        serie.nombre = i.name
        serie.idShow = i.id
        serie.overview = i.overview
        serie.poster = i.poster_path
        serie.puntuacionIMDB = i.vote_average
        serie.tipo=1
        return serie

    def descubrir(self):
        show = self.discover.discover_tv_shows({'sort_by': 'popularity.desc'})
        series=[]
        for i in show:
            serie=Tablas.Show()
            serie.nombre = i.name
            serie.idShow = i.id
            serie.overview = i.overview
            serie.poster = i.poster_path
            serie.puntuacionIMDB = i.vote_average
            serie.tipo=1
            series.append(serie)
        return series
