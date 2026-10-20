"""Version antes de Factory Method: instanciacion repetida.

Corre esto para ver ambas funciones en accion:

    python3 reservas_sin_fabrica.py
"""


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre


class EquipoOficial:
    def __init__(self, nombre):
        self.nombre = nombre


class ReservaRegular:
    def __init__(self, cancha, fecha, hora_inicio, hora_fin, solicitante):
        self.cancha = cancha
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.solicitante = solicitante

    def confirmar(self):
        return "Reserva confirmada para " + self.solicitante.nombre + "."


class ReservaConPrioridad:
    def __init__(self, cancha, fecha, hora_inicio, hora_fin, solicitante):
        self.cancha = cancha
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.solicitante = solicitante

    def confirmar(self):
        return "Reserva con prioridad de equipo oficial confirmada para " + self.solicitante.nombre + "."


# isinstance(objeto, Clase) verifica si un objeto pertenece a una clase o a
# una subclase de ella. Aqui decide si el solicitante es un EquipoOficial
# (reserva con prioridad) o cualquier otro caso (reserva regular).
def registrar_reserva_desde_formulario_web(cancha, fecha, hora_inicio, hora_fin, solicitante):
    if isinstance(solicitante, EquipoOficial):
        reserva = ReservaConPrioridad(cancha, fecha, hora_inicio, hora_fin, solicitante)
    else:
        reserva = ReservaRegular(cancha, fecha, hora_inicio, hora_fin, solicitante)
    print("Formulario web:", reserva.confirmar())
    return reserva


def registrar_reserva_desde_conserje(cancha, fecha, hora_inicio, hora_fin, solicitante):
    if isinstance(solicitante, EquipoOficial):
        reserva = ReservaConPrioridad(cancha, fecha, hora_inicio, hora_fin, solicitante)
    else:
        reserva = ReservaRegular(cancha, fecha, hora_inicio, hora_fin, solicitante)
    print("Registro de conserje:", reserva.confirmar())
    return reserva


if __name__ == "__main__":
    registrar_reserva_desde_formulario_web("Cancha 1", "2026-10-01", "18:00", "19:00", Estudiante("Ana"))
    registrar_reserva_desde_conserje("Cancha 2", "2026-10-01", "17:00", "18:00", EquipoOficial("Voleibol A"))
