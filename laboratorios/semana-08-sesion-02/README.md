# Semana 8, Sesión 2: Escalabilidad: de un servidor a millones de usuarios, balanceadores de carga

> Objetivo de la sesión: explicar cuándo escalar verticalmente deja de ser viable, y qué rol cumple un balanceador de carga al escalar horizontalmente.

**Lectura previa de esta sesión:** [System Design: Scale From Zero To Millions of Users (Part I) (Medium)](https://medium.com/@connect2kaushambi/system-design-scale-from-zero-to-millions-of-users-part-i-9f544407d44e)

**Referencia de esta sesión:** [What Is Load Balancing? (AWS)](https://aws.amazon.com/what-is/load-balancing/)

## Antes de empezar

Entra a esta carpeta:

```
cd laboratorios/semana-08-sesion-02
```

`servidor.py` es el arnés de simulación de hoy, ya completo: no lo modifiques. Cada `Servidor` atiende como máximo `capacidad` solicitudes al mismo tiempo; cada solicitud ocupa una conexión durante `duracion` segundos simulados, y `avanzar_un_segundo()` libera las que terminaron. `caer()` simula que el servidor deja de responder, y `health_check()` dice si está sano.

## Respuesta sobre la lectura

El artículo arranca con un solo servidor que hace todo y lo va separando a medida que crecen los usuarios. Según el artículo, ¿cuáles son los dos problemas de seguir agrandando ese único servidor en vez de agregar otros?

_(tu respuesta)_

## Respuesta sobre la pregunta de apertura

Primer día de inscripciones: miles de estudiantes abren ReservaU en la misma hora. ¿Por qué no simplemente comprar un servidor más grande, y seguir comprando uno más grande cada semestre?

_(tu respuesta)_

## Ejercicio 1: El pico contra un solo servidor

Este ejercicio se resuelve en vivo, sobre `pico_ejercicio1.py`. Antes de que se muestre cada resultado, responde:

**Respuesta 1:** 250 solicitudes llegan en el mismo segundo a un servidor de capacidad 100. ¿Cuántas atiende y cuántas rechaza? ¿Y si el servidor tiene capacidad 300?

_(tu respuesta)_

**Respuesta 2:** el servidor de capacidad 300 se cae a mitad de las inscripciones. ¿Cuántas de las 250 solicitudes se atienden?

_(tu respuesta)_

## Ejercicio 2: Balanceador round robin con health check

Ahora te toca a ti. `balanceador_ejercicio2.py` trae la clase `BalanceadorRoundRobin` con la lista de servidores y el índice `siguiente` ya creados en `__init__`, y un método `enviar(...)` sin terminar.

1. Completa `enviar(duracion)`: reparte en turnos, salta los servidores que no pasan el health check o que están llenos, y devuelve el nombre del servidor que aceptó la solicitud, o `None` si ninguno pudo.
2. Corre las pruebas:
   ```
   pytest test_balanceador_ejercicio2.py
   ```
3. Antes de dar por terminado el ejercicio, responde: si quitas la llamada a `health_check()` de tu solución, ¿qué prueba falla, y qué le pasaría en ReservaU a un estudiante cuya solicitud cae en ese turno?

_(tu respuesta)_

## Ejercicio 3: Balanceador de menos conexiones

El ejercicio más exigente de los tres. `menos_conexiones_ejercicio3.py` trae la clase `BalanceadorMenosConexiones`, con el mismo `enviar(duracion)` por completar.

1. Completa `enviar(duracion)`: elige, entre los servidores sanos que pueden atender, el que tiene menos conexiones activas; en empate, el primero de la lista.
2. Corre las pruebas:
   ```
   pytest test_menos_conexiones_ejercicio3.py
   ```
   Dos de estas pruebas corren el mismo tráfico mixto (una solicitud de 10 segundos seguida de una de 1 segundo, cuatro veces) con tu balanceador del Ejercicio 2 y con el de este ejercicio, usando `simular_trafico(...)` de `servidor.py`.
3. Responde, con lo que muestran esas dos pruebas: ¿cuántas conexiones activas le quedan a cada servidor al final con cada algoritmo, y por qué round robin las reparte así?

_(tu respuesta)_

4. Responde: ahora el balanceador es el único punto de entrada a los servidores de ReservaU. ¿Qué pasa si se cae, y qué propondrías para que esa caída no detenga el sistema?

_(tu respuesta)_

### Checklist final

- [ ] `BalanceadorRoundRobin.enviar` consulta `health_check()` antes de enviar a cada servidor.
- [ ] `BalanceadorRoundRobin.enviar` nunca pasa dos veces por el mismo servidor en un mismo envío, y devuelve `None` si ninguno puede atender.
- [ ] `BalanceadorMenosConexiones.enviar` compara `conexiones_activas()` solo entre servidores sanos que pueden atender.
- [ ] Los tests de `test_pico_ejercicio1.py`, `test_balanceador_ejercicio2.py` y `test_menos_conexiones_ejercicio3.py` pasan.

## Antes de la próxima sesión

**Lectura:** [Database Sharding (PlanetScale)](https://planetscale.com/blog/database-sharding)

Hoy pusiste tres servidores detrás de un balanceador, pero los tres siguen leyendo y escribiendo en la misma base de datos. Cuando ReservaU tenga 500 millones de reservas, ¿qué se rompe primero?

_(tu respuesta)_
