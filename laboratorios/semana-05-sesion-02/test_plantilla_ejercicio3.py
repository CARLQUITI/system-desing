"""Corre esto con `pytest test_plantilla_ejercicio3.py` antes de dar
por resuelto el Ejercicio 3.
"""

from plantilla_ejercicio3 import ReservaPlantilla, generar_reservas_recurrentes


def _plantilla_base():
    return ReservaPlantilla(
        "Cancha 3", "18:00", "19:00", "Voleibol A",
        equipo_prestado=["Balon"], notas="Practica semanal",
    )


def test_clonar_produce_un_objeto_distinto_con_los_mismos_valores():
    plantilla = _plantilla_base()
    clon = plantilla.clonar()
    assert clon is not plantilla
    assert clon.cancha == plantilla.cancha
    assert clon.equipo_prestado == plantilla.equipo_prestado


def test_clonar_no_comparte_la_lista_equipo_prestado():
    plantilla = _plantilla_base()
    clon = plantilla.clonar()
    clon.agregar_al_equipo_prestado("Red")
    assert "Red" not in plantilla.equipo_prestado
    assert "Red" in clon.equipo_prestado


def test_con_fecha_encadena_y_asigna():
    plantilla = _plantilla_base()
    clon = plantilla.clonar().con_fecha("2026-10-06")
    assert clon.fecha == "2026-10-06"
    assert plantilla.fecha is None


def test_generar_reservas_recurrentes_retorna_una_por_fecha():
    plantilla = _plantilla_base()
    fechas = ["2026-10-06", "2026-10-13", "2026-10-20"]
    reservas = generar_reservas_recurrentes(plantilla, fechas)
    assert len(reservas) == 3
    fechas_generadas = []
    for reserva in reservas:
        fechas_generadas.append(reserva.fecha)
    assert fechas_generadas == fechas


def test_generar_reservas_recurrentes_no_comparte_equipo_prestado_entre_clones():
    plantilla = _plantilla_base()
    reservas = generar_reservas_recurrentes(plantilla, ["2026-10-06", "2026-10-13"])
    reservas[0].agregar_al_equipo_prestado("Red")
    assert "Red" not in reservas[1].equipo_prestado
    assert "Red" not in plantilla.equipo_prestado
