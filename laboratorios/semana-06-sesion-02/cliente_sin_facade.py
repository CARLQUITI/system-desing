"""Punto de partida: el codigo cliente habla directamente con los 3
subsistemas de ReservaU (disponibilidad, calendario, notificacion).

Corre esto para ver el resultado:

    python3 cliente_sin_facade.py
"""

from disponibilidad import Reserva, VerificadorDeDisponibilidad, Estudiante, EquipoOficial
from calendario import CalendarioDeCancha
from notificacion import elegir_creador_de_notificador


calendario = CalendarioDeCancha()
verificador = VerificadorDeDisponibilidad(calendario)


def registrar_reserva_desde_formulario_web(cancha, fecha, hora_inicio, hora_fin, solicitante):
    if not verificador.esta_disponible(cancha, fecha, hora_inicio, hora_fin):
        print("Formulario web: cancha no disponible.")
        return None
    reserva = Reserva(cancha, fecha, hora_inicio, hora_fin, solicitante)
    calendario.registrar(reserva)
    notificador = elegir_creador_de_notificador(solicitante).crear_notificador()
    print("Formulario web:", notificador.enviar("tu reserva fue confirmada"))
    return reserva


def registrar_reserva_desde_conserje(cancha, fecha, hora_inicio, hora_fin, solicitante):
    if not verificador.esta_disponible(cancha, fecha, hora_inicio, hora_fin):
        print("Registro de conserje: cancha no disponible.")
        return None
    reserva = Reserva(cancha, fecha, hora_inicio, hora_fin, solicitante)
    calendario.registrar(reserva)
    notificador = elegir_creador_de_notificador(solicitante).crear_notificador()
    print("Registro de conserje:", notificador.enviar("tu reserva fue confirmada"))
    return reserva


if __name__ == "__main__":
    registrar_reserva_desde_formulario_web("Cancha 1", "2026-10-01", 18, 19, Estudiante("Ana"))
    registrar_reserva_desde_conserje("Cancha 1", "2026-10-01", 18, 19, EquipoOficial("Voleibol A"))
