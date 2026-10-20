from datos_reservas import generar_reservas, ReservaRegistrada
from sharding_por_campus_ejercicio1 import shard_por_campus, contar_por_shard


def test_cada_campus_va_a_su_shard():
    reserva = ReservaRegistrada(1, "est-0001", "Campus Centro", "Cancha 1", "2026-10-19", 9)
    assert shard_por_campus(reserva) == 2


def test_el_campus_norte_concentra_mas_de_la_mitad():
    conteo = contar_por_shard(generar_reservas(), 4)
    assert conteo == [600, 200, 150, 50]
