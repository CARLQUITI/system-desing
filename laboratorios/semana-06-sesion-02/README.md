# Semana 6, Sesión 2: ReservaU con patrón Facade: unificar disponibilidad, calendario y notificación

> Objetivo de la sesión: aplicar el patrón Facade para exponer una interfaz simple sobre los subsistemas de disponibilidad, registro en calendario y notificación de ReservaU.

**Lectura previa de esta sesión:** [The Facade Design Pattern: Simplifying Complex Subsystems Through Unified Interfaces (Medium)](https://tobiaslang.medium.com/the-facade-design-pattern-simplifying-complex-subsystems-through-unified-interfaces-a569d0589ac3)

**Referencia de esta sesión:** [Facade (Refactoring.Guru)](https://refactoring.guru/design-patterns/facade)

## Antes de empezar

Entra a esta carpeta y corre el ejemplo de partida:

```
cd laboratorios/semana-06-sesion-02
python3 cliente_sin_facade.py
```

Mira las dos líneas de salida: la primera reserva se confirma, la segunda (misma cancha, mismo horario) se rechaza por disponibilidad. Con eso arrancamos la discusión de hoy.

## Respuesta sobre la lectura

Antes de que se abra la discusión: según el artículo, después de que existe una Facade, ¿el código cliente pierde la posibilidad de hablar directo con un subsistema, o solo deja de ser obligatorio para el caso común?

_(tu respuesta)_

## Respuesta sobre la pregunta de apertura

**Respuesta:** si `registrar_reserva_desde_formulario_web` y `registrar_reserva_desde_conserje` repiten la misma secuencia de 3 llamadas a los subsistemas, ¿qué problema aparece cuando ReservaU necesita agregar un cuarto paso obligatorio al flujo?

_(tu respuesta)_

## Ejercicio 1: Construir la Facade
Este ejercicio se resuelve en vivo, sobre `cliente_sin_facade.py`. Antes de que se muestre la solución, responde:

**Respuesta 1:** ¿qué subsistemas necesita conocer `FacadeDeReservas` para poder ofrecer un método `reservar(...)` completo?

_(tu respuesta)_

**Respuesta 2:** con la Facade ya construida, ¿en cuántos lugares del código hay que agregar un cuarto paso obligatorio (por ejemplo, un log de auditoría)?

_(tu respuesta)_

## Ejercicio 2: Ambos puntos de entrada usando la Facade
Seguimos con los mismos dos puntos de entrada de `cliente_sin_facade.py` (formulario web, registro de conserje), ahora usando `FacadeDeReservas`.

**Respuesta 1:** antes de ver el refactor, ¿qué clases o funciones esperas que ya no aparezcan mencionadas dentro de `registrar_reserva_desde_formulario_web` ni de `registrar_reserva_desde_conserje`?

_(tu respuesta)_

**Respuesta 2:** ¿Facade elimina la lógica de verificar disponibilidad, registrar en el calendario y notificar, o solo cambia dónde vive esa lógica?

_(tu respuesta)_

## Ejercicio 3: Extender la Facade con cancelar

Ahora te toca extender `FacadeDeReservas`: `facade_ejercicio3.py` ya trae `reservar(...)` completo y las clases de política de cancelación de la Semana 6, Sesión 1 (`CancelacionEstandar`, `CancelacionSinPenalidad`, `elegir_politica_de_cancelacion`). Falta un método.

1. Completa el método `cancelar(self, reserva, hora_actual)` de `FacadeDeReservas`: usa `elegir_politica_de_cancelacion(reserva.solicitante)` para obtener la política correcta, guarda el resultado de `politica.resolver(reserva.hora_inicio, hora_actual)` en `reserva.estado`, y notifica ese resultado con `elegir_creador_de_notificador(reserva.solicitante)` usando el mensaje exacto `"tu reserva fue registrada como "` concatenado con `reserva.estado`. El método retorna ese mismo mensaje.
2. Corre las pruebas:
   ```
   pytest test_facade_ejercicio3.py
   ```
3. Antes de dar por terminado el ejercicio, revisa: ¿tu método `cancelar` llama a `elegir_politica_de_cancelacion` y a `elegir_creador_de_notificador`, o reimplementa esa lógica con su propio `isinstance`? Si la reimplementa, no estás reutilizando el Strategy de la sesión pasada.

### Checklist final

- [ ] `cancelar` usa `elegir_politica_de_cancelacion(reserva.solicitante)`, sin repetir la lógica de la política con un `isinstance` propio.
- [ ] `reserva.estado` queda actualizado con el resultado de `politica.resolver(...)` antes de construir el mensaje de notificación.
- [ ] El mensaje de notificación es exactamente `"tu reserva fue registrada como "` concatenado con `reserva.estado`.
- [ ] Después de cancelar, `verificador.esta_disponible(...)` vuelve a retornar `True` para ese mismo horario.
- [ ] Los 5 tests de `test_facade_ejercicio3.py` pasan.

## Antes de la próxima sesión

Dos estudiantes intentan reservar la misma cancha, el mismo horario, casi al mismo instante. `VerificadorDeDisponibilidad.esta_disponible(...)` responde que sí a ambos antes de que ninguna de las dos reservas se haya registrado todavía. ¿Qué tendría que pasar distinto para que solo una de las dos reservas termine confirmada?

_(tu respuesta)_
