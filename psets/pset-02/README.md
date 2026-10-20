# PSet 2: Patrones de Diseño en ReservaU

ReservaU ya está en uso. Después del PSet 1, dos áreas nuevas de la universidad se reunieron con el equipo de producto. Lo que pidieron forma parte de la especificación de este PSet, junto con todo lo que ya documentaste en el PSet 1.

Partes de tu PSet 1: tus requerimientos, tu modelo de dominio, tus casos de uso y tu código. Este PSet los extiende, no empiezas desde cero.

## El tercer stakeholder: Coordinación de Deportes

Los equipos oficiales entrenan siempre el mismo día y a la misma hora, pero hoy el capitán tiene que reservar semana por semana. Coordinación pide que un capitán pueda hacer una **reserva recurrente**: la misma cancha y el mismo horario durante el número de semanas que él elija, entre 2 y 8. De forma opcional, puede pedir equipo prestado (balones, red, chalecos) y dejar notas para el conserje.

Existe una regla:

> La reserva recurrente es todo o nada. Si una sola semana choca con otra reserva, el sistema no registra ninguna e informa qué semana produjo el conflicto.

Coordinación también cambió las reglas de cancelación, porque un equipo oficial que cancela tarde deja vacía una de las franjas más pedidas:

- Un estudiante mantiene la regla del PSet 1: si cancela con menos de 2 horas de anticipación, se registra no-show.
- Un capitán que cancela una reserva de su equipo con menos de 24 horas de anticipación genera un no-show.
- Cuando el administrador anula una reserva (mantenimiento o conflicto), nunca se registra penalidad para el solicitante.

Y una regla nueva:

> Quien acumule 3 no-shows dentro del mismo mes calendario queda suspendido y no puede crear reservas durante 7 días.

Por último, el administrador organiza torneos y mantenimientos que ocupan varias canchas a la vez, y hoy registra cada bloqueo a mano. Quiere definir un bloqueo una sola vez (motivo, franja horaria y equipo que debe montarse) y replicarlo en varias canchas y fechas, cambiando solo la cancha y la fecha. Si al aplicar un bloqueo ya existen reservas en esa franja, el sistema las anula y notifica a cada afectado.

## El cuarto stakeholder: Dirección de Tecnología

La universidad abrió una segunda sede. ReservaU ahora opera en Campus Norte y Campus Sur, y cada sede tiene sus propias reglas de operación:

| | Campus Norte | Campus Sur |
|---|---|---|
| Horario permitido | 06:00 a 22:00 | 07:00 a 23:00 |
| Canal de notificación | Correo institucional | Mensaje de texto |

Una reserva de Campus Sur nunca debe validarse con el horario de Campus Norte ni notificarse por su canal.

Tecnología también quiere que los valores de las reglas (la hora límite de prioridad, las ventanas de cancelación de 2 y 24 horas, el límite de 3 no-shows y los 7 días de suspensión) vivan en un único lugar del sistema, para cambiarlos sin buscar números repartidos por el código.

Además, reportó un incidente: el primer lunes del semestre, dos estudiantes recibieron confirmación por la misma cancha a la misma hora. Ambos verificaron disponibilidad al mismo tiempo, ambos vieron la cancha libre y ambos registraron su reserva. Esto no puede volver a ocurrir.

Los entregables deben mostrar la transición:

```
Conversación con el stakeholder
↓
Requerimientos
↓
Modelo de dominio y casos de uso
↓
Diagramas de comportamiento
↓
Patrón de diseño
↓
Código
↓
Simulación
↓
Validación
```

Si aplicas un patrón, debes poder explicar qué problema del enunciado resuelve y qué le pasaría a tu código sin él. Un patrón sin un requerimiento que lo justifique es complejidad que nadie pidió.

## Entregables

### 1. Requerimientos

Agrega los requerimientos funcionales y no funcionales que surgen del tercer y del cuarto stakeholder. Continúa la numeración del PSet 1 (si terminaste en RF-08, el primero nuevo es RF-09) y marca cuáles son nuevos y cuáles modificaste.

El incidente de la doble reserva es un requerimiento no funcional. Escríbelo de forma verificable: ¿qué debe ocurrir exactamente cuando dos solicitudes por la misma cancha y franja llegan al mismo tiempo?

### 2. Modelo de dominio y casos de uso

Actualiza tu diagrama de modelo de dominio con las entidades y reglas nuevas: sede, reserva recurrente, bloqueo y suspensión. Las reglas siguen viviendo en la entidad que conoce la información necesaria para aplicarlas. Por ejemplo, ¿quién sabe cuántos no-shows lleva un solicitante este mes?

Actualiza tu diagrama de casos de uso. Como mínimo deben aparecer:

- Reservar de forma recurrente
- Bloquear canchas para un evento
- Cancelar una reserva (modificado)

Crea el diagrama de flujo de cada caso de uso nuevo o modificado, con actor principal, precondiciones, flujo principal y flujos alternos anclados a un paso con la notación número + letra.

### 3. Diagramas de comportamiento

Construye los cuatro diagramas de la Semana 4, cada uno sobre el caso que mejor lo aprovecha:

- **Robustez** de "Cancelar una reserva". Respeta las reglas de conexión de ICONIX: el actor solo habla con clases de frontera y ninguna frontera habla directamente con una entidad.
- **Secuencia** de "Reservar una cancha", con el primer mensaje entrando por tu Facade. Incluye un fragmento `alt` para cada motivo de rechazo: cancha no disponible, solicitante suspendido y horario fuera del permitido por la sede.
- **Actividad** de "Reservar de forma recurrente". Debe mostrar la verificación semana por semana y la decisión de todo o nada.
- **Máquina de estados** de `Reserva`, con estados, eventos y guardas (por ejemplo, `[faltan menos de 2 horas]`). Debe quedar claro desde qué estados una reserva ya no puede cambiar.

Cada diagrama debe coincidir con tus casos de uso: los mismos pasos, en el mismo orden y con los mismos nombres.

### 4. Implementación con patrones

Extiende tu implementación en Python del PSet 1. Siguen sin hacer falta servidor, base de datos, interfaz gráfica, API ni pruebas automatizadas.

Cada patrón responde a un problema del enunciado:

**Factory Method.** El tipo de reserva depende de quién la solicita: un estudiante crea una reserva regular y un capitán crea una reserva de equipo oficial. La decisión de qué clase instanciar vive en un solo lugar, y cada reserva sale del creador con su política de cancelación ya asignada.

**Abstract Factory.** Cada sede produce una familia de objetos que se usan juntos: su validador de horario y su notificador. Crea una fábrica por sede. Desde el código cliente no debe ser posible combinar el validador de una sede con el notificador de la otra.

**Builder.** La reserva recurrente tiene datos obligatorios (cancha, fecha de inicio, franja y solicitante) y opcionales (número de semanas, equipo prestado y notas). Constrúyela paso a paso, sin un constructor con nueve parámetros posicionales.

**Prototype.** El bloqueo del administrador se define una vez como plantilla y se clona para cada cancha y fecha. Modificar el equipo de un clon no debe modificar la plantilla. En tu README, explica por qué usaste `copy.copy` o `copy.deepcopy`.

**Singleton.** La configuración de reglas de Tecnología existe una sola vez en el sistema, y tanto la prioridad como la cancelación y la suspensión leen sus valores de ahí. En tu README, explica en dos o tres oraciones qué ganaste y qué costo aceptaste al usarlo. Recuerda lo que pasó con la configuración en el laboratorio de la Sesión 5.1.

**Strategy.** La regla de prioridad que extrajiste en el PSet 1 ya es un Strategy: ahora nómbrala así. Agrega la política de cancelación con al menos tres estrategias: estudiante (2 horas), capitán (24 horas) y anulación administrativa (sin penalidad). `Reserva` no debe contener un `if` que pregunte quién la creó para decidir cómo cancelarse.

**Facade.** Reservar, reservar de forma recurrente, cancelar y bloquear coordinan varios subsistemas: disponibilidad, calendario, sede, registro de no-shows y notificación. Crea una Facade que exponga esas cuatro operaciones. Para operar sobre reservas, `simulacion.py` solo habla con la Facade, nunca con un subsistema directamente.

**Concurrencia.** Protege la sección crítica de verificar y registrar, de modo que dos solicitudes simultáneas por la misma cancha y franja produzcan exactamente una reserva confirmada. Elige locking pesimista u optimista y justifica tu elección en el README a partir del escenario de ReservaU: muchas más consultas de disponibilidad que reservas, con picos de escritura al inicio de cada semestre.

### simulacion.py

Actualiza:

`implementacion/simulacion.py`

Como mínimo, debe ejecutar estos escenarios e imprimir cada paso a medida que ocurre:

1. Una reserva en cada sede, cada una validada y notificada según su sede.
2. Una reserva rechazada por estar fuera del horario permitido de su sede.
3. Una reserva recurrente exitosa y otra rechazada por conflicto, indicando qué semana chocó.
4. Tres cancelaciones con resultados distintos: estudiante a tiempo, capitán con menos de 24 horas (no-show) y anulación del administrador.
5. Un solicitante que llega a 3 no-shows en el mes y luego intenta reservar.
6. Un bloqueo clonado en dos canchas, una de ellas con una reserva existente que se anula y se notifica.
7. Dos hilos (`threading`) que intentan reservar la misma cancha y franja al mismo tiempo: solo uno obtiene confirmación.

El orden de los `print()` debe corresponder al flujo principal documentado y a tus diagramas de secuencia y actividad.

### Docker

Actualiza el Dockerfile dentro de:

`psets/pset-02/implementacion/`

Debe ser posible ejecutar:

```
docker build -t reservau-v2 .
```

y luego:

```
docker run reservau-v2
```

El contenedor debe terminar sin errores e imprimir la simulación completa.

### 5. Tabla de patrones

En tu `README.md`, incluye una tabla con una fila por patrón y una para tu decisión de concurrencia:

| Patrón | Requerimiento que lo justifica | Problema que resuelve | Clases y métodos |
|---|---|---|---|
| Strategy | RF-.. | ... | ... |

## Consistencia

Los entregables siguen representando el mismo sistema. La cadena de trazabilidad ahora tiene dos eslabones más:

```
Requerimiento
↓
Caso de uso
↓
Diagrama (robustez, secuencia, actividad o estados)
↓
Patrón
↓
Clase / método
↓
Simulación
```

Antes de entregar, toma la regla de los 3 no-shows y recórrela completa:

- ¿Qué requerimiento la define?
- ¿En qué caso de uso y en qué diagrama aparece?
- ¿Qué entidad lleva la cuenta y qué método aplica la suspensión?
- ¿Qué valor lee de la configuración?
- ¿En qué línea de la salida de `simulacion.py` se observa?

Haz lo mismo con cada patrón: si lo quitaras, ¿qué `if`, qué duplicación o qué acoplamiento volvería a aparecer? Si no puedes responderlo, ese patrón no está resolviendo nada en tu diseño.

## Entrega

Todo debe estar en tu repositorio del curso, dentro de:

`psets/pset-02/`

Los entregables de documentación van en formato PDF, uno por archivo:

1. Requerimientos actualizados
2. Diagrama de modelo de dominio actualizado
3. Diagrama de casos de uso y diagramas de flujo de los casos nuevos o modificados
4. Diagrama de robustez
5. Diagrama de secuencia
6. Diagrama de actividad
7. Máquina de estados

La implementación y el Dockerfile van en `psets/pset-02/implementacion/`. La tabla de patrones y las justificaciones de Prototype, Singleton y concurrencia van en `psets/pset-02/README.md`.

Ejemplo de estructura:

```
psets/
└── pset-02/
  ├── README.md
  ├── <entregables>.pdf
  └── implementacion/
     ├── <archivos>.py
     ├── simulacion.py
     └── Dockerfile
```

Tu PSet 1 queda intacto en `pset-01/`: copia a `pset-02/` lo que necesites y extiéndelo ahí.
