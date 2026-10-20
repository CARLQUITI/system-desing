"""Extiende CalendarioDeCancha con un numero de version, para locking
optimista: en vez de bloquear a todos los demas mientras se verifica
y se registra (locking pesimista), cada solicitud verifica sin ningun
lock, y solo al final confirma con una escritura muy corta y atomica
que compara la version que leyo contra la version actual.
"""

import threading


class CalendarioDeCanchaConVersion:
    def __init__(self):
        self.reservas = []
        self.version = 0
        self._lock_interno = threading.Lock()

    def intentar_registrar_con_version(self, reserva, version_leida):
        # Seccion critica minima: solo compara y escribe, nunca
        # verifica disponibilidad aqui dentro. Esto es lo que hace que
        # el locking sea "optimista": el lock protege una operacion de
        # un solo paso (comparar version y escribir), no el flujo
        # completo de verificar-y-registrar como en el Ejercicio 2.
        self._lock_interno.acquire()
        if self.version != version_leida:
            self._lock_interno.release()
            return False
        self.reservas.append(reserva)
        self.version = self.version + 1
        self._lock_interno.release()
        return True
