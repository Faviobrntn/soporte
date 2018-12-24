import unittest
from DBase import Tablas
from Negocio import ABMUsuario


class usuarioTest(unittest.TestCase):

    def test_validarUsuario(self):
        usu = Tablas.Usuario()
        abm=ABMUsuario.ABMUsuario()
        usu.nombreUsuario='seby'
        usu.contrasena='seby'
        usu.idpersona=1
        #ya existe, pero es el mismo usuario que quiero modificar
        self.assertTrue(abm.validarUsuarioContraseña(usu))
        usu.idpersona=2
        #ya existe y no es el mismo usuario que quiero modificar
        self.assertFalse(abm.validarUsuarioContraseña(usu))
        usu.nombreUsuario='No existo'
        self.assertTrue(abm.validarUsuarioContraseña(usu))
        #no existe nadie con ese usu y cont


if __name__ == '__main__':
    unittest.main()
