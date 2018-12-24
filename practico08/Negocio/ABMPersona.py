from DBase import PersonaDB
from DBase import UsuarioDB


class ABMPersona():
    def __init__(self):
        self.perDB = PersonaDB.PersonaDB()
        self.usuDB = UsuarioDB.UsuarioDB()

    def validarCamposPer(self,per):
        if(per.nombre!="" and per.apellido!="" and per.dni!=""):
            return True
        else:
            return False

    def validarCamposUsu(self,usu):
        if(usu.nombreUsuario!="" and usu.contrasena!=""):
            return True
        else:
            return False

    def altaPersona(self,per,us):
        pers=self.validarDni(per)
        usus=self.validarUsuarioContraseña(us)
        val1=self.validarCamposPer(per)
        val2=self.validarCamposUsu(us)
        if(pers and usus and val1 and val2):
            guardado = self.perDB.alta(per,us)
            return guardado
        else:
            return False

    def validarDni(self, pe):
        per=self.buscarPersonaPorDni(pe)
        if per==None:
            return True
        else:
            return False

    def validarUsuarioContraseña(self,us):
        usu=self.usuDB.buscarUsuario(us)
        if usu==None:
            return True
        else:
            return False


    def listarPersonas(self):
        return self.perDB.listar()

    def buscarPersonaPorDni(self,per):
        return self.perDB.buscarPersonaPorDni(per)

    def buscarPersonaPorID(self,id):
        return self.perDB.buscarPersonaPorID(id)

    def actualizarPersona(self,per):
        val=self.validarDniAndIdpersona(per)
        val1=self.validarCamposPer(per)
        if(val and val1):
            return self.perDB.actualizarPersona(per)
        else:
            return False

    def validarDniAndIdpersona(self,per):
        pers=self.buscarPersonaPorID(per)
        if(pers==None or pers.idpersona==per.idpersona):
            return True
        else:
            return False
