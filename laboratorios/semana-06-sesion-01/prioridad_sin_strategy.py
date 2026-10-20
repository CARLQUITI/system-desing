"""Punto de partida: la politica de prioridad de ReservaU, con un
enorme if/elif dentro del mismo metodo.

Corre esto para ver el resultado:

    python3 prioridad_sin_strategy.py
"""


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre


class EquipoOficial:
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

    def es_prioritaria(self, es_evento_institucional):
        if isinstance(self.solicitante, AdministradorDelComplejo):
            if es_evento_institucional:
                return True
            return False
        elif isinstance(self.solicitante, EquipoOficial):
            if self.hora_inicio < 18:
                return True
            return False
        else:
            return False


if __name__ == "__main__":
    reserva_1 = Reserva("Cancha 1", 17, EquipoOficial("Voleibol A"))
    reserva_2 = Reserva("Cancha 2", 20, EquipoOficial("Basquet B"))
    reserva_3 = Reserva("Cancha 3", 10, AdministradorDelComplejo("Recepcion"))
    reserva_4 = Reserva("Cancha 4", 10, Estudiante("Ana"))
    print("Voleibol A a las 17h:", reserva_1.es_prioritaria(False))
    print("Basquet B a las 20h:", reserva_2.es_prioritaria(False))
    print("Administrador, evento institucional:", reserva_3.es_prioritaria(True))
    print("Ana, estudiante regular:", reserva_4.es_prioritaria(False))
