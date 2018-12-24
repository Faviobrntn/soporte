import unittest
from DBase import Tablas
from Negocio import ABMPersona

class personaTest(unittest.TestCase):

    def test_validarDatosPersona(self):
        per = Tablas.Persona()
        per.nombre=''
        abm=ABMPersona.ABMPersona()
        self.assertFalse(abm.validarCamposPer(per))
        per.nombre='juan'
        per.apellido=''
        self.assertFalse(abm.validarCamposPer(per))
        per.apellido='perez'
        per.dni=''
        self.assertFalse(abm.validarCamposPer(per))
        per.dni='14586697'
        self.assertTrue(abm.validarCamposPer(per))

    def test_validarDatosUsuario(self):
        usu = Tablas.Usuario()
        abm=ABMPersona.ABMPersona()
        usu.nombreUsuario=''
        self.assertFalse(abm.validarCamposUsu(usu))
        usu.nombreUsuario="pepito"
        usu.contrasena=''
        self.assertFalse(abm.validarCamposUsu(usu))
        usu.contrasena="donpepito"
        self.assertTrue(abm.validarCamposUsu(usu))

    def test_validarDni(self):
        per=Tablas.Persona()
        per.dni="1234567"
        abm=ABMPersona.ABMPersona()
        #dni no existe
        self.assertTrue(abm.validarDni(per))
        per.dni='38541538'
        self.assertFalse(abm.validarDni(per))

    def test_validarUsuario(self):
        usu=Tablas.Usuario()
        usu.nombreUsuario='seby'
        usu.contrasena='seby'
        #ya existe
        abm=ABMPersona.ABMPersona()
        self.assertFalse(abm.validarUsuarioContraseña(usu))
        usu.nombreUsuario='Juan'
        #no existe
        self.assertTrue(abm.validarUsuarioContraseña(usu))


    def test_validarPersonaDniAndId(self):
        per=Tablas.Persona()
        per.idpersona=1
        per.dni='38541538'
        #existe persona con el mismo dni, pero es la misma persona (permite la modificacion)
        abm=ABMPersona.ABMPersona()
        self.assertTrue(abm.validarDniAndIdpersona(per))
        per.idpersona=2
        #ya existe otra persona con ese dni que se desea modificar
        self.assertFalse(abm.validarDniAndIdpersona(per))




if __name__ == '__main__':
    unittest.main()
