"""Corre esto con `pytest test_vehiculo.py` antes de dar por resuelto el
Ejercicio 3. El TODO 5 (la clase Avion) no tiene test aca porque el
nombre de la clase lo eliges tu.
"""

from vehiculo_ejercicio3 import Auto, Bote


def test_auto_conduce_por_carretera():
    assert Auto().mover() == "Conduciendo por carretera."


def test_bote_navega_por_agua():
    assert Bote().mover() == "Navegando por agua."


def test_auto_y_bote_usan_comportamientos_distintos():
    assert Auto().mover() != Bote().mover()
