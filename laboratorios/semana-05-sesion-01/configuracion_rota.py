"""Configuracion global de ReservaU, primera version.

Corre las pruebas con:

    pytest test_configuracion_rota.py -v

Mira el orden en que corren y el resultado de cada una.
"""


class GestorDeConfiguracion:
    _instancia = None

    def __init__(self):
        self.modo_mantenimiento = False
        GestorDeConfiguracion._instancia = self

    @staticmethod
    def obtener_instancia():
        if GestorDeConfiguracion._instancia is None:
            GestorDeConfiguracion()
        return GestorDeConfiguracion._instancia


def reserva_permitida(gestor_config):
    return not gestor_config.modo_mantenimiento
