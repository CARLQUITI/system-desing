"""Una base de datos de ReservaU con una primaria y una replica, con
replicacion asincronica. Ya esta completa: no la modifiques.

escribir(...) guarda la reserva solo en la primaria y la deja en la
lista "pendientes". La replica recien la recibe cuando alguien llama a
replicar(), que en un sistema real ocurre por su cuenta, unos
milisegundos o unos segundos despues: ese intervalo es el retraso de
replicacion.

Cada lectura cuenta en que nodo se hizo, para poder medir cuanta carga
le quita la replica a la primaria.
"""


class BaseReplicada:
    def __init__(self):
        self.primaria = []
        self.replica = []
        self.pendientes = []
        self.lecturas_en_primaria = 0
        self.lecturas_en_replica = 0

    def escribir(self, reserva):
        self.primaria.append(reserva)
        self.pendientes.append(reserva)

    def replicar(self):
        for reserva in self.pendientes:
            self.replica.append(reserva)
        self.pendientes = []

    def leer_de_primaria(self):
        self.lecturas_en_primaria = self.lecturas_en_primaria + 1
        return self.primaria

    def leer_de_replica(self):
        self.lecturas_en_replica = self.lecturas_en_replica + 1
        return self.replica

    def tiene_escrituras_pendientes_de(self, id_estudiante):
        for reserva in self.pendientes:
            if reserva.id_estudiante == id_estudiante:
                return True
        return False
