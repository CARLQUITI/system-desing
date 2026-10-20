# Semana 6, Sesión 1: ReservaU con patrón Strategy: políticas de prioridad y cancelación

> Objetivo de la sesión: aplicar el patrón Strategy a ReservaU para intercambiar políticas de prioridad o de cancelación sin modificar el código cliente.

**Lectura previa de esta sesión:** [Strategy Pattern: Because Your Giant if Statement Is Crying for Help (Medium)](https://ingelbrechtrobin.medium.com/strategy-pattern-because-your-giant-if-statement-is-crying-for-help-48e979d9a399)

**Referencia de esta sesión:** [Strategy (Refactoring.Guru)](https://refactoring.guru/design-patterns/strategy)

## Antes de empezar

Entra a esta carpeta y corre el ejemplo de partida:

```
cd laboratorios/semana-06-sesion-01
python3 prioridad_sin_strategy.py
```

Mira las 4 líneas de salida: la política de prioridad de 3 tipos de solicitante, todas decididas dentro del mismo método. Con eso arrancamos la discusión de hoy.

## Respuesta sobre la lectura

Antes de que se abra la discusión: según el artículo, ¿qué gana el código cuando cada rama de un if enorme se convierte en su propia clase, más allá de "queda más corto"?

_(tu respuesta)_

## Ejercicio 1: Strategy para la política de prioridad
Este ejercicio se resuelve en vivo, sobre `prioridad_sin_strategy.py`. Antes de que se muestre el refactor, responde:

**Respuesta 1:** con el diseño actual de `Reserva.es_prioritaria`, ¿qué línea de código hay que tocar si ReservaU agrega una cuarta política de prioridad?

_(tu respuesta)_

**Respuesta 2:** después del refactor con Strategy, ¿qué archivo o función esperas que sea el único lugar con un `isinstance`?

_(tu respuesta)_

## Ejercicio 2: Strategy para la política de cancelación
Seguimos con `cancelacion_sin_strategy.py`, donde `Reserva.cancelar` mezcla la regla de las 2 horas con un caso especial para el administrador.

**Respuesta 1:** antes de ver el refactor, ¿por qué un administrador que cancela por mantenimiento no debería generar un no-show?

_(tu respuesta)_

**Respuesta 2:** ¿qué gana `Reserva.cancelar` cuando pasa de tener el if/else adentro a delegar en `self.politica_cancelacion.resolver(...)`?

_(tu respuesta)_

## Ejercicio 3: Strategy para la política de recordatorio

Ahora te toca aplicar el mismo patrón a una decisión distinta: `recordatorio_ejercicio3.py` decide con cuántas horas de anticipación se envía el recordatorio de una reserva, con 4 TODOs.

1. Completa los TODOs 1 y 2: `RecordatorioEstudiante.horas_de_anticipacion()` retorna 1, `RecordatorioEquipoOficial.horas_de_anticipacion()` retorna 3.
2. Resuelve el TODO 3: `elegir_politica_de_recordatorio(solicitante)`, que retorna `RecordatorioEstudiante` para un `Estudiante` y `RecordatorioEquipoOficial` para un `EquipoOficial` (usa `isinstance`, igual que en los dos ejercicios anteriores).
3. Resuelve el TODO 4: `calcular_hora_de_envio(hora_inicio, solicitante)`, que retorna `hora_inicio` menos las horas de anticipación de la política correcta.
4. Corre las pruebas:
   ```
   pytest test_recordatorio_ejercicio3.py
   ```
5. Antes de dar por terminado el ejercicio, revisa: ¿tocaste una sola línea de `RecordatorioEstudiante` o `RecordatorioEquipoOficial` para que `calcular_hora_de_envio` funcione? Si sí, tu diseño todavía depende de un `isinstance` disperso en vez de Strategy.

### Checklist final

- [ ] `RecordatorioEstudiante.horas_de_anticipacion()` retorna 1 y `RecordatorioEquipoOficial.horas_de_anticipacion()` retorna 3.
- [ ] `elegir_politica_de_recordatorio` retorna la política correcta según el tipo de `solicitante`, sin un `isinstance` adicional en ninguna otra función del archivo.
- [ ] `calcular_hora_de_envio` usa `elegir_politica_de_recordatorio`, no un `isinstance` propio.
- [ ] Los 6 tests de `test_recordatorio_ejercicio3.py` pasan.

## Antes de la próxima sesión

Hoy `Reserva` decide su propia prioridad y su propia cancelación con una política intercambiable, pero para completar una reserva, el código cliente todavía tiene que hablar por separado con el verificador de disponibilidad, el calendario de la cancha y el notificador. ¿Qué le pasa a ese código cliente si mañana tiene que hablar directamente con esos 3 subsistemas, cada uno con su propia forma de llamarse?

_(tu respuesta)_
