from DBase import ShowAPIDB


class ShowAPI():
    def __init__(self):
        self.api=ShowAPIDB.ShowAPIDB()

    def buscarSerie(self,nombre):
        return self.api.buscarSerie(nombre)

    def buscarPelicula(self,nombre):
        return self.api.buscarPelicula(nombre)

    def buscarPeliculaPorId(self,id):
        return self.api.buscarPeliculaPorID(id)

    def buscarSeriePorId(self,id):
        return self.api.buscarSeriePorID(id)

    def descubrir(self):
        return self.api.descubrir()
