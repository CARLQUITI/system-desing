# Semana 9, Sesión 2: Caché y CDN en sistemas a gran escala

> Objetivo de la sesión: seleccionar una estrategia de caché (cache-aside, write-through, entre otras) y explicar qué problema resuelve un CDN para contenido estático distribuido geográficamente.

**Lectura previa de esta sesión:** [Top caching strategies (ByteByteGo)](https://blog.bytebytego.com/p/top-caching-strategies)

**Referencia de esta sesión:** [HTTP caching (MDN Web Docs)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching)

## Antes de empezar

Entra a esta carpeta:

```
cd laboratorios/semana-09-sesion-02
```

`repositorio.py` simula la base de datos de ReservaU: cada operación tarda `latencia` segundos de verdad, y los contadores `consultas` y `escrituras` registran cuántas veces se llegó hasta ahí. `reloj.py` trae un `RelojSimulado` que solo avanza cuando la prueba se lo pide, para probar un tiempo de vida sin esperar de verdad. Los dos archivos ya están completos: no los modifiques.

## Respuesta sobre la lectura

Según el artículo, ¿en qué se diferencia una estrategia de caché de lectura de una de escritura? ¿Cuál de las de escritura confirma más rápido, y qué arriesga a cambio?

_(tu respuesta)_

## Respuesta sobre la pregunta de la sesión pasada

La disponibilidad de una cancha se consulta muchas más veces de las que alguien reserva. ¿Por qué ir a la base de datos cada vez? ¿Qué tendría que pasar para que guardar la respuesta sea un error?

_(tu respuesta)_

## Ejercicio 1: Cache-aside sobre la disponibilidad

Este ejercicio se resuelve en vivo, sobre `cache_aside_ejercicio1.py`. Antes de que se muestre cada resultado, responde:

**Respuesta 1:** cada consulta al repositorio tarda 0.02 segundos. ¿Cuánto esperas que tarden 50 consultas iguales sin caché, y cuántas de esas 50 llegan al repositorio con cache-aside?

_(tu respuesta)_

**Respuesta 2:** con la disponibilidad ya guardada en el caché, alguien registra una reserva a las 18 directamente en el repositorio. ¿Qué horas libres devuelve ahora el servicio con caché?

_(tu respuesta)_

## Ejercicio 2: Invalidación y tiempo de vida

Ahora te toca a ti. `invalidacion_ttl_ejercicio2.py` trae la clase `ServicioConInvalidacionYTTL`, que recibe el repositorio, el reloj y el tiempo de vida en segundos.

1. Completa `disponibilidad(...)`: cache-aside, guardando cada entrada como una tupla `(libres, instante)` y tratando como fallo una entrada con `ttl` segundos o más.
2. Completa `reservar(...)`: verifica en el repositorio, registra, e invalida la entrada de esa cancha y esa fecha con `self.cache.pop((cancha, fecha), None)`.
3. Corre las pruebas:
   ```
   pytest test_invalidacion_ttl_ejercicio2.py
   ```
4. Responde: si ya invalidas en cada reserva, ¿para qué sirve además el tiempo de vida? Piensa en una reserva que se registra sin pasar por este servicio, como la del Ejercicio 1.

_(tu respuesta)_

## Ejercicio 3: Write-through y write-back

El ejercicio más exigente de los tres. `estrategias_escritura_ejercicio3.py` trae dos clases:

- `DisponibilidadWriteThrough`: al reservar, escribe en el repositorio y actualiza la entrada del caché en la misma operación, en vez de borrarla.
- `VisitasWriteBack`: cuenta cuántas veces se abre la página de cada cancha. Cada visita se suma solo en el caché, y `vaciar()` las pasa al repositorio, una escritura por cancha. `caer()` ya está completo: simula que el caché se reinicia antes de vaciar.

1. Completa los métodos marcados con `TODO` en las dos clases.
2. Corre las pruebas:
   ```
   pytest test_estrategias_escritura_ejercicio3.py
   ```
3. Responde: ¿por qué write-back sirve para el contador de visitas y no serviría nunca para las reservas? Usa lo que muestra `test_write_back_pierde_lo_que_no_alcanzo_a_vaciar`.

_(tu respuesta)_

4. Responde: la página de cada cancha muestra también una foto y el mapa del campus, iguales para todos los estudiantes y en todas las ciudades donde ReservaU tenga usuarios. ¿Qué componente se encarga de esos archivos, y por qué no el caché de hoy?

_(tu respuesta)_

### Checklist final

- [ ] `ServicioConInvalidacionYTTL.reservar` verifica la hora en el repositorio, nunca en el caché.
- [ ] `reservar` invalida solo la entrada `(cancha, fecha)` afectada.
- [ ] `DisponibilidadWriteThrough.reservar` deja el caché al día sin volver a consultar el repositorio.
- [ ] `VisitasWriteBack.registrar_visita` no escribe en el repositorio.
- [ ] Los tests de los tres ejercicios pasan.

## Antes de la próxima sesión

**Lectura:** [What are Message Queues and When to Use Them? (AlgoMaster)](https://blog.algomaster.io/p/message-queues)

Al confirmar una reserva, ReservaU envía un correo. Si el servicio de correo se cae justo en ese momento, ¿qué pasa con la reserva y con el correo, tal como está escrito ReservaU hoy?

_(tu respuesta)_
