"""Subsistema 3 de ReservaU: notificar al solicitante.

Reutiliza el Factory Method de notificaciones construido en la Semana
5, Sesion 1: un Estudiante recibe el aviso por correo institucional,
un EquipoOficial lo recibe por SMS.
"""

from disponibilidad import EquipoOficial


class Notificador:
    def enviar(self, mensaje):
        raise NotImplementedError


class NotificadorCorreo(Notificador):
    def enviar(self, mensaje):
        return "Correo institucional: " + mensaje


class NotificadorSMS(Notificador):
    def enviar(self, mensaje):
        return "SMS: " + mensaje


class CreadorDeNotificador:
    def crear_notificador(self):
        raise NotImplementedError


class CreadorDeNotificadorCorreo(CreadorDeNotificador):
    def crear_notificador(self):
        return NotificadorCorreo()


class CreadorDeNotificadorSMS(CreadorDeNotificador):
    def crear_notificador(self):
        return NotificadorSMS()


def elegir_creador_de_notificador(solicitante):
    if isinstance(solicitante, EquipoOficial):
        return CreadorDeNotificadorSMS()
    return CreadorDeNotificadorCorreo()
