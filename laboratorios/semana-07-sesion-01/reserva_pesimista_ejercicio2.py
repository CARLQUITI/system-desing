"""Ejercicio 2: evitar la doble reserva del Ejercicio 1 con locking
pesimista: un threading.Lock que obliga a la segunda solicitud a
esperar a que la primera termine de verificar y registrar, antes de
dejarla siquiera empezar a verificar.

Corre las pruebas con:

    pytest test_reserva_pesimista_ejercicio2.py

No cambies las firmas de las funciones ni de la clase: los tests
dependen de que existan exactamente asi.
"""

import threading
import time

from disponibilidad import Reserva, VerificadorDeDisponibilidad
from calendario import CalendarioDeCancha


class ReservadorPesimista:
    def __init__(self):
        self.calendario = CalendarioDeCancha()
        self.verificador = VerificadorDeDisponibilidad(self.calendario)
        self.lock = threading.Lock()

    def reservar(self, cancha, fecha, hora_inicio, hora_fin, solicitante):
        # TODO: adquiere self.lock antes de verificar disponibilidad
        # (self.lock.acquire()), y libera self.lock (self.lock.release())
        # justo antes de cada punto en el que esta funcion retorna,
        # tanto si la cancha no esta disponible como si la reserva ya
        # quedo registrada. Mientras el lock esta tomado, cualquier
        # otro hilo que llame a reservar() se detiene, esperando, en
        # su propio self.lock.acquire(), sin poder verificar
        # disponibilidad todavia.
        #
        # Agrega time.sleep(0.05) entre el momento en que confirmas
        # que la cancha esta disponible y el momento en que registras
        # la reserva: simula el tiempo real que toma escribir la
        # reserva (por ejemplo, una consulta a una base de datos), y
        # es lo que hace que la ventana de la condicion de carrera sea
        # real y no instantanea.
        raise NotImplementedError
