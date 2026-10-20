from datos_reservas import generar_reservas
from cluster_por_hash_ejercicio2 import ClusterPorHash, fraccion_que_cambia_de_shard


def cluster_cargado():
    cluster = ClusterPorHash(4)
    for reserva in generar_reservas():
        cluster.insertar(reserva)
    return cluster


def test_ningun_shard_supera_el_30_por_ciento():
    tamanos = cluster_cargado().tamanos()
    assert sum(tamanos) == 1000
    assert max(tamanos) <= 300


def test_el_mismo_estudiante_cae_siempre_en_el_mismo_shard():
    cluster = ClusterPorHash(4)
    assert cluster.shard_de("est-0042") == cluster.shard_de("est-0042")


def test_consulta_de_un_estudiante_revisa_un_solo_shard():
    cluster = cluster_cargado()
    encontradas, shards_consultados = cluster.reservas_de_estudiante("est-0008")
    assert shards_consultados == 1
    assert len(encontradas) == 4
    for reserva in encontradas:
        assert reserva.id_estudiante == "est-0008"


def test_consulta_de_una_cancha_revisa_todos_los_shards():
    cluster = cluster_cargado()
    encontradas, shards_consultados = cluster.reservas_de_cancha("Campus Norte", "Cancha 3", "2026-10-20")
    assert shards_consultados == 4
    esperadas = 0
    for reserva in generar_reservas():
        if reserva.campus == "Campus Norte" and reserva.cancha == "Cancha 3" and reserva.fecha == "2026-10-20":
            esperadas = esperadas + 1
    assert len(encontradas) == esperadas


def test_pasar_de_4_a_5_shards_mueve_la_mayoria_de_las_claves():
    claves = []
    for reserva in generar_reservas():
        if reserva.id_estudiante not in claves:
            claves.append(reserva.id_estudiante)
    fraccion = fraccion_que_cambia_de_shard(claves, 4, 5)
    assert 0.7 < fraccion < 0.9
