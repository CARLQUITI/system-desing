"""Ejemplo resuelto 2: Abstract Factory para las dos sedes de ReservaU.

Corre esto para ver la familia completa en accion, para cada sede:

    python3 fabrica_de_campus.py
"""


class ValidadorDeHorario:
    def horario_valido(self, hora_inicio, hora_fin):
        raise NotImplementedError


class ValidadorDeHorarioNorte(ValidadorDeHorario):
    def horario_valido(self, hora_inicio, hora_fin):
        return 6 <= hora_inicio and hora_fin <= 22


class ValidadorDeHorarioSur(ValidadorDeHorario):
    def horario_valido(self, hora_inicio, hora_fin):
        return 7 <= hora_inicio and hora_fin <= 23


class Notificador:
    def enviar(self, mensaje):
        raise NotImplementedError


class NotificadorCampusNorte(Notificador):
    def enviar(self, mensaje):
        return "[Campus Norte] " + mensaje


class NotificadorCampusSur(Notificador):
    def enviar(self, mensaje):
        return "[Campus Sur] " + mensaje


class FabricaDeCampus:
    def crear_validador(self):
        raise NotImplementedError

    def crear_notificador(self):
        raise NotImplementedError


class FabricaCampusNorte(FabricaDeCampus):
    def crear_validador(self):
        return ValidadorDeHorarioNorte()

    def crear_notificador(self):
        return NotificadorCampusNorte()


class FabricaCampusSur(FabricaDeCampus):
    def crear_validador(self):
        return ValidadorDeHorarioSur()

    def crear_notificador(self):
        return NotificadorCampusSur()


def procesar_reserva(fabrica, hora_inicio, hora_fin):
    validador = fabrica.crear_validador()
    notificador = fabrica.crear_notificador()
    if not validador.horario_valido(hora_inicio, hora_fin):
        return notificador.enviar("horario fuera del rango permitido en esta sede")
    return notificador.enviar("reserva confirmada")


if __name__ == "__main__":
    print(procesar_reserva(FabricaCampusNorte(), 6, 22))
    print(procesar_reserva(FabricaCampusSur(), 6, 22))
    print(procesar_reserva(FabricaCampusSur(), 7, 23))
