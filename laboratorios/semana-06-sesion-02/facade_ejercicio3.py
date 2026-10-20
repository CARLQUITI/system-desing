"""Ejercicio 3: extiende la Facade de ReservaU con un metodo cancelar,
que unifica el calendario y la notificacion detras de una sola
interfaz, aplicando la politica de cancelacion construida en la
Semana 6, Sesion 1.

Corre las pruebas con:

    pytest test_facade_ejercicio3.py

No cambies las firmas de las clases ni los nombres de los metodos: los
tests dependen de que existan exactamente asi.
"""

from disponibilidad import Reserva, VerificadorDeDisponibilidad, Estudiante, EquipoOficial, AdministradorDelComplejo
from calendario import CalendarioDeCancha
from notificacion import elegir_creador_de_notificador


class PoliticaDeCancelacion:
    def resolver(self, hora_inicio, hora_actual):
        raise NotImplementedError


class CancelacionEstandar(PoliticaDeCancelacion):
    def resolver(self, hora_inicio, hora_actual):
        if hora_inicio - hora_actual < 2:
            return "no_show"
        return "cancelada"


class CancelacionSinPenalidad(PoliticaDeCancelacion):
    def resolver(self, hora_inicio, hora_actual):
        return "cancelada"


def elegir_politica_de_cancelacion(solicitante):
    if isinstance(solicitante, AdministradorDelComplejo):
        return CancelacionSinPenalidad()
    return CancelacionEstandar()


class FacadeDeReservas:
    def __init__(self):
        self.calendario = CalendarioDeCancha()
        self.verificador = VerificadorDeDisponibilidad(self.calendario)

    def reservar(self, cancha, fecha, hora_inicio, hora_fin, solicitante):
        if not self.verificador.esta_disponible(cancha, fecha, hora_inicio, hora_fin):
            return None
        reserva = Reserva(cancha, fecha, hora_inicio, hora_fin, solicitante)
        self.calendario.registrar(reserva)
        return reserva

    def cancelar(self, reserva, hora_actual):
        # TODO: aplica la politica de cancelacion correcta segun
        # reserva.solicitante (elegir_politica_de_cancelacion), guarda
        # el resultado en reserva.estado, notifica el resultado con
        # elegir_creador_de_notificador(reserva.solicitante) usando el
        # mensaje exacto "tu reserva fue registrada como " concatenado
        # con reserva.estado, y retorna ese mismo mensaje.
        raise NotImplementedError
