"""Ejercicio 3: evitar la doble reserva con locking optimista, sin
bloquear a nadie mientras se verifica disponibilidad.

Corre las pruebas con:

    pytest test_reserva_optimista_ejercicio3.py

No cambies las firmas de las funciones ni de la clase: los tests
dependen de que existan exactamente asi.
"""

import time

from disponibilidad import Reserva, VerificadorDeDisponibilidad
from calendario_con_version import CalendarioDeCanchaConVersion


class ReservadorOptimista:
    def __init__(self):
        self.calendario = CalendarioDeCanchaConVersion()
        self.verificador = VerificadorDeDisponibilidad(self.calendario)

    def reservar(self, cancha, fecha, hora_inicio, hora_fin, solicitante):
        # TODO, en este orden exacto:
        # 1. Lee self.calendario.version y guardala en una variable
        #    (por ejemplo version_leida), antes de verificar nada.
        # 2. Verifica disponibilidad con self.verificador.esta_disponible(...).
        #    Si no esta disponible, retorna None. Nota que este paso no
        #    toma ningun lock: cualquier otra solicitud puede verificar
        #    al mismo tiempo, sin esperar en fila.
        # 3. Agrega time.sleep(0.05), simulando el mismo tiempo de
        #    procesamiento del Ejercicio 2.
        # 4. Construye la Reserva y llama a
        #    self.calendario.intentar_registrar_con_version(reserva, version_leida).
        #    Si retorna False, alguien mas ya registro una reserva
        #    entre tu paso 1 y tu paso 4: retorna None (tu solicitud
        #    perdio la carrera, no queda ninguna reserva doble). Si
        #    retorna True, retorna la reserva.
        raise NotImplementedError
