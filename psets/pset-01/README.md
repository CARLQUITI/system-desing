# PSet 1: Análisis y Diseño de ReservaU

## Contexto

**ReservaU** es una plataforma de reservas de espacios universitarios. La información que levantaste en los role plays de la Sesión 2.2 forma parte de la especificación de este PSet.

El primer stakeholder te explicó cómo funciona el proceso de reservas. Los estudiantes pueden utilizar ReservaU para reservar canchas deportivas disponibles en el campus para actividades individuales o informales. También hay **capitanes de equipos oficiales**. Un capitán puede realizar las mismas acciones que un estudiante, pero existe una regla: los equipos oficiales tienen **prioridad para reservar antes de las 6:00 p. m.**

El segundo stakeholder te explicó el proceso de cancelación y algunas responsabilidades administrativas. Un estudiante puede cancelar su propia reserva. Si la cancelación ocurre con suficiente anticipación, se procesa como una cancelación normal. Sin embargo, existe una regla de negocio: si un estudiante cancela cuando faltan menos de 2 horas para el inicio de la reserva, la acción debe registrarse como **no-show** en lugar de una cancelación regular. La regla de las 2 horas debe aplicarla el sistema, no la decides tú como usuario.

El administrador del complejo deportivo también participa en ReservaU. Es responsable de:

- Gestionar las canchas disponibles.
- Intervenir en conflictos relacionados con las reservas.

Tus entregables deben mostrar la transición completa:

```
Conversación con el stakeholder
↓
Requerimientos
↓
Modelo de dominio
↓
Casos de uso
↓
Código
↓
Simulación
↓
Validación
```

Si agregas una regla, entidad, método o caso de uso que no viste en clase, debes poder explicar qué necesidad de alguno de los dos stakeholders lo justifica.

## Entregables

### 1. Requerimientos

Documenta los requerimientos:

- Funcionales
- No funcionales

Por ejemplo:

RF-01: El sistema debe permitir que un estudiante reserve una cancha disponible.

Un requerimiento como "el sistema debe gestionar correctamente las reservas" no es suficiente, porque "correctamente" admite múltiples interpretaciones. Tus requerimientos funcionales deben describir comportamientos o reglas del sistema, no decisiones de interfaz.

### 2. Modelo de dominio

Construye el diagrama de modelo completo de ReservaU. Define:

- Atributos
- Relaciones
- Responsabilidades
- Reglas de negocio

Las reglas de negocio deben vivir en la entidad que conoce la información necesaria para aplicarlas. Buscamos un **modelo rico**, no un modelo anémico.

```
Requerimiento → Entidad → Responsabilidad
```

### 3. Casos de uso

Crea un diagrama de todos los **casos de uso**.

Crea un **diagrama de flujo** para cada caso de uso, y debe contener:

- Actor principal
- Precondiciones
- Flujo principal
- Flujos alternos

El flujo principal debe describir la interacción lógica entre el actor y el sistema. No describas detalles de interfaz.

Los flujos alternos deben estar anclados a un paso específico del flujo principal, utilizando la notación **número + letra**.

### 4. Implementación con POO

Toma las clases de tu modelo de dominio y escribe una implementación en **Python**.

Esto NO es la aplicación completa. No necesitas:

- Servidor
- Base de datos
- Interfaz gráfica
- API
- Pruebas automatizadas

Se reduce a dos piezas:

1. Las clases de tu modelo.
2. Un script `simulacion.py`.

Tu implementación debe incluir las clases con sus atributos y métodos correspondientes.

Crea una clase separada que represente la **regla de prioridad**. Debes tener al menos dos comportamientos: una regla que aplica prioridad antes de las 6:00 p. m., y una regla que nunca aplica prioridad.

Haz que cada solicitante **tenga** una regla de prioridad en lugar de decidirla mediante un `if` dentro de su propio método. Es el mismo movimiento que hicieron con los patos en clase: sacar el comportamiento que varía a su propia clase y componerlo, en vez de encadenarlo dentro del método que lo usa.

**`simulacion.py`**

Crea un script: `implementacion/simulacion.py`. Este script debe:

- Crear instancias de tus clases.
- Ejecutar todos los flujos.
- Llamar los métodos correspondientes.
- Imprimir cada paso a medida que ocurre.

El orden de los `print()` debe corresponder al flujo principal documentado. Por ejemplo, si tu caso de uso dice:

```
1. El estudiante solicita reservar una cancha.
2. El sistema verifica disponibilidad.
3. El sistema crea la reserva.
4. El sistema confirma la reserva.
```

la simulación debe mostrar la misma secuencia.

**Docker**

Agrega un `Dockerfile` dentro de `psets/pset-01/implementacion/`. El contenedor debe ejecutar `simulacion.py`.

No necesitas:

- Exponer puertos
- Docker Compose
- Volúmenes
- Réplicas

Debe ser posible ejecutar:

```
docker build -t reservau .
```

y luego:

```
docker run reservau
```

El contenedor debe terminar sin errores e imprimir la simulación completa.

## Consistencia

Los seis entregables (requerimientos, modelo de dominio, casos de uso, código, simulación, validación) representan el mismo sistema. Por eso deben ser consistentes entre sí. Un requerimiento debe poder rastrearse hasta el resto del diseño:

```
Requerimiento → Caso de uso → Entidad / método → Simulación
```

Antes de entregar, selecciona al menos un requerimiento importante y comprueba mentalmente:

- ¿Dónde aparece en mis casos de uso?
- ¿Qué clase es responsable de esa regla?
- ¿Qué método la implementa?
- ¿Puedo observarla en `simulacion.py`?

Si una regla aparece únicamente en el documento pero no tiene representación en el diseño, revisa tu solución. Si aparece un comportamiento en el código que nunca fue solicitado por un requerimiento, revisa también tu solución.

## Entrega

Todo debe estar en tu fork del repositorio del curso, dentro de `psets/pset-01/`.

Los entregables de documentación, en formato PDF cada uno:

1. Documento PDF de requerimientos.
2. Diagrama de modelo de dominio.
3. Diagrama de casos de uso.
4. Diagrama de flujo de casos de uso.

La implementación (clases + `simulacion.py` + `Dockerfile`) va en `psets/pset-01/implementacion/`.

Ejemplo de estructura:

```
psets/
└── pset-01/
    ├── README.md
    └── implementacion/
        ├── <archivos>.py
        └── Dockerfile
```

La estructura exacta de los archivos de Python puede variar según tu diseño. Pull Request al repositorio del curso antes de la fecha de entrega.

## Fecha de entrega

Semana 4, Sesión 2.

## Qué reviso

- Que los requerimientos funcionales describan comportamientos o reglas del sistema, no decisiones de interfaz, y que ninguno dependa de una palabra ambigua como "correctamente".
- Que el modelo de dominio sea rico: las reglas de negocio viven en la entidad que las conoce, no en una función externa.
- Que el diagrama de casos de uso cubra todos los casos de uso de ReservaU, que cada flujo principal describa solo interacción lógica actor-sistema, y que los flujos alternos estén anclados con la notación número + letra.
- Que exista una clase separada para la regla de prioridad, con al menos los dos comportamientos pedidos (aplica antes de las 6pm, nunca aplica), y que cada solicitante la tenga compuesta en vez de decidirla con un `if`.
- Que `simulacion.py` ejecute todos los flujos documentados y que el orden de sus `print()` coincida con el flujo principal de cada caso de uso.
- Que `docker build -t reservau .` y `docker run reservau` terminen sin errores e impriman la simulación completa.
- Que al menos un requerimiento importante se pueda rastrear completo: caso de uso → entidad/método → línea de `simulacion.py`.

## Una recomendación

No empieces desde cero. Retoma lo que ya construimos juntos: los dos stakeholders de la Sesión 2.2, los casos de uso de la Sesión 3.1, el modelo de dominio de la Sesión 3.2, y llévalos a la versión completa que pide este PSet. Lo que más se revisa no es si copiaste bien lo de clase, es la trazabilidad: que un requerimiento se pueda seguir hasta un caso de uso, hasta una entidad y un método, hasta una línea de tu simulación.
