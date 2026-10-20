"""Punto de partida: la politica de cancelacion de ReservaU, con un
if/else dentro del mismo metodo.

Corre esto para ver el resultado:

    python3 cancelacion_sin_strategy.py
"""


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre


class AdministradorDelComplejo:
    def __init__(self, nombre):
        self.nombre = nombre


class Reserva:
    def __init__(self, cancha, hora_inicio, solicitante):
        self.cancha = cancha
        self.hora_inicio = hora_inicio
        self.solicitante = solicitante
        self.estado = "activa"

    def cancelar(self, hora_actual):
        if isinstance(self.solicitante, AdministradorDelComplejo):
            self.estado = "cancelada"
        else:
            if self.hora_inicio - hora_actual < 2:
                self.estado = "no_show"
            else:
                self.estado = "cancelada"
        return self.estado


if __name__ == "__main__":
    reserva_1 = Reserva("Cancha 1", 18, Estudiante("Ana"))
    print("Ana cancela a las 17h (falta 1 hora):", reserva_1.cancelar(17))

    reserva_2 = Reserva("Cancha 2", 18, Estudiante("Beto"))
    print("Beto cancela a las 15h (faltan 3 horas):", reserva_2.cancelar(15))

    reserva_3 = Reserva("Cancha 3", 18, AdministradorDelComplejo("Recepcion"))
    print("Administrador cancela por mantenimiento:", reserva_3.cancelar(17))
