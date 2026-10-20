"""Corre esto con `pytest test_reserva_optimista_ejercicio3.py` antes
de dar por resuelto el Ejercicio 3.
"""

import threading

from disponibilidad import Estudiante
from reserva_optimista_ejercicio3 import ReservadorOptimista


def dos_estudiantes_reservan_optimista():
    reservador = ReservadorOptimista()
    barrera = threading.Barrier(2)
    resultados = [None, None]

    def solicitud(indice, solicitante):
        barrera.wait()
        resultados[indice] = reservador.reservar("Cancha 1", "2026-10-05", 18, 19, solicitante)

    hilo_ana = threading.Thread(target=solicitud, args=(0, Estudiante("Ana")))
    hilo_luis = threading.Thread(target=solicitud, args=(1, Estudiante("Luis")))
    hilo_ana.start()
    hilo_luis.start()
    hilo_ana.join()
    hilo_luis.join()
    return reservador, resultados


def test_solo_una_de_las_dos_solicitudes_se_confirma():
    _, resultados = dos_estudiantes_reservan_optimista()
    exitosas = []
    rechazadas = []
    for resultado in resultados:
        if resultado is not None:
            exitosas.append(resultado)
        else:
            rechazadas.append(resultado)
    assert len(exitosas) == 1
    assert len(rechazadas) == 1


def test_el_calendario_termina_con_una_sola_reserva_y_version_1():
    reservador, _ = dos_estudiantes_reservan_optimista()
    assert len(reservador.calendario.reservas) == 1
    assert reservador.calendario.version == 1


def test_repetido_20_veces_nunca_deja_pasar_las_dos():
    contador_de_dobles = 0
    for _ in range(20):
        reservador, resultados = dos_estudiantes_reservan_optimista()
        if all(resultado is not None for resultado in resultados):
            contador_de_dobles += 1
    assert contador_de_dobles == 0


def test_sin_contencion_la_reserva_se_confirma_normalmente():
    reservador = ReservadorOptimista()
    resultado = reservador.reservar("Cancha 2", "2026-10-05", 10, 11, Estudiante("Maria"))
    assert resultado is not None
    assert reservador.calendario.version == 1
