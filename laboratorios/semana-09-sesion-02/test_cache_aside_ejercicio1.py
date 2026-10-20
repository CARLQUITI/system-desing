from repositorio import RepositorioDeReservas
from cache_aside_ejercicio1 import ServicioConCacheAside


def test_50_consultas_iguales_llegan_una_sola_vez_al_repositorio():
    repositorio = RepositorioDeReservas(latencia=0)
    servicio = ServicioConCacheAside(repositorio)
    for _ in range(50):
        servicio.disponibilidad("Cancha 1", "2026-10-26")
    assert repositorio.consultas == 1
    assert servicio.aciertos == 49
    assert servicio.fallos == 1


def test_claves_distintas_no_comparten_entrada():
    repositorio = RepositorioDeReservas(latencia=0)
    servicio = ServicioConCacheAside(repositorio)
    servicio.disponibilidad("Cancha 1", "2026-10-26")
    servicio.disponibilidad("Cancha 2", "2026-10-26")
    servicio.disponibilidad("Cancha 1", "2026-10-27")
    assert repositorio.consultas == 3


def test_sin_invalidacion_el_cache_sirve_un_dato_viejo():
    repositorio = RepositorioDeReservas(latencia=0)
    servicio = ServicioConCacheAside(repositorio)
    servicio.disponibilidad("Cancha 1", "2026-10-26")
    repositorio.registrar_reserva("Cancha 1", "2026-10-26", 18)
    assert 18 in servicio.disponibilidad("Cancha 1", "2026-10-26")
