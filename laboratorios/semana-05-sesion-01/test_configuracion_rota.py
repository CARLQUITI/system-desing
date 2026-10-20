from configuracion_rota import GestorDeConfiguracion, reserva_permitida


def test_reserva_rechazada_en_mantenimiento():
    config = GestorDeConfiguracion.obtener_instancia()
    config.modo_mantenimiento = True
    assert reserva_permitida(config) is False


def test_reserva_permitida_en_operacion_normal():
    config = GestorDeConfiguracion.obtener_instancia()
    assert reserva_permitida(config) is True
