"""Ejercicio 3 (lo resuelves tu): el mismo patron de composicion que
viste en los patos, ahora sobre una jerarquia de vehiculos.

Corre las pruebas con:

    pytest test_vehiculo.py

No cambies las firmas de las clases ni los nombres de los metodos: los
tests dependen de que existan exactamente asi.
"""


class ComportamientoMover:
    """Cualquier comportamiento de movimiento implementa mover()."""

    def mover(self):
        raise NotImplementedError


class ConducirPorCarretera(ComportamientoMover):
    def mover(self):
        # TODO 1: retorna el string "Conduciendo por carretera."
        raise NotImplementedError


class NavegarPorAgua(ComportamientoMover):
    def mover(self):
        # TODO 2: retorna el string "Navegando por agua."
        raise NotImplementedError


class Vehiculo:
    def __init__(self, comportamiento_mover):
        self.comportamiento_mover = comportamiento_mover

    def mover(self):
        return self.comportamiento_mover.mover()


class Auto(Vehiculo):
    def __init__(self):
        # TODO 3: llama a super().__init__(...) con el comportamiento
        # de conducir por carretera.
        raise NotImplementedError


class Bote(Vehiculo):
    def __init__(self):
        # TODO 4: llama a super().__init__(...) con el comportamiento
        # de navegar por agua.
        raise NotImplementedError


# TODO 5: la prueba de fuego del patron. Un avion no conduce ni navega:
# vuela. Crea tu propia clase de ComportamientoMover para esto (elige el
# nombre) y una clase Avion(Vehiculo) que la use, siguiendo exactamente
# el mismo patron que Auto y Bote de arriba.
#
# Ninguna de las clases que ya existen en este archivo (ComportamientoMover,
# ConducirPorCarretera, NavegarPorAgua, Vehiculo, Auto, Bote) debe cambiar
# una sola linea para que Avion funcione. Si tuviste que tocar alguna,
# algo en tu diseno todavia depende de herencia en vez de composicion.
