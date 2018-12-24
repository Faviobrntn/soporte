import unittest
from DBase import Tablas
from Negocio import ABMPersonaShow



class showTest(unittest.TestCase):
    #valida que el show no exista en la bd
    def test_validarShow(self):
        #La casa de papel id serie=71446 (ya se encuentra en la BD) para el usuario 1
        per=Tablas.PersonaShow()
        abm=ABMPersonaShow.ABMPersonaShow()
        per.idpersona=1
        per.idshow=71446
        per.tipo=1#(serie)
        self.assertFalse(abm.validarPersho(per))
        per.tipo=0#(pelicula)
        self.assertTrue(abm.validarPersho(per))
        #tiene que dar True, porque no existe en la base de datos la pelicula con esa persona
        per.idshow=17458
        self.assertTrue(abm.validarPersho(per))
        #no existe esa relacion


if __name__ == '__main__':
    unittest.main()
