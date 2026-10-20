# Semana 4, Sesión 1: De Dominio y Casos de Uso a Clases de Diseño: Diagramas de Robustez

> Objetivo de la sesión: construir un diagrama de robustez (método ICONIX) que traduzca un caso de uso y el modelo de dominio en clases de frontera, control y entidad.

**Lectura previa de esta sesión:** [ICONIX Process Today (Medium)](https://delatbabel.medium.com/iconix-process-today-d6ce13d8f964)

**Referencia de esta sesión:** [ICONIX Process (Sparx Systems EA User Guide)](https://sparxsystems.com/enterprise_architect_user_guide/17.1/modeling_domains/iconix_process.html)

Esta sesión no tiene código. Seguimos con ReservaU: hoy traducimos un caso de uso ya escrito (Sesión 3.1) y el modelo de dominio ya validado (Sesión 3.2) a un diagrama de robustez, con clases de frontera, control y entidad.

## Notación

Usamos texto plano, no un dibujo, con este formato:

```
Robustez: <nombre del caso de uso>

Actor: <nombre del actor>
Frontera: <nombre de la clase de frontera>
Control: <nombre de la clase de control>
Entidades: <lista de entidades del modelo de dominio que participan>

Conexiones (flujo principal):
<Actor> (actor) → <Frontera> (frontera)
<Frontera> (frontera) → <Control> (control)
<Control> (control) → <Entidad> (entidad): <qué le pide o qué método invoca>
<Control> (control) → <Frontera> (frontera): <qué le confirma o qué le muestra>

Conexiones (flujos alternos):
<Control> (control) → <lo que corresponda>: <qué pasa en ese flujo alterno>
```

Cada conexión debe respetar una de estas 4 reglas: actor solo con frontera, frontera solo con actor o control, control con frontera/entidad/otro control, entidad solo con control. Ninguna conexión directa entre frontera y entidad, ni entre actor y control o entidad.

## Sobre la lectura previa

El artículo defiende partes del proceso ICONIX aunque cuestiona el valor del diagrama de robustez en sí. Según el autor, ¿qué sí sigue siendo útil del proceso completo, más allá de ese diagrama puntual?

_(tu respuesta)_

## Ejercicio 1: robustez de "Reservar una cancha"
Antes de que yo lo resuelva: ¿qué frontera, qué control y qué entidades necesitas, como mínimo, para cubrir el flujo principal completo de "Reservar una cancha" (Versión 2, Sesión 3.1)?

_(tu respuesta)_

## Ejercicio 2: robustez de "Cancelar una reserva"
Antes de que yo lo resuelva: la decisión de si una cancelación se registra como cancelación regular o como no-show, ¿en qué clase del diagrama debería vivir: en la frontera, en el control, o en la entidad `Reserva`?

_(tu respuesta)_

## Ejercicio 3: robustez de la reserva con prioridad

Construye el diagrama de robustez completo del caso de uso "Reservar con prioridad de equipo oficial", el que documentaste en la Sesión 3.1. Usa el modelo de dominio completo de la Sesión 3.2 (`Cancha`, `Reserva`, `Estudiante`, `EquipoOficial`).

```
Robustez: Reservar con prioridad de equipo oficial

Actor:
Frontera:
Control:
Entidades:

Conexiones (flujo principal):
1.
2.
3.

Conexiones (al menos un flujo alterno):
```

Necesitas cubrir al menos uno de los flujos alternos de tu caso de uso original (conflicto con una reserva individual existente, o conflicto entre dos equipos oficiales).

### Checklist final

- [ ] Cada conexión respeta una de las 4 reglas: actor solo con frontera, frontera solo con actor o control, control con frontera/entidad/otro control, entidad solo con control.
- [ ] Ninguna conexión directa entre frontera y entidad.
- [ ] Las entidades del diagrama son las mismas de tu modelo de dominio de la Sesión 3.2, sin entidades nuevas.
- [ ] La regla de negocio de prioridad se resuelve invocando `EquipoOficial.tiene_prioridad(hora)`, no reimplementándola dentro del control.
- [ ] Al menos un flujo alterno de tu caso de uso original queda representado.

## Antes de la próxima sesión

Mira el diagrama de robustez que acabas de construir. Si tuvieras que mostrar, paso a paso, el orden exacto en que un mensaje viaja de una clase a otra, ¿qué información de tu diagrama de hoy ya no te alcanzaría para mostrarla?

_(tu respuesta)_
