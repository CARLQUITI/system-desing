"""Subsistema 2 de ReservaU: el calendario de reservas de una cancha."""


class CalendarioDeCancha:
    def __init__(self):
        self.reservas = []

    def registrar(self, reserva):
        self.reservas.append(reserva)
