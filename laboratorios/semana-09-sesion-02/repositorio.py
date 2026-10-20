"""El almacenamiento persistente de ReservaU (en un sistema real, la base
de datos). Ya esta completo: no lo modifiques.

Cada operacion tarda "latencia" segundos de verdad (time.sleep), para
que la diferencia de tiempo con y sin cache se pueda medir. Los
contadores "consultas" y "escrituras" registran cuantas veces se llego
hasta aqui.
"""

import time

HORAS_DEL_DIA = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


class RepositorioDeReservas:
    def __init__(self, latencia=0.02):
        self.latencia = latencia
        self.ocupadas = {}
        self.visitas = {}
        self.consultas = 0
        self.escrituras = 0

    def consultar_disponibilidad(self, cancha, fecha):
        time.sleep(self.latencia)
        self.consultas = self.consultas + 1
        ocupadas = self.ocupadas.get((cancha, fecha), [])
        libres = []
        for hora in HORAS_DEL_DIA:
            if hora not in ocupadas:
                libres.append(hora)
        return libres

    def registrar_reserva(self, cancha, fecha, hora):
        time.sleep(self.latencia)
        self.escrituras = self.escrituras + 1
        if (cancha, fecha) not in self.ocupadas:
            self.ocupadas[(cancha, fecha)] = []
        self.ocupadas[(cancha, fecha)].append(hora)

    def sumar_visitas(self, cancha, cantidad):
        time.sleep(self.latencia)
        self.escrituras = self.escrituras + 1
        self.visitas[cancha] = self.visitas.get(cancha, 0) + cantidad

    def visitas_de(self, cancha):
        return self.visitas.get(cancha, 0)
