# Semana 1, Sesión 2: Arquitectura de Sistemas, Monolito y Contenedores

> Objetivo de la sesión: distinguir arquitectura monolítica de microservicios, entender qué resuelve un contenedor (empaquetar código + dependencias + ambiente de ejecución), y contenerizar una aplicación monolítica simple corriendo dos réplicas para observar, de primera mano, la idea de escalamiento horizontal.

**Lectura previa de esta sesión:** [Monolith First Approach Before Moving to Microservices (Medium)](https://medium.com/design-microservices-architecture-with-patterns/monolith-first-approach-before-moving-to-microservices-da969be8bf7c)

**Referencia de esta sesión:** [Docker overview (Docker Docs)](https://docs.docker.com/get-started/docker-overview/)

## Antes de empezar

Verifica que tienes Docker disponible en tu ambiente (`docker --version`). Si estás en el Dev Container del repositorio, Docker-in-Docker ya está configurado y no necesitas instalar nada. Entra a esta carpeta:

```
cd laboratorios/semana-01-sesion-02
```

Este laboratorio usa `app.py`: un monolito de "estacionamientos" hecho con Flask que junta, en un solo servicio, la gestión de espacios y la gestión de reservas. Es intencional: hoy lo vamos a contenerizar tal cual está, sin separarlo. La pregunta de si conviene separarlo es la que vamos a empezar a responder recién en la Semana 6.

No necesitas entender Flask a nivel de sintaxis hoy: trátalo como una caja negra ya resuelta. Lo único que vas a escribir es el cuerpo de una función de Python normal (sin nada de Flask) en el Ejercicio 1. Flask como framework web se enseña formalmente más adelante en el curso (APIs REST, Semana 9).

## Ejercicio 1: Completa la función y corre las pruebas

1. Abre `app.py` y localiza `espacios_disponibles(espacios)`. Actualmente lanza `NotImplementedError`.
2. Implementa la función: debe devolver cuántos elementos de la lista `espacios` tienen `"ocupado": False`. No cambies el nombre ni la firma de la función.
3. Instala las dependencias y corre las pruebas:
   ```
   pip install -r requirements.txt
   pytest test_app.py
   ```
4. Los 3 tests en `test_app.py` deben pasar antes de seguir al Ejercicio 2. Si el contenedor falla más adelante, la causa más probable es que este paso quedó incompleto.

## Ejercicio 2: Completa el Dockerfile y construye la imagen

Abre `Dockerfile`. Tiene 4 TODOs marcados con comentarios; el resto (WORKDIR, el orden de los COPY) ya está resuelto y comentado para que veas por qué `requirements.txt` se copia antes que el resto del código (caché de capas: si el código cambia pero las dependencias no, Docker reutiliza la capa de `pip install` en vez de reinstalarlo todo).

1. **TODO 1:** define la imagen base (`FROM ...`). Usa la imagen oficial `python` en su variante `slim`, versión `3.12`.
2. **TODO 2:** el comando `RUN` que instala las dependencias de `requirements.txt` con `pip`.
3. **TODO 3:** el puerto que expone el contenedor (`EXPOSE ...`). Revisa el final de `app.py`: ¿en qué puerto llama `app.run()`?
4. **TODO 4:** el `CMD` que arranca la aplicación al iniciar el contenedor, en su forma de lista.

Construye la imagen:

```
docker build -t estacionamientos-monolito .
```

Si el build falla, el mensaje de error casi siempre apunta directo al TODO que quedó mal. No borres capas que ya funcionan para "probar cosas": lee el error primero.

## Ejercicio 3: Corre dos réplicas y observa el escalamiento horizontal

Un solo contenedor es solo un contenedor. Escalar horizontalmente significa correr **más de una copia idéntica** del mismo servicio. Vamos a simularlo en tu propia máquina con dos contenedores en puertos distintos.

1. Levanta la primera réplica, mapeando el puerto 5000 del contenedor al 8001 de tu máquina:
   ```
   docker run -d -p 8001:5000 --name replica-1 estacionamientos-monolito
   ```
2. Levanta una segunda réplica, en el puerto 8002:
   ```
   docker run -d -p 8002:5000 --name replica-2 estacionamientos-monolito
   ```
3. Confirma que ambas están corriendo:
   ```
   docker ps
   ```
4. Consulta la raíz (`/`) de cada una:
   ```
   curl http://localhost:8001/
   curl http://localhost:8002/
   ```
5. Compara el campo `"atendido_por"` de las dos respuestas. Debe ser distinto: cada réplica corre en su propio contenedor, con su propio hostname. Esto es, en miniatura, exactamente lo que hace un load balancer al repartir tráfico entre réplicas idénticas (tema de una semana más adelante en el curso).
6. Prueba también `curl http://localhost:8001/espacios` y confirma que tu implementación de `espacios_disponibles` responde correctamente desde dentro del contenedor.
7. Cuando termines, detén y elimina las dos réplicas:
   ```
   docker rm -f replica-1 replica-2
   ```

## Pregunta de reflexión (para la próxima sesión)

`app.py` mezcla dos responsabilidades en un solo servicio: gestión de espacios y gestión de reservas. Hoy las escalaste juntas, aunque solo una de las dos reciba mucho tráfico (por ejemplo, muchas más consultas de espacios disponibles que reservas nuevas). ¿Qué tendrías que cambiar en esta arquitectura si quisieras escalar cada responsabilidad por separado? No hace falta que lo resuelvas ahora: es la pregunta que el curso va a retomar cuando lleguemos a monolito vs. microservicios en profundidad.
