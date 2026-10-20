# Semana 4, Sesión 2: Diagramas UML de Comportamiento: Secuencia, Actividad y Máquina de Estados

> Objetivo de la sesión: elegir el diagrama UML de comportamiento adecuado (secuencia, actividad o máquina de estados) según lo que se necesite comunicar de un caso de uso del sistema propio.

**Lectura previa de esta sesión:** [Undervaluation of UML Diagrams and an Introduction to Sequence Diagrams (Medium)](https://medium.com/@nandinigupta_productmgt/undervaluation-of-uml-diagrams-and-an-introduction-to-sequence-diagrams-with-functional-example-4259bf498e66)

**Referencia de esta sesión:** [Choosing the Right UML Diagram: State, Sequence, or Activity Diagrams (Visual Paradigm)](https://guides.visual-paradigm.com/choosing-the-right-uml-diagram-state-diagrams-sequence-diagrams-or-activity-diagrams/)

Esta sesión no tiene código. Seguimos con ReservaU: hoy tomamos las clases del diagrama de robustez de la sesión pasada y las miramos con tres diagramas distintos, cada uno pensado para responder una pregunta diferente.

## Notación

**Diagrama de secuencia** (texto plano):

```
Secuencia: <nombre del caso de uso>

Lifelines: <objeto> : <tipo (Actor/Frontera/Control/Entidad)>, ...

1. <objeto emisor> → <objeto receptor>: <mensaje>
2. <objeto receptor> -->> <objeto emisor>: <respuesta>
...

alt <condición del flujo alterno>
    N.a.1 <objeto> → <objeto>: <mensaje>
end
```

`→` es un mensaje síncrono (una llamada). `-->>` es una respuesta. `alt` encierra un flujo alterno.

**Diagrama de actividad** (texto plano):

```
Actividad: <nombre del proceso>

(●) inicio
[<acción>]
<¿condición?>
  --sí--> [<acción>] --> (◉) fin
  --no--> [<acción>] --> (◉) fin
```

**Máquina de estados** (texto plano):

```
Máquina de estados: <entidad>

(●) inicio → [<estado inicial>]
[<estado>] --<evento>() [<guarda>]--> [<estado>]
[<estado>] → (◉) fin
```

## Sobre la lectura previa

El artículo argumenta que los diagramas UML están subvalorados, y que un diagrama de secuencia sirve a audiencias distintas de quien programa. Según el artículo, ¿a qué otro rol, además de quien programa, le sirve un diagrama de secuencia, y para qué lo usa?

_(tu respuesta)_

## Ejercicio 1: secuencia de "Reservar una cancha"
Antes de que yo lo resuelva: en tu diagrama de robustez de la sesión pasada, ¿el control llama primero a `Cancha`/`Reserva`, o llama primero a la frontera para confirmar algo con el estudiante?

_(tu respuesta)_

## Ejercicio 2: actividad del mismo flujo
Antes de que yo lo resuelva: si tuvieras que explicarle este flujo a alguien que no conoce ninguna de tus clases, ¿usarías el diagrama de secuencia del Ejercicio 1 o preferirías otro tipo de diagrama? ¿Por qué?

_(tu respuesta)_

## Ejercicio 3: secuencia y máquina de estados de "Cancelar una reserva"

### Parte A: diagrama de secuencia

Construye el diagrama de secuencia completo de "Cancelar una reserva" (Sesión 3.1), reutilizando las clases del diagrama de robustez que construiste en la Sesión 4.1 (Ejercicio 2). Incluye el flujo alterno de no-show.

```
Secuencia: Cancelar una reserva

Lifelines: Estudiante : Actor, PantallaDeCancelacion : Frontera,
           ControladorDeCancelacion : Control, Reserva : Entidad

1.
2.
3.
```

### Parte B: máquina de estados de `Reserva`

Construye la máquina de estados completa de `Reserva`, a partir de lo que ya sabes de `Reserva.cancelar(hora_actual)` (Sesión 3.2) y del atributo `estado` de la entidad.

```
Máquina de estados: Reserva

(●) inicio → [Activa]
[Activa] --cancelar() [ ]--> [        ]
[Activa] --cancelar() [ ]--> [        ]
[Activa] --                --> [Completada]
[        ] → (◉) fin
[        ] → (◉) fin
[Completada] → (◉) fin
```

Completa las guardas y los estados que faltan. Necesitas cubrir, como mínimo, los tres destinos posibles de una reserva activa: cancelación regular, no-show, y el caso en que la reserva simplemente se completa sin que nadie la cancele.

### Checklist final

- [ ] El diagrama de secuencia usa las mismas clases del diagrama de robustez de la Sesión 4.1, sin clases nuevas.
- [ ] El flujo alterno de no-show aparece en el diagrama de secuencia dentro de un recuadro `alt`.
- [ ] La máquina de estados distingue `Cancelada` de `NoShow` con la misma guarda (faltan menos de 2 horas) que ya usa `Reserva.cancelar(hora_actual)`, sin inventar una condición nueva.
- [ ] La máquina de estados incluye un estado para cuando la reserva se completa sin cancelación.

## Antes de la próxima sesión

En tu diagrama de robustez o de secuencia de esta semana, ¿qué parte del control tendrías que cambiar si mañana ReservaU agrega un tercer tipo de reserva, además de la regular y la de prioridad?

_(tu respuesta)_
