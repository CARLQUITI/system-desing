# Semana 5, Sesión 2: Patrones Creacionales: Abstract Factory, Builder y Prototype

> Objetivo de la sesión: seleccionar entre Abstract Factory, Builder y Prototype según el problema de creación de objetos (familias de productos, construcción paso a paso o clonación), y justificar la elección frente a un constructor telescópico.

**Lectura previa de esta sesión:** [Design Patterns #2: The Builder Pattern and the Telescoping Constructor Anti-pattern (Medium)](https://medium.com/@modestofiguereo/design-patterns-2-the-builder-pattern-and-the-telescoping-constructor-anti-pattern-60a33de7522e)

**Referencia de esta sesión:** [Abstract Factory, Builder, Prototype (Refactoring.Guru)](https://refactoring.guru/design-patterns/abstract-factory)

## Antes de empezar

Entra a esta carpeta y corre el ejemplo de partida:

```
cd laboratorios/semana-05-sesion-02
python3 reserva_builder.py
```

Mira las dos líneas de salida: una reserva construida con un constructor de 8 parámetros y la misma reserva construida con un Builder. Con eso arrancamos la discusión de hoy.

## Respuesta sobre la lectura

Antes de que se abra la discusión: según el artículo, ¿qué hace exactamente el patrón Builder para resolver el problema del constructor telescópico, más allá de "tener menos parámetros"?

_(tu respuesta)_

## Ejercicio 1: Builder para ReservaU
Este ejercicio se resuelve en vivo, sobre `reserva_builder.py`. Antes de que se muestre la comparación completa, responde:

**Respuesta 1:** si no llamas a `con_recurrencia(...)` sobre un `ReservaBuilder`, ¿qué valor queda en `recurrente` de la reserva final?

_(tu respuesta)_

**Respuesta 2:** ¿por qué cada método de `ReservaBuilder` (`con_recurrencia`, `con_equipo_prestado`, `con_notas`) retorna `self` en vez de no retornar nada?

_(tu respuesta)_

## Ejercicio 2: Abstract Factory para las sedes de ReservaU
Seguimos con `fabrica_de_campus.py`, donde Campus Norte y Campus Sur necesitan un validador de horario y un notificador compatibles entre sí.

**Respuesta 1:** antes de ver la solución, ¿qué pasaría si `procesar_reserva` recibiera el validador de una sede y el notificador de otra?

_(tu respuesta)_

**Respuesta 2:** ¿por qué `procesar_reserva` recibe una sola fábrica como parámetro, en vez de recibir el validador y el notificador por separado?

_(tu respuesta)_

## Ejercicio 3: Prototype para reservas recurrentes

Ahora te toca aplicar Prototype: `plantilla_ejercicio3.py` modela una plantilla de reserva recurrente, con 4 TODOs.

1. Completa el TODO 1 (`clonar()`, usando `copy.deepcopy`), el TODO 2 (`con_fecha(fecha)`, que asigna y retorna `self`) y el TODO 3 (`agregar_al_equipo_prestado(item)`, que agrega y retorna `self`).
2. Corre las pruebas:
   ```
   pytest test_plantilla_ejercicio3.py
   ```
3. Cuando los primeros 4 tests pasen, resuelve el TODO 4: `generar_reservas_recurrentes(plantilla, fechas)`, que retorna una lista con un clon de la plantilla por cada fecha, cada uno con su propia fecha asignada.
4. Antes de dar por terminado el ejercicio, revisa: si le agregas un ítem al equipo prestado de una de las reservas generadas, ¿cambia el equipo prestado de la plantilla original o el de las demás reservas de la lista? Si cambia, `clonar()` todavía está haciendo una copia superficial en vez de una copia profunda.

### Checklist final

- [ ] `clonar()` usa `copy.deepcopy`, no una copia superficial ni una asignación directa.
- [ ] `con_fecha` y `agregar_al_equipo_prestado` retornan `self`, permitiendo encadenar llamadas.
- [ ] `generar_reservas_recurrentes` retorna una reserva por cada fecha de la lista recibida.
- [ ] Ninguna reserva generada comparte su lista `equipo_prestado` con la plantilla original ni con las demás reservas generadas.
- [ ] Los 5 tests de `test_plantilla_ejercicio3.py` pasan.

## Antes de la próxima sesión

El PSet 1 ya extrajo la política de prioridad de `EquipoOficial` a su propia clase, por composición, sin nombrar ese movimiento todavía. La próxima sesión le pone nombre. ¿Qué tendría que cambiar en ReservaU si mañana aparece una tercera política de prioridad, además de la actual y la de un estudiante regular, sin esa política estar aislada en su propia clase?

_(tu respuesta)_
