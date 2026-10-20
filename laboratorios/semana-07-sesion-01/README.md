# Semana 7, Sesión 1: ReservaU bajo concurrencia: evitar la doble reserva del mismo horario

> Objetivo de la sesión: diagnosticar una condición de carrera al reservar la misma cancha y el mismo horario simultáneamente, y elegir entre locking optimista y pesimista según el nivel de contención esperado.

**Lectura previa de esta sesión:** [When Millions Click at Once: How Pessimistic Locking Prevents Double Booking in High-Traffic Systems (Medium)](https://medium.com/@niketl16/when-millions-click-at-once-how-pessimistic-locking-prevents-double-booking-in-high-traffic-2e9d3b109b19)

**Referencia de esta sesión:** [Explicit Locking, cap. 13.3 (PostgreSQL Docs)](https://www.postgresql.org/docs/current/explicit-locking.html)

## Antes de empezar

Entra a esta carpeta:

```
cd laboratorios/semana-07-sesion-01
```

`disponibilidad.py` y `calendario.py` son exactamente el `VerificadorDeDisponibilidad` y el `CalendarioDeCancha` de la Semana 6: el mismo camino de código que ya usa `FacadeDeReservas.reservar(...)` para verificar y registrar una reserva. Hoy ese camino es el problema.

## Respuesta sobre la lectura

El artículo distingue el locking pesimista (bloquear el recurso antes de tocarlo) del optimista (verificar el conflicto solo al final, sin bloquear nada mientras tanto). Según el artículo, ¿en un escenario de alta contención (muchas solicitudes compitiendo por el mismo recurso al mismo tiempo), cuál de los dos evita más trabajo desperdiciado en reintentos?

_(tu respuesta)_

## Respuesta sobre la pregunta de la sesión pasada

Dos estudiantes intentan reservar la misma cancha, el mismo horario, casi al mismo instante. `VerificadorDeDisponibilidad.esta_disponible(...)` responde que sí a ambos antes de que ninguna de las dos reservas se haya registrado todavía. ¿Qué tendría que pasar distinto para que solo una de las dos reservas termine confirmada?

_(tu respuesta)_

## Ejercicio 1: Reproducir la condición de carrera

Este ejercicio se resuelve en vivo, sobre `race_condicion_ejercicio1.py`. Antes de que se muestre el resultado, responde:

**Respuesta 1:** si dos hilos llaman a `esta_disponible(...)` para la misma cancha y el mismo horario, y ninguno de los dos ha llamado todavía a `calendario.registrar(...)`, ¿qué le responde `esta_disponible` al segundo hilo?

_(tu respuesta)_

**Respuesta 2:** después de correr `python3 race_condicion_ejercicio1.py`, ¿cuántas reservas activas y superpuestas quedan en el calendario para esa cancha y ese horario?

_(tu respuesta)_

## Ejercicio 2: Evitar la doble reserva con locking pesimista

Ahora te toca a ti. `reserva_pesimista_ejercicio2.py` trae la clase `ReservadorPesimista` con un `threading.Lock` ya creado en `__init__`, y un método `reservar(...)` sin terminar.

1. Completa `reservar(...)`: adquiere `self.lock` antes de verificar disponibilidad, agrega `time.sleep(0.05)` entre la verificación y el registro, y libera `self.lock` en cada punto en el que la función retorna.
2. Corre las pruebas:
   ```
   pytest test_reserva_pesimista_ejercicio2.py
   ```
3. Antes de dar por terminado el ejercicio, responde: mientras un hilo tiene `self.lock` tomado dentro de `reservar(...)`, ¿qué hace un segundo hilo que llama a `reservar(...)` al mismo tiempo?

_(tu respuesta)_

## Ejercicio 3: Evitar la doble reserva con locking optimista

El ejercicio más exigente de los tres. `reserva_optimista_ejercicio3.py` trae la clase `ReservadorOptimista`, que usa `CalendarioDeCanchaConVersion` (en `calendario_con_version.py`, ya completo: no lo modifiques) en vez de `CalendarioDeCancha`. `intentar_registrar_con_version(reserva, version_leida)` ya hace la comparación atómica de la versión; tu trabajo es usarla en el orden correcto dentro de `reservar(...)`.

1. Completa `reservar(...)` siguiendo los 4 pasos comentados en el archivo: lee la versión antes de verificar nada, verifica disponibilidad sin ningún lock, simula el tiempo de procesamiento, e intenta registrar comparando contra la versión que leíste al inicio.
2. Corre las pruebas:
   ```
   pytest test_reserva_optimista_ejercicio3.py
   ```
3. Responde, con lo que mediste en tus propias pruebas: en ReservaU, donde muchos estudiantes intentan reservar las canchas más populares apenas se abre el horario (alta contención), ¿cuál de los dos, locking optimista o pesimista, deja a menos estudiantes con una solicitud rechazada por conflicto en vez de por falta de disponibilidad real?

_(tu respuesta)_

### Checklist final

- [ ] `ReservadorPesimista.reservar` adquiere `self.lock` antes de verificar disponibilidad y lo libera en cada retorno.
- [ ] `ReservadorOptimista.reservar` lee `self.calendario.version` antes de verificar disponibilidad, no después.
- [ ] `ReservadorOptimista.reservar` nunca llama a `self.calendario.reservas.append(...)` directamente: toda escritura pasa por `intentar_registrar_con_version(...)`.
- [ ] Corriendo cada prueba varias veces seguidas, ninguna de las dos soluciones deja pasar dos reservas superpuestas.
- [ ] Los tests de `test_reserva_pesimista_ejercicio2.py` y `test_reserva_optimista_ejercicio3.py` pasan.

## Antes de la próxima sesión

La próxima sesión es el Repaso de medio semestre, sin lectura nueva. Trae una duda concreta sobre tu propio PSet 1 o PSet 2 (una decisión de diseño que no te quedó clara, un error que no lograste resolver): la clase la resuelve en conjunto.
