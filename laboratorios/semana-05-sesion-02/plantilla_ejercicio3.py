"""Ejercicio 3: patron Prototype, sobre una plantilla de reserva
recurrente de ReservaU.

Corre las pruebas con:

    pytest test_plantilla_ejercicio3.py

No cambies las firmas de las clases ni los nombres de los metodos: los
tests dependen de que existan exactamente asi.
"""

import copy


class ReservaPlantilla:
    def __init__(self, cancha, hora_inicio, hora_fin, solicitante, equipo_prestado=None, notas=""):
        if equipo_prestado is None:
            equipo_prestado = []
        self.cancha = cancha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.solicitante = solicitante
        self.equipo_prestado = equipo_prestado
        self.notas = notas
        self.fecha = None

    def clonar(self):
        # TODO 1: retorna una copia PROFUNDA (deep copy) de este objeto,
        # usando el modulo copy. Una copia superficial (shallow copy)
        # dejaria equipo_prestado apuntando a la misma lista original.
        raise NotImplementedError

    def con_fecha(self, fecha):
        # TODO 2: asigna self.fecha = fecha y retorna self, para poder
        # encadenar esta llamada justo despues de clonar().
        raise NotImplementedError

    def agregar_al_equipo_prestado(self, item):
        # TODO 3: agrega item a self.equipo_prestado y retorna self.
        raise NotImplementedError


# TODO 4: la prueba de fuego del patron. Dada una plantilla ya
# configurada y una lista de fechas, retorna una lista de reservas
# clonadas, una por fecha, cada una con esa fecha asignada mediante
# con_fecha(...). Ninguna reserva de la lista debe compartir la lista
# equipo_prestado con la plantilla original ni con las demas.
def generar_reservas_recurrentes(plantilla, fechas):
    raise NotImplementedError
