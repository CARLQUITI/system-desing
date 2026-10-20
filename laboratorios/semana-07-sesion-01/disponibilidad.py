"""Subsistema de ReservaU: verificar disponibilidad de una cancha.

Reutiliza Reserva.se_solapa_con(otra_reserva), la misma regla de
negocio construida en la Semana 3, Sesion 2.
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
    def __init__(self, cancha, fecha, hora_inicio, hora_fin, solicitante):
        self.cancha = cancha
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.solicitante = solicitante
        self.estado = "activa"

    def se_solapa_con(self, otra_reserva):
        if self.cancha != otra_reserva.cancha:
            return False
        if self.fecha != otra_reserva.fecha:
            return False
        return self.hora_inicio < otra_reserva.hora_fin and otra_reserva.hora_inicio < self.hora_fin


class VerificadorDeDisponibilidad:
    def __init__(self, calendario):
        self.calendario = calendario

    def esta_disponible(self, cancha, fecha, hora_inicio, hora_fin):
        candidata = Reserva(cancha, fecha, hora_inicio, hora_fin, None)
        for reserva_existente in self.calendario.reservas:
            if reserva_existente.estado == "activa" and candidata.se_solapa_con(reserva_existente):
                return False
        return True
