"""El calendario de reservas de una cancha, sin ningun control de
concurrencia todavia: esta es la version vulnerable a la doble
reserva que el Ejercicio 1 reproduce.
"""


class CalendarioDeCancha:
    def __init__(self):
        self.reservas = []

    def registrar(self, reserva):
        self.reservas.append(reserva)
