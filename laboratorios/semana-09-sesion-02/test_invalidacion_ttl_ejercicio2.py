from repositorio import RepositorioDeReservas
from reloj import RelojSimulado
from invalidacion_ttl_ejercicio2 import ServicioConInvalidacionYTTL


def servicio_nuevo(ttl=30):
    repositorio = RepositorioDeReservas(latencia=0)
    reloj = RelojSimulado()
    return repositorio, reloj, ServicioConInvalidacionYTTL(repositorio, reloj, ttl)


def test_antes_de_vencer_responde_desde_el_cache():
    repositorio, reloj, servicio = servicio_nuevo()
    servicio.disponibilidad("Cancha 1", "2026-10-26")
    reloj.avanzar(29)
    servicio.disponibilidad("Cancha 1", "2026-10-26")
    assert repositorio.consultas == 1
    assert servicio.aciertos == 1


def test_al_vencer_vuelve_al_repositorio():
    repositorio, reloj, servicio = servicio_nuevo()
    servicio.disponibilidad("Cancha 1", "2026-10-26")
    reloj.avanzar(30)
    servicio.disponibilidad("Cancha 1", "2026-10-26")
    assert repositorio.consultas == 2
    assert servicio.fallos == 2


def test_reservar_invalida_y_la_siguiente_consulta_ve_la_reserva():
    repositorio, reloj, servicio = servicio_nuevo()
    assert 18 in servicio.disponibilidad("Cancha 1", "2026-10-26")
    assert servicio.reservar("Cancha 1", "2026-10-26", 18) is True
    assert 18 not in servicio.disponibilidad("Cancha 1", "2026-10-26")


def test_reservar_solo_invalida_la_cancha_y_fecha_afectadas():
    repositorio, reloj, servicio = servicio_nuevo()
    servicio.disponibilidad("Cancha 1", "2026-10-26")
    servicio.disponibilidad("Cancha 2", "2026-10-26")
    servicio.reservar("Cancha 1", "2026-10-26", 18)
    consultas_antes = repositorio.consultas
    servicio.disponibilidad("Cancha 2", "2026-10-26")
    assert repositorio.consultas == consultas_antes


def test_no_acepta_una_hora_ya_reservada_aunque_el_cache_este_viejo():
    repositorio, reloj, servicio = servicio_nuevo()
    servicio.disponibilidad("Cancha 1", "2026-10-26")
    repositorio.registrar_reserva("Cancha 1", "2026-10-26", 18)
    assert servicio.reservar("Cancha 1", "2026-10-26", 18) is False


def test_reservar_sin_entrada_en_cache_no_falla():
    repositorio, reloj, servicio = servicio_nuevo()
    assert servicio.reservar("Cancha 3", "2026-10-26", 9) is True
