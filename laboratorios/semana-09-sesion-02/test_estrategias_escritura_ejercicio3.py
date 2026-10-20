from repositorio import RepositorioDeReservas
from estrategias_escritura_ejercicio3 import DisponibilidadWriteThrough, VisitasWriteBack


def test_write_through_escribe_en_el_repositorio_al_reservar():
    repositorio = RepositorioDeReservas(latencia=0)
    servicio = DisponibilidadWriteThrough(repositorio)
    servicio.disponibilidad("Cancha 1", "2026-10-26")
    assert servicio.reservar("Cancha 1", "2026-10-26", 18) is True
    assert repositorio.escrituras == 1
    assert 18 not in repositorio.consultar_disponibilidad("Cancha 1", "2026-10-26")


def test_write_through_deja_el_cache_al_dia_sin_volver_a_consultar():
    repositorio = RepositorioDeReservas(latencia=0)
    servicio = DisponibilidadWriteThrough(repositorio)
    servicio.disponibilidad("Cancha 1", "2026-10-26")
    servicio.reservar("Cancha 1", "2026-10-26", 18)
    consultas_antes = repositorio.consultas
    libres = servicio.disponibilidad("Cancha 1", "2026-10-26")
    assert 18 not in libres
    assert repositorio.consultas == consultas_antes


def test_write_through_rechaza_una_hora_ocupada():
    repositorio = RepositorioDeReservas(latencia=0)
    servicio = DisponibilidadWriteThrough(repositorio)
    servicio.reservar("Cancha 1", "2026-10-26", 18)
    assert servicio.reservar("Cancha 1", "2026-10-26", 18) is False


def test_write_back_no_escribe_en_cada_visita():
    repositorio = RepositorioDeReservas(latencia=0)
    visitas = VisitasWriteBack(repositorio)
    for _ in range(100):
        visitas.registrar_visita("Cancha 1")
    assert repositorio.escrituras == 0
    assert visitas.visitas("Cancha 1") == 100


def test_write_back_vacia_con_una_escritura_por_cancha():
    repositorio = RepositorioDeReservas(latencia=0)
    visitas = VisitasWriteBack(repositorio)
    for _ in range(100):
        visitas.registrar_visita("Cancha 1")
    for _ in range(40):
        visitas.registrar_visita("Cancha 2")
    visitas.vaciar()
    assert repositorio.escrituras == 2
    assert repositorio.visitas_de("Cancha 1") == 100
    assert repositorio.visitas_de("Cancha 2") == 40
    assert visitas.visitas("Cancha 1") == 100


def test_write_back_pierde_lo_que_no_alcanzo_a_vaciar():
    repositorio = RepositorioDeReservas(latencia=0)
    visitas = VisitasWriteBack(repositorio)
    for _ in range(100):
        visitas.registrar_visita("Cancha 1")
    visitas.vaciar()
    for _ in range(30):
        visitas.registrar_visita("Cancha 1")
    visitas.caer()
    assert visitas.visitas("Cancha 1") == 100
