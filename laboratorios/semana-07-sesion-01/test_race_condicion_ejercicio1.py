from race_condicion_ejercicio1 import dos_estudiantes_reservan_la_misma_cancha


def test_las_dos_solicitudes_pasan_la_verificacion():
    _, resultados = dos_estudiantes_reservan_la_misma_cancha()
    assert resultados[0] is not None
    assert resultados[1] is not None


def test_el_calendario_termina_con_dos_reservas_superpuestas():
    calendario, _ = dos_estudiantes_reservan_la_misma_cancha()
    assert len(calendario.reservas) == 2
    primera, segunda = calendario.reservas
    assert primera.estado == "activa"
    assert segunda.estado == "activa"
    assert primera.se_solapa_con(segunda)
