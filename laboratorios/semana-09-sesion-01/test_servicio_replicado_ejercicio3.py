from base_replicada import BaseReplicada
from servicio_replicado_ejercicio3 import ServicioDeReservasReplicado


def servicio_nuevo():
    base = BaseReplicada()
    return base, ServicioDeReservasReplicado(base)


def test_no_acepta_dos_reservas_del_mismo_horario_antes_de_replicar():
    base, servicio = servicio_nuevo()
    primera = servicio.reservar("est-0001", "Campus Norte", "Cancha 1", "2026-10-19", 18)
    segunda = servicio.reservar("est-0002", "Campus Norte", "Cancha 1", "2026-10-19", 18)
    assert primera is not None
    assert segunda is None
    assert len(base.primaria) == 1


def test_quien_acaba_de_reservar_ve_su_reserva_antes_de_replicar():
    base, servicio = servicio_nuevo()
    servicio.reservar("est-0001", "Campus Norte", "Cancha 1", "2026-10-19", 18)
    assert len(base.replica) == 0
    assert len(servicio.mis_reservas("est-0001")) == 1


def test_sin_escrituras_pendientes_mis_reservas_lee_de_la_replica():
    base, servicio = servicio_nuevo()
    servicio.reservar("est-0001", "Campus Norte", "Cancha 1", "2026-10-19", 18)
    base.replicar()
    lecturas_antes = base.lecturas_en_primaria
    assert len(servicio.mis_reservas("est-0001")) == 1
    assert base.lecturas_en_primaria == lecturas_antes
    assert base.lecturas_en_replica == 1


def test_otro_estudiante_lee_de_la_replica_aunque_haya_pendientes():
    base, servicio = servicio_nuevo()
    servicio.reservar("est-0001", "Campus Norte", "Cancha 1", "2026-10-19", 18)
    lecturas_antes = base.lecturas_en_primaria
    assert servicio.mis_reservas("est-0002") == []
    assert base.lecturas_en_primaria == lecturas_antes


def test_el_reporte_de_ocupacion_lee_de_la_replica():
    base, servicio = servicio_nuevo()
    servicio.reservar("est-0001", "Campus Norte", "Cancha 1", "2026-10-19", 18)
    servicio.reservar("est-0002", "Campus Sur", "Cancha 1", "2026-10-19", 18)
    base.replicar()
    lecturas_antes = base.lecturas_en_primaria
    assert servicio.ocupacion_del_campus("Campus Norte") == 1
    assert base.lecturas_en_primaria == lecturas_antes
