from DBase import UsuarioDB


class ABMUsuario():
    def __init__(self):
        self.usDB=UsuarioDB.UsuarioDB()

    def listarUsuarios(self):
        return self.usDB.listar()

    def buscarUsuario(self, usu):
        return self.usDB.buscarUsuario(usu)

    def buscarUsuarioPorID(self,id):
        return self.usDB.buscarUsuarioPorID(id)

    def actualizarUsuario(self,usu):
        val=self.validarUsuarioContraseña(usu)
        if(val):
            return self.usDB.actualizarUsuario(usu)
        else:
            return False

    def validarUsuarioContraseña(self,usu):
        usus=self.usDB.buscarUsuario(usu)
        if(usus==None or usus.idpersona==usu.idpersona):
            return True
        else:
            return False
