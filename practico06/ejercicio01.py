import sys
sys.path += ['..']

from practico05.base import Socio
from practico05.ejercicio02 import DatosSocio

class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        try:
            socio= self.datos.buscar(id_socio)
            return(socio)
        except Exception as e:
            return None


    def buscar_dni(self, dni_socio):
        try:
            socio=self.datos.buscarDni(dni_socio)
            return socio
        except Exception as e:
            return None

        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """


    def todos(self):

        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        socios=self.datos.todos()
        return socios


    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        self.regla_1(socio)
        self.regla_2(socio)
        self.regla_3()
        validacion=self.datos.alta(socio)
        if (validacion==False):
            return False
        else:
            return True

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            return self.datos.baja(id_socio)
        except Exception as e:
            raise e

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        try:
            self.regla_2(socio)
            validacion=self.datos.modificacion(socio)
            if (validacion):
                return True
            else:
                return False
        except Exception as e:
            raise e

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        if(self.buscar_dni(socio.dni)):
            raise DniRepetido("Ya existe un Socio con el mismo DNI.")
        else:
            return True


    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(socio.nombre)>self.MIN_CARACTERES & len(socio.nombre)<self.MAX_CARACTERES):
            if (len(socio.apellido)>self.MIN_CARACTERES & len(socio.apellido)<self.MAX_CARACTERES):
                return True
            else:
                raise LongitudInvalida('Longitud Invalida: campo "Apellido"')
        else:
            raise LongitudInvalida('Longitud Invalida: campo "Nombre"')


    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        socios=self.todos()
        if (len(socios)<self.MAX_SOCIOS):
            return True
        else:
            raise MaximoAlcanzado('Cantidad máxima de socios alcanzada.')
