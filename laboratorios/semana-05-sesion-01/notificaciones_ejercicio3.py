"""Ejercicio 3: mismo patron de Factory Method que viste con las
reservas, ahora sobre como ReservaU decide a quien avisar.

Corre las pruebas con:

    pytest test_notificaciones_ejercicio3.py

No cambies las firmas de las clases ni los nombres de los metodos: los
tests dependen de que existan exactamente asi.
"""


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre


class EquipoOficial:
    def __init__(self, nombre):
        self.nombre = nombre


class Notificador:
    def enviar(self, mensaje):
        raise NotImplementedError


class NotificadorCorreo(Notificador):
    def enviar(self, mensaje):
        # TODO 1: retorna "Correo institucional: " concatenado con mensaje
        raise NotImplementedError


class NotificadorSMS(Notificador):
    def enviar(self, mensaje):
        # TODO 2: retorna "SMS: " concatenado con mensaje
        raise NotImplementedError


class CreadorDeNotificador:
    def crear_notificador(self):
        raise NotImplementedError


class CreadorDeNotificadorCorreo(CreadorDeNotificador):
    def crear_notificador(self):
        # TODO 3: retorna una instancia de NotificadorCorreo
        raise NotImplementedError


class CreadorDeNotificadorSMS(CreadorDeNotificador):
    def crear_notificador(self):
        # TODO 4: retorna una instancia de NotificadorSMS
        raise NotImplementedError


# TODO 5: la prueba de fuego del patron. Un Estudiante recibe avisos por
# correo institucional; un EquipoOficial, cuyo capitan necesita
# coordinar con el resto del equipo rapido, recibe avisos por SMS.
#
# Completa esta funcion para que retorne el creador correcto segun el
# tipo de solicitante (usa isinstance, igual que en reservas_sin_fabrica.py).
# Ninguna de las clases que ya existen en este archivo debe cambiar una
# sola linea para que esto funcione: si tuviste que tocar alguna, algo en
# tu diseno todavia depende de un if/else disperso en vez de Factory
# Method.
def elegir_creador_de_notificador(solicitante):
    raise NotImplementedError
