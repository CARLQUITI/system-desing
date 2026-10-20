"""Ejercicio 1: reproducir, con hilos reales, la doble reserva de la
misma cancha y el mismo horario, ejecutando ambas solicitudes al
mismo tiempo sobre el mismo calendario.

Corre esto para ver el resultado:

    python3 race_condicion_ejercicio1.py
"""

import threading
import time

from disponibilidad import Reserva, VerificadorDeDisponibilidad, Estudiante
from calendario import CalendarioDeCancha


def reservar_sin_control(calendario, verificador, cancha, fecha, hora_inicio, hora_fin, solicitante, barrera):
    if not verificador.esta_disponible(cancha, fecha, hora_inicio, hora_fin):
        return None
    # Las dos solicitudes ya pasaron la verificacion. barrera.wait()
    # las detiene aqui hasta que ambas lleguen, para que ninguna de
    # las dos registre su reserva antes de que la otra ya haya
    # verificado disponibilidad, exactamente el escenario de "casi al
    # mismo instante" de la pregunta de la sesion pasada.
    barrera.wait()
    reserva = Reserva(cancha, fecha, hora_inicio, hora_fin, solicitante)
    calendario.registrar(reserva)
    return reserva


def dos_estudiantes_reservan_la_misma_cancha():
    calendario = CalendarioDeCancha()
    verificador = VerificadorDeDisponibilidad(calendario)
    barrera = threading.Barrier(2)
    resultados = [None, None]

    def solicitud(indice, solicitante):
        resultados[indice] = reservar_sin_control(
            calendario, verificador, "Cancha 1", "2026-10-05", 18, 19, solicitante, barrera
        )

    hilo_ana = threading.Thread(target=solicitud, args=(0, Estudiante("Ana")))
    hilo_luis = threading.Thread(target=solicitud, args=(1, Estudiante("Luis")))
    hilo_ana.start()
    hilo_luis.start()
    hilo_ana.join()
    hilo_luis.join()
    return calendario, resultados


if __name__ == "__main__":
    calendario, resultados = dos_estudiantes_reservan_la_misma_cancha()
    print("Reservas registradas para Cancha 1, 2026-10-05, 18-19:", len(calendario.reservas))
    for reserva in calendario.reservas:
        print(" -", reserva.solicitante.nombre, "estado:", reserva.estado)
    print("Ambas solicitudes obtuvieron una reserva:", all(resultado is not None for resultado in resultados))
