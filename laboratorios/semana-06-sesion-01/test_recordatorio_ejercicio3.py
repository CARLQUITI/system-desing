"""Corre esto con `pytest test_recordatorio_ejercicio3.py` antes de
dar por resuelto el Ejercicio 3.
"""

from recordatorio_ejercicio3 import (
    Estudiante,
    EquipoOficial,
    RecordatorioEstudiante,
    RecordatorioEquipoOficial,
    elegir_politica_de_recordatorio,
    calcular_hora_de_envio,
)


def test_recordatorio_estudiante_es_una_hora_antes():
    assert RecordatorioEstudiante().horas_de_anticipacion() == 1


def test_recordatorio_equipo_oficial_es_3_horas_antes():
    assert RecordatorioEquipoOficial().horas_de_anticipacion() == 3


def test_estudiante_recibe_politica_de_una_hora():
    politica = elegir_politica_de_recordatorio(Estudiante("Ana"))
    assert isinstance(politica, RecordatorioEstudiante)


def test_equipo_oficial_recibe_politica_de_3_horas():
    politica = elegir_politica_de_recordatorio(EquipoOficial("Voleibol A"))
    assert isinstance(politica, RecordatorioEquipoOficial)


def test_calcular_hora_de_envio_para_estudiante():
    assert calcular_hora_de_envio(18, Estudiante("Ana")) == 17


def test_calcular_hora_de_envio_para_equipo_oficial():
    assert calcular_hora_de_envio(18, EquipoOficial("Voleibol A")) == 15
