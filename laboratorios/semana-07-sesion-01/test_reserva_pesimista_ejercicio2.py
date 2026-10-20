"""Corre esto con `pytest test_reserva_pesimista_ejercicio2.py` antes
de dar por resuelto el Ejercicio 2.
"""

import threading

from disponibilidad import Estudiante
from reserva_pesimista_ejercicio2 import ReservadorPesimista


def dos_estudiantes_reservan_con_lock():
    reservador = ReservadorPesimista()
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


def test_solo_una_de_las_dos_solicitudes_obtiene_reserva():
    _, resultados = dos_estudiantes_reservan_con_lock()
    exitosas = []
    rechazadas = []
    for resultado in resultados:
        if resultado is not None:
            exitosas.append(resultado)
        else:
            rechazadas.append(resultado)
    assert len(exitosas) == 1
    assert len(rechazadas) == 1


def test_el_calendario_termina_con_una_sola_reserva():
    reservador, _ = dos_estudiantes_reservan_con_lock()
    assert len(reservador.calendario.reservas) == 1


def test_repetido_20_veces_nunca_deja_pasar_las_dos():
    contador_de_dobles = 0
    for _ in range(20):
        reservador, resultados = dos_estudiantes_reservan_con_lock()
        if all(resultado is not None for resultado in resultados):
            contador_de_dobles += 1
    assert contador_de_dobles == 0
