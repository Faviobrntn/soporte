from DBase import PersonaShowDB
from DBase import ShowDB

class ABMPersonaShow():
    def __init__(self):
        self.pershowDB = PersonaShowDB.PersonaShowDB()
        self.showDB = ShowDB.ShowDB()

    def altaPersonaShow(self,pershow):
        persho=self.pershowDB.buscarPerShow(pershow)
        if (persho == None or persho.tipo!=pershow.tipo):
            self.pershowDB.alta(pershow)
        return True

    def validarPersho(self,pershow):
        persho=self.pershowDB.buscarPerShow(pershow)
        if (persho == None or persho.tipo!=pershow.tipo):
            return True
        else:
            return False



    def buscarPerShowPorIdPersona(self,id):
        return self.pershowDB.buscarPerShowsPorIdPersona(id)

    def listarPersonaShow(self):
        return self.pershowDB.listarPersonaShow()

    def buscarPerShow(self,pershow):
        return self.pershowDB.buscarPerShow(pershow)

    def modificarPerShow(self,pershow):
        return self.pershowDB.modificarPerShow(pershow)

    def eliminarPerShow(self,pershow):
        return self.pershowDB.bajaPerShow(pershow)


