"""Ejercicio 3: aplica el mismo patron Strategy a una decision distinta
de ReservaU: con cuantas horas de anticipacion se envia el recordatorio
de una reserva.

Corre las pruebas con:

    pytest test_recordatorio_ejercicio3.py

No cambies las firmas de las clases ni los nombres de los metodos: los
tests dependen de que existan exactamente asi.
"""


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre


class EquipoOficial:
    def __init__(self, nombre):
        self.nombre = nombre


class PoliticaDeRecordatorio:
    def horas_de_anticipacion(self):
        raise NotImplementedError


class RecordatorioEstudiante(PoliticaDeRecordatorio):
    def horas_de_anticipacion(self):
        # TODO 1: retorna 1 (recordatorio 1 hora antes de la reserva).
        raise NotImplementedError


class RecordatorioEquipoOficial(PoliticaDeRecordatorio):
    def horas_de_anticipacion(self):
        # TODO 2: retorna 3 (recordatorio 3 horas antes, para que el
        # capitan alcance a avisar al resto del equipo).
        raise NotImplementedError


# TODO 3: la prueba de fuego del patron. Retorna la politica correcta
# segun el tipo de solicitante (usa isinstance, igual que en
# prioridad_con_strategy.py y cancelacion_con_strategy.py). Ninguna de
# las dos clases de politica de arriba debe cambiar una sola linea
# para que esto funcione.
def elegir_politica_de_recordatorio(solicitante):
    raise NotImplementedError


# TODO 4: retorna la hora exacta en la que debe enviarse el
# recordatorio de esta reserva: hora_inicio menos las horas de
# anticipacion que indique la politica del solicitante.
def calcular_hora_de_envio(hora_inicio, solicitante):
    raise NotImplementedError
