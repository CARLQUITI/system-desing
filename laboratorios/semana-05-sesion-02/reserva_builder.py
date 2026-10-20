"""Ejemplo resuelto 1: constructor telescopico vs Builder.

Corre esto para comparar ambas formas de construir la misma reserva:

    python3 reserva_builder.py
"""


class ReservaCompleja:
    def __init__(self, cancha, fecha, hora_inicio, hora_fin, solicitante,
                 recurrente=False, semanas_de_recurrencia=1,
                 equipo_prestado=None, notas=""):
        if equipo_prestado is None:
            equipo_prestado = []
        self.cancha = cancha
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.solicitante = solicitante
        self.recurrente = recurrente
        self.semanas_de_recurrencia = semanas_de_recurrencia
        self.equipo_prestado = equipo_prestado
        self.notas = notas

    def resumen(self):
        texto = self.cancha + ", " + self.fecha + " " + self.hora_inicio + "-" + self.hora_fin
        if self.recurrente:
            texto = texto + " | recurrente por " + str(self.semanas_de_recurrencia) + " semanas"
        if self.equipo_prestado:
            texto_equipo = ""
            for item in self.equipo_prestado:
                if texto_equipo == "":
                    texto_equipo = item
                else:
                    texto_equipo = texto_equipo + ", " + item
            texto = texto + " | equipo prestado: " + texto_equipo
        if self.notas:
            texto = texto + " | notas: " + self.notas
        return texto


class ReservaBuilder:
    def __init__(self, cancha, fecha, hora_inicio, hora_fin, solicitante):
        self._cancha = cancha
        self._fecha = fecha
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin
        self._solicitante = solicitante
        self._recurrente = False
        self._semanas_de_recurrencia = 1
        self._equipo_prestado = []
        self._notas = ""

    def con_recurrencia(self, semanas):
        self._recurrente = True
        self._semanas_de_recurrencia = semanas
        return self

    def con_equipo_prestado(self, equipo):
        self._equipo_prestado = equipo
        return self

    def con_notas(self, notas):
        self._notas = notas
        return self

    def construir(self):
        return ReservaCompleja(
            self._cancha, self._fecha, self._hora_inicio, self._hora_fin,
            self._solicitante, self._recurrente, self._semanas_de_recurrencia,
            self._equipo_prestado, self._notas,
        )


if __name__ == "__main__":
    # Constructor telescopico: hay que recordar el orden y el significado
    # de cada posicion, incluidas las que no se van a usar.
    reserva_telescopica = ReservaCompleja(
        "Cancha 3", "2026-10-05", "18:00", "19:00", "Voleibol A",
        True, 4, ["Balon", "Red"], "",
    )
    print("Telescopica:", reserva_telescopica.resumen())

    # Builder: cada paso se nombra, y solo se llama el que aplica.
    reserva_con_builder = (
        ReservaBuilder("Cancha 3", "2026-10-05", "18:00", "19:00", "Voleibol A")
        .con_recurrencia(4)
        .con_equipo_prestado(["Balon", "Red"])
        .construir()
    )
    print("Con Builder:", reserva_con_builder.resumen())
