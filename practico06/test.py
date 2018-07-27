import unittest
import sys
sys.path += ['..']

from practico05.base import Socio
from practico06.ejercicio01 import NegocioSocio, LongitudInvalida


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertFalse(self.ns.regla_1(invalido))
        valido = Socio(dni=125478993, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        invalido = Socio(dni=12345678, nombre='Juanpedrorobertojorgerogelio', apellido='Perez')
        self.assertFalse(self.ns.regla_2(invalido))
        valido = Socio(dni=12345678, nombre='jorge', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))




    def test_regla_2_apellido_menor_3(self):
        invalido = Socio(dni=12345678, nombre='jorge', apellido='Pe')
        self.assertFalse(self.ns.regla_2(invalido))
        valido = Socio(dni=12345678, nombre='jorge', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

    def test_regla_2_apellido_mayor_15(self):
        invalido = Socio(dni=12345678, nombre='jorge', apellido='Perezroamiendatututututu')
        self.assertFalse(self.ns.regla_2(invalido))
        valido = Socio(dni=12345678, nombre='jorge', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

    def test_regla_3(self):
        #precondicion: menos de 200 usuarios
        self.assertTrue(len(self.ns.todos())<200)
        self.assertTrue(self.ns.regla_3())
        pass

    def test_baja(self):
        # pre-condiciones:hay un socio registrado
        self.assertEqual(len(self.ns.todos()), 1)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.baja(socio.id_socio)
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()),0)


    def test_buscar(self):
        #hay un socio con id 1
        self.assertTrue(len(self.ns.todos())>0)
        socio=self.ns.buscar(1)
        self.assertEqual(socio.id_socio,1)

    def test_buscar_dni(self):
        #hay un socio con dni 123
        socio=Socio(dni=123,nombre="juan",apellido="perez")
        self.ns.alta(socio)
        self.assertTrue(len(self.ns.todos())>0)

        socio=self.ns.buscar(123)
        self.assertEqual(socio.dni,123)
        pass

    def test_todos(self):
        #hay al menos un socio
        self.assertTrue(len(self.ns.todos())>0)

    def test_modificacion(self):
        socio=Socio(dni=123,nombre="juan",apellido="roque")
        self.assertTrue(self.ns.modificacion(socio))


