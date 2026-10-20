"""Corre esto con `pytest test_notificaciones_ejercicio3.py` antes de
dar por resuelto el Ejercicio 3.
"""

from notificaciones_ejercicio3 import (
    Estudiante,
    EquipoOficial,
    NotificadorCorreo,
    NotificadorSMS,
    CreadorDeNotificadorCorreo,
    CreadorDeNotificadorSMS,
    elegir_creador_de_notificador,
)


def test_notificador_correo_envia_con_prefijo_correo():
    assert NotificadorCorreo().enviar("hola") == "Correo institucional: hola"


def test_notificador_sms_envia_con_prefijo_sms():
    assert NotificadorSMS().enviar("hola") == "SMS: hola"


def test_creador_de_correo_produce_notificador_correo():
    assert isinstance(CreadorDeNotificadorCorreo().crear_notificador(), NotificadorCorreo)


def test_creador_de_sms_produce_notificador_sms():
    assert isinstance(CreadorDeNotificadorSMS().crear_notificador(), NotificadorSMS)


def test_estudiante_recibe_creador_de_correo():
    creador = elegir_creador_de_notificador(Estudiante("Ana"))
    assert isinstance(creador, CreadorDeNotificadorCorreo)


def test_equipo_oficial_recibe_creador_de_sms():
    creador = elegir_creador_de_notificador(EquipoOficial("Voleibol A"))
    assert isinstance(creador, CreadorDeNotificadorSMS)
