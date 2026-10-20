from servidor import Servidor, simular_trafico
from balanceador_ejercicio2 import BalanceadorRoundRobin
from menos_conexiones_ejercicio3 import BalanceadorMenosConexiones

# Trafico mixto de ReservaU: cada solicitud larga (10 segundos, generar
# el reporte semestral de una cancha) va seguida de una corta (1 segundo,
# consultar disponibilidad).
TRAFICO_MIXTO = [10, 1, 10, 1, 10, 1, 10, 1]


def dos_servidores():
    return [Servidor("a", 10), Servidor("b", 10)]


def test_elige_el_servidor_con_menos_conexiones():
    servidores = dos_servidores()
    servidores[0].atender(10)
    servidores[0].atender(10)
    balanceador = BalanceadorMenosConexiones(servidores)
    assert balanceador.enviar(10) == "b"


def test_en_empate_gana_el_primero_de_la_lista():
    balanceador = BalanceadorMenosConexiones(dos_servidores())
    assert balanceador.enviar(10) == "a"


def test_ignora_un_servidor_caido_aunque_este_vacio():
    servidores = dos_servidores()
    servidores[0].atender(10)
    servidores[1].caer()
    balanceador = BalanceadorMenosConexiones(servidores)
    assert balanceador.enviar(10) == "a"
    assert servidores[1].perdidas == 0


def test_devuelve_none_si_nadie_puede_atender():
    servidores = [Servidor("a", 1)]
    balanceador = BalanceadorMenosConexiones(servidores)
    assert balanceador.enviar(10) == "a"
    assert balanceador.enviar(10) is None


def test_round_robin_amontona_las_solicitudes_largas_en_un_servidor():
    servidores = dos_servidores()
    simular_trafico(BalanceadorRoundRobin(servidores), servidores, TRAFICO_MIXTO)
    assert servidores[0].conexiones_activas() == 4
    assert servidores[1].conexiones_activas() == 0


def test_menos_conexiones_reparte_las_solicitudes_largas():
    servidores = dos_servidores()
    simular_trafico(BalanceadorMenosConexiones(servidores), servidores, TRAFICO_MIXTO)
    assert servidores[0].conexiones_activas() == 2
    assert servidores[1].conexiones_activas() == 2
