# Semana 9, Sesión 1: Bases de datos a escala: replicación y particionamiento (sharding)

> Objetivo de la sesión: elegir una estrategia de sharding y de replicación para una base de datos que ya no cabe ni responde en un solo nodo, justificando la clave de partición elegida.

**Lectura previa de esta sesión:** [Database Sharding (PlanetScale)](https://planetscale.com/blog/database-sharding)

**Referencia de esta sesión:** [Sharding (MongoDB Manual)](https://www.mongodb.com/docs/manual/sharding/)

## Antes de empezar

Entra a esta carpeta:

```
cd laboratorios/semana-09-sesion-01
```

`datos_reservas.py` trae 1000 reservas de ReservaU, siempre las mismas, repartidas entre 4 campus y 300 estudiantes, y la función `hash_estable(texto)`. `base_replicada.py` simula una base con una primaria y una réplica, con replicación asincrónica. Los dos archivos ya están completos: no los modifiques.

## Respuesta sobre la lectura

Según el artículo, ¿qué es un shard, y qué decide la clave de partición? ¿Qué le pasa a un sistema cuando la mayoría de las filas terminan en el mismo shard?

_(tu respuesta)_

## Respuesta sobre el caso de apertura

La tabla de reservas de ReservaU creció de 10 mil a 500 millones de filas, con tres servidores de aplicación contra la misma base. ¿Qué se rompe primero, y por qué ya no alcanza con un servidor de base de datos más grande?

_(tu respuesta)_

## Ejercicio 1: Un shard por campus

Este ejercicio se resuelve en vivo, sobre `sharding_por_campus_ejercicio1.py`. Antes de que se muestre el resultado, responde:

**Respuesta 1:** el Campus Norte tiene 10 de las 17 canchas. ¿Cuántas de las 1000 reservas esperas que caigan en el shard del Campus Norte?

_(tu respuesta)_

**Respuesta 2:** con un shard por campus, ¿cuántos shards hay que consultar para mostrar la disponibilidad de una cancha del Campus Sur? ¿Y para mostrarle a una estudiante todas sus reservas, si reservó en dos campus distintos?

_(tu respuesta)_

## Ejercicio 2: Sharding por hash del estudiante

Ahora te toca a ti. `cluster_por_hash_ejercicio2.py` trae la clase `ClusterPorHash`, con la lista de shards ya creada en `__init__`, y sus métodos sin terminar.

1. Completa `shard_de`, `insertar` y `tamanos`.
2. Completa `reservas_de_estudiante` (consulta dirigida) y `reservas_de_cancha`. Las dos devuelven una tupla con las reservas encontradas y la cantidad de shards que tuviste que revisar.
3. Completa `fraccion_que_cambia_de_shard(claves, shards_antes, shards_despues)`.
4. Corre las pruebas:
   ```
   pytest test_cluster_por_hash_ejercicio2.py
   ```
5. Responde: ¿qué fracción de los estudiantes cambia de shard al pasar de 4 a 5 shards? ¿Qué tendría que hacer ReservaU con sus reservas en ese momento?

_(tu respuesta)_

6. Responde: compara el reparto por campus del Ejercicio 1 con el reparto por hash del estudiante. Propón la clave de partición que usarías para las reservas de ReservaU y justifícala con dos criterios: qué tan parejo reparte, y cuál de sus consultas frecuentes queda dirigida y cuál queda en scatter-gather. La consulta más frecuente de ReservaU es la disponibilidad de una cancha en una fecha.

_(tu respuesta)_

## Ejercicio 3: Primaria o réplica, lectura por lectura

El ejercicio más exigente de los tres. `servicio_replicado_ejercicio3.py` trae la clase `ServicioDeReservasReplicado`, que trabaja sobre una `BaseReplicada`. `reservar(...)` ya está completo y escribe siempre en la primaria. Cada lectura tiene que pasar por `self.base.leer_de_primaria()` o `self.base.leer_de_replica()`: las pruebas cuentan dónde leíste.

1. Completa `cancha_disponible(...)`, `mis_reservas(...)` y `ocupacion_del_campus(...)`. Para cada uno, decide de qué nodo leer. `mis_reservas(...)` tiene que cumplir la garantía de leer lo que uno mismo escribió, usando `self.base.tiene_escrituras_pendientes_de(...)`.
2. Corre las pruebas:
   ```
   pytest test_servicio_replicado_ejercicio3.py
   ```
3. Responde: si `cancha_disponible(...)` leyera de la réplica, ¿qué prueba falla, y qué le pasaría a dos estudiantes que reservan la misma cancha con dos segundos de diferencia?

_(tu respuesta)_

### Checklist final

- [ ] `ClusterPorHash.reservas_de_estudiante` revisa un solo shard.
- [ ] `ClusterPorHash.reservas_de_cancha` revisa todos los shards y no pierde ninguna reserva.
- [ ] `cancha_disponible` nunca decide con un dato que pueda estar desactualizado.
- [ ] `mis_reservas` lee de la réplica salvo cuando el propio estudiante tiene escrituras pendientes de replicar.
- [ ] Los tests de los tres ejercicios pasan.

## Antes de la próxima sesión

**Lectura:** [Top caching strategies (ByteByteGo)](https://blog.bytebytego.com/p/top-caching-strategies)

En ReservaU, la disponibilidad de una cancha se consulta muchas más veces de las que alguien reserva. ¿Por qué ir a la base de datos en cada consulta, si la respuesta casi nunca cambia entre una y otra?

_(tu respuesta)_
