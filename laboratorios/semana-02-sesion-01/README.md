# Semana 2, Sesión 1: Fundamentos de Diseño Orientado a Objetos

> Objetivo de la sesión: aplicar composición sobre herencia al refactorizar una jerarquía de clases rígida, distinguiendo cuándo cada principio de POO resuelve o crea problemas de diseño.

**Lectura previa de esta sesión:** [Why Composition over Inheritance (Medium)](https://medium.com/booleanbhushan/why-composition-over-inheritance-bbc845340dfe)

**Referencia de esta sesión:** [Object-Oriented Programming Concepts (Oracle Java Tutorials)](https://docs.oracle.com/javase/tutorial/java/concepts/index.html)

## Antes de empezar

Entra a esta carpeta y corre el archivo de partida:

```
cd laboratorios/semana-02-sesion-01
python patos_roto.py
```

Mira el resultado con atención, en especial la última línea. Con eso arrancamos la discusión de hoy.

## Respuesta sobre la lectura

Antes de que yo abra la discusión: en una frase, ¿cuál es el problema que el artículo le atribuye a extender una clase por herencia, más allá de "la herencia es mala"?

_(espacio para tu respuesta)_

## Ejercicio 1: refactorizar el vuelo con composición
Voy a resolver este ejercicio en vivo, sobre `patos_roto.py`. Antes de que muestre cada paso, anota tu respuesta.

**Respuesta 1:** si `PatoDeGoma` hereda `volar()` de `Pato` tal como está en `patos_roto.py`, ¿qué imprime `PatoDeGoma().volar()`? Corre el archivo si no estás seguro.

_(tu respuesta)_

**Respuesta 2:** para que un pato de goma no pueda "volar" de verdad, ¿moverías el método `volar()` a otro lugar? ¿A dónde, y por qué ahí?

_(tu respuesta)_

**Lo que construyo en vivo:** extraigo el comportamiento de vuelo a una clase separada (`ComportamientoVolar`, con una versión `VuelaConAlas` y una `NoVuela`), y `Pato` deja de heredar `volar()` para en cambio recibir un objeto de comportamiento en el constructor y delegarle la llamada. Después de esto, anota en tus propias palabras: ¿qué cambió entre "heredar un comportamiento" y "componer un comportamiento"?

_(tu respuesta)_

## Ejercicio 2: agregar un caso nuevo sin romper nada
Seguimos sobre el mismo código. Ahora aplico el mismo patrón al método `graznar()`, y agrego un tercer tipo de pato, `PatoSeñuelo`, que no vuela ni grazna de verdad.

**Respuesta 1:** antes de que lo agregue, ¿tienes que modificar `Pato`, `PatoSalvaje` o `PatoDeGoma` para que `PatoSeñuelo` exista? ¿Por qué sí o por qué no?

_(tu respuesta)_

**Respuesta 2:** ¿qué le pasaría a este mismo ejercicio si `Pato` siguiera usando herencia pura (sin composición) para el vuelo y el graznido, en vez del diseño que armamos en el Ejercicio 1?

_(tu respuesta)_

## Ejercicio 3: vehículos
Ahora te toca a ti aplicar el mismo patrón a un dominio distinto: `vehiculo_ejercicio3.py` tiene una jerarquía de vehículos con 5 TODOs. Los primeros cuatro siguen exactamente el patrón que viste en los patos. El quinto te pide diseñar tu propia clase de comportamiento desde cero.

1. Completa los TODOs 1 a 4 en `vehiculo_ejercicio3.py`.
2. Corre las pruebas:
   ```
   pytest test_vehiculo.py
   ```
3. Cuando los 3 tests pasen, resuelve el TODO 5: agrega `Avion`, que se mueve de una forma que ni `Auto` ni `Bote` usan. No hay test automático para este TODO porque el nombre de tu clase de comportamiento lo eliges tú; en la puesta en común comparamos soluciones.
4. Antes de dar por terminado el ejercicio, revisa: ¿tocaste una sola línea de `Vehiculo`, `Auto` o `Bote` para que `Avion` funcione? Si sí, tu diseño todavía depende de herencia en algún punto donde debería depender de composición.

## Antes de la próxima sesión

Pregunta: si tuvieras que levantar los requerimientos de un sistema nuevo hablando directamente con quien lo va a usar, ¿qué preguntarías primero: cómo se ve la pantalla, o qué problema tiene hoy sin el sistema?
