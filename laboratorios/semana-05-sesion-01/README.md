# Semana 5, Sesión 1: Patrones de Diseño: Propósito, Categorías, Singleton y Factory Method

> Objetivo de la sesión: clasificar un patrón de diseño según su categoría (creacional, estructural, de comportamiento), y justificar cuándo Singleton o Factory Method resuelven un problema de creación de objetos sin introducir acoplamiento innecesario.

**Lectura previa de esta sesión:** [Singleton: The Anti-pattern! (Medium)](https://medium.com/@razu.dev/singleton-the-anti-pattern-18fb2bd102c2)

**Referencia de esta sesión:** [Singleton y Factory Method (Refactoring.Guru)](https://refactoring.guru/design-patterns/singleton)

## Antes de empezar

Entra a esta carpeta y corre las pruebas del archivo de partida:

```
cd laboratorios/semana-05-sesion-01
pytest test_configuracion_rota.py -v
```

Mira el resultado de cada prueba y el orden en que corrieron. Con eso arrancamos la discusión de hoy.

## Respuesta sobre la lectura

Antes de que se abra la discusión: en una frase, ¿qué problema genera una variable global disfrazada de Singleton específicamente en las pruebas automatizadas?

_(tu respuesta)_

## Ejercicio 1: Singleton disciplinado
Este ejercicio se resuelve en vivo, sobre `configuracion_rota.py`. Antes de que se muestre la solución, responde:

**Respuesta 1:** la primera prueba de `test_configuracion_rota.py` pasa; la segunda falla, aunque no menciona `modo_mantenimiento` en ningún momento. ¿Por qué?

_(tu respuesta)_

**Respuesta 2:** ¿agregar un método `GestorDeConfiguracion.reiniciar()` elimina el Singleton, o lo mantiene y solo agrega un punto de control?

_(tu respuesta)_

**Lo que se construye en vivo:** un método `reiniciar()` que borra `GestorDeConfiguracion._instancia`, llamado como primera línea de cada prueba. Después de esto, anota en tus propias palabras: ¿qué cambió entre "Singleton sin control" y "Singleton disciplinado"?

_(tu respuesta)_

## Ejercicio 2: Factory Method sobre la creación de reservas
Seguimos con `reservas_sin_fabrica.py`, donde dos funciones repiten el mismo `if isinstance(solicitante, EquipoOficial)` para decidir qué tipo de reserva crear.

**Respuesta 1:** antes de ver el refactor, ¿qué pasaría si ReservaU agrega un tercer tipo de reserva con el diseño actual de `reservas_sin_fabrica.py`?

_(tu respuesta)_

**Respuesta 2:** ¿en qué archivo de `reservas_con_fabrica.py` esperas que viva la única decisión sobre qué clase crear?

_(tu respuesta)_

## Ejercicio 3: Factory Method para notificaciones

Ahora te toca aplicar el mismo patrón a un problema distinto: `notificaciones_ejercicio3.py` decide cómo avisar de una reserva, con 5 TODOs. Los primeros cuatro siguen exactamente el patrón que viste en las reservas. El quinto te pide escribir tú la función que elige el creador correcto.

1. Completa los TODOs 1 a 4 en `notificaciones_ejercicio3.py`.
2. Corre las pruebas:
   ```
   pytest test_notificaciones_ejercicio3.py
   ```
3. Cuando los tests de `NotificadorCorreo`, `NotificadorSMS` y los dos creadores pasen, resuelve el TODO 5: `elegir_creador_de_notificador(solicitante)`, que retorna `CreadorDeNotificadorCorreo` para un `Estudiante` y `CreadorDeNotificadorSMS` para un `EquipoOficial`.
4. Antes de dar por terminado el ejercicio, revisa: ¿tocaste una sola línea de `NotificadorCorreo`, `NotificadorSMS`, `CreadorDeNotificadorCorreo` o `CreadorDeNotificadorSMS` para que `elegir_creador_de_notificador` funcione? Si sí, tu diseño todavía depende de un `if` disperso en vez de Factory Method.

### Checklist final

- [ ] `NotificadorCorreo.enviar` y `NotificadorSMS.enviar` retornan el string exacto que pide el comentario TODO.
- [ ] `CreadorDeNotificadorCorreo.crear_notificador` y `CreadorDeNotificadorSMS.crear_notificador` retornan una instancia del notificador correcto.
- [ ] `elegir_creador_de_notificador` retorna el creador correcto según el tipo de `solicitante`, sin un `isinstance` adicional en ninguna otra clase del archivo.
- [ ] Los 6 tests de `test_notificaciones_ejercicio3.py` pasan.

## Antes de la próxima sesión

Imagina un constructor de `ReservaCompleja` con 8 parámetros, la mayoría opcionales (recurrencia, equipo prestado, notas, confirmación manual). Factory Method resuelve qué clase crear. ¿Qué problema distinto aparece cuando lo difícil no es elegir la clase, sino simplemente llamar al constructor sin equivocarse de parámetro?

_(tu respuesta)_
