"""Corre esto con `pytest test_facade_ejercicio3.py` antes de dar por
resuelto el Ejercicio 3.
"""

from facade_ejercicio3 import FacadeDeReservas, Estudiante, EquipoOficial, AdministradorDelComplejo


def test_cancelacion_administrativa_nunca_es_no_show():
    facade = FacadeDeReservas()
    reserva = facade.reservar("Cancha 1", "2026-10-01", 18, 19, AdministradorDelComplejo("Recepcion"))
    resultado = facade.cancelar(reserva, 18)
    assert reserva.estado == "cancelada"
    assert "cancelada" in resultado


def test_cancelacion_estudiante_menos_de_2_horas_antes_es_no_show():
    facade = FacadeDeReservas()
    reserva = facade.reservar("Cancha 2", "2026-10-01", 18, 19, Estudiante("Ana"))
    facade.cancelar(reserva, 17)
    assert reserva.estado == "no_show"


def test_cancelacion_estudiante_2_horas_o_mas_antes_es_cancelada():
    facade = FacadeDeReservas()
    reserva = facade.reservar("Cancha 3", "2026-10-01", 18, 19, Estudiante("Ana"))
    facade.cancelar(reserva, 16)
    assert reserva.estado == "cancelada"


def test_cancelar_libera_el_horario_para_una_nueva_reserva():
    facade = FacadeDeReservas()
    reserva = facade.reservar("Cancha 4", "2026-10-01", 18, 19, Estudiante("Ana"))
    facade.cancelar(reserva, 16)
    assert facade.verificador.esta_disponible("Cancha 4", "2026-10-01", 18, 19) is True


def test_cancelacion_equipo_oficial_notifica_por_sms():
    facade = FacadeDeReservas()
    reserva = facade.reservar("Cancha 5", "2026-10-01", 18, 19, EquipoOficial("Voleibol A"))
    resultado = facade.cancelar(reserva, 16)
    assert resultado == "SMS: tu reserva fue registrada como cancelada"
