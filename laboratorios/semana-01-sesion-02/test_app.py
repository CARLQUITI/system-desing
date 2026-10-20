"""Corre esto con `pytest test_app.py` antes de pasar al Ejercicio 2 (Docker).

Si estos dos tests no pasan, tu funcion espacios_disponibles todavia no
esta lista, y el contenedor va a fallar por el mismo motivo.
"""

from app import espacios_disponibles


def test_espacios_disponibles_cuenta_los_no_ocupados():
    espacios = [
        {"id": 1, "ocupado": False},
        {"id": 2, "ocupado": True},
        {"id": 3, "ocupado": False},
    ]
    assert espacios_disponibles(espacios) == 2


def test_espacios_disponibles_lista_vacia():
    assert espacios_disponibles([]) == 0


def test_espacios_disponibles_todos_ocupados():
    espacios = [{"id": 1, "ocupado": True}, {"id": 2, "ocupado": True}]
    assert espacios_disponibles(espacios) == 0
