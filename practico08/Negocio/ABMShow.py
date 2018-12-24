from DBase import ShowDB


class ABMShow():
    def __init__(self):
        self.showDB = ShowDB.ShowDB()

    def altaShow(self,show):
        val=self.validarShow(show)
        if(val):
            self.showDB.alta(show)
        return True

    def validarShow(self,show):
        shows=self.showDB.buscarShowPorID(show)
        if(shows==None or shows.tipo!=show.tipo):
            return True
        else:
            return False

    def buscarShowporIDyTipo(self,show):
        return self.showDB.buscarShowPorIdyTipo(show)

    def listarShows(self):
        return self.showDB.listarShows()

    def listarShowsPorID(self,show):
        return self.showDB.listarShowsPorID(show)


    def buscarShowPorID(self,show):
        return self.showDB.buscarShowPorID(show)

    def puntuarShow(self,show):
        return self.showDB.puntuarShow(show)
