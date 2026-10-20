# Semana 1, Sesión 1: SDLC, Terminal y Git

> Objetivo de la sesión: explicar qué es SDLC y su importancia, comparar metodologías Cascada vs. Ágil, usar la terminal para gestión básica, y dominar el flujo básico de Git y GitHub (commits, branches, push y pull requests).

**Lectura previa de esta sesión:** [Waterfall Process (Martin Fowler)](https://martinfowler.com/bliki/WaterfallProcess.html)

**Referencia de esta sesión:** [What is the software development life cycle (SDLC)? (IBM Think)](https://www.ibm.com/think/topics/sdlc)

## Antes de empezar

Verifica que tu ambiente de desarrollo compile correctamente siguiendo el `README.md` de la raíz del repositorio (`python main.py` debe imprimir "Ambiente de Diseño de Sistemas funcionando correctamente."). Una vez confirmado, entra a esta carpeta:

```
cd laboratorios/semana-01-sesion-01
```

## Ejercicio 1: Terminal, redirección y pipes

En esta carpeta encuentras `servidor.log`, un archivo de log con líneas `INFO` y `ERROR` mezcladas.

1. Usa `pwd` y `ls -la` para confirmar dónde estás y qué archivos hay.
2. Filtra únicamente las líneas que contienen `ERROR` y guarda el resultado en un archivo nuevo, usando un pipe y redirección:
   ```
   cat servidor.log | grep "ERROR" > resultado_errores.txt
   ```
3. Agrega, sin sobrescribir, una línea de resumen al final de ese mismo archivo (usa `>>`, no `>`):
   ```
   echo "Total de errores: $(grep -c ERROR servidor.log)" >> resultado_errores.txt
   ```
4. Verifica el contenido con `cat resultado_errores.txt`.

`resultado_errores.txt` no se sube al repositorio (ver `.gitignore` de la raíz, si tu instructor lo agrega ahí); es un ejercicio de práctica, no una entrega.

## Ejercicio 2: Flujo básico de Git, branching y un conflicto real

Vas a reproducir, con tus propias manos, el flujo que se demostró en clase: crear un repositorio de práctica, hacer commits, crear una rama, y forzar un conflicto para aprender a resolverlo (no a evitarlo).

1. Dentro de esta carpeta, crea e inicializa un repositorio de práctica:
   ```
   mkdir practica-git && cd practica-git
   git init
   git config user.name "Tu Nombre"
   git config user.email "tu@email.com"
   ```
2. Crea `bitacora.md` con una primera línea (por ejemplo `# Bitácora de la sesión 1`), y haz tu primer commit:
   ```
   git add bitacora.md
   git commit -m "docs: bitacora inicial"
   ```
3. Crea una rama `feature/nota` y, en esa rama, cambia la primera línea de `bitacora.md` por otra distinta. Haz commit.
4. Vuelve a `main` (o `master`, según tu configuración) y cambia esa misma línea de `bitacora.md` por una tercera versión distinta. Haz commit ahí también.
5. Intenta fusionar `feature/nota` en `main` (`git merge feature/nota`). Git va a marcar un conflicto porque la misma línea cambió en los dos lados.
6. Abre `bitacora.md`, elige (o combina) el contenido correcto entre las marcas `<<<<<<<`, `=======` y `>>>>>>>`, borra esas marcas, y completa la fusión:
   ```
   git add bitacora.md
   git commit -m "merge: resolver conflicto de bitacora"
   ```
7. Corre `git log --oneline` y confirma que ves los commits de ambas ramas más el commit de fusión.

**Antes de seguir:** en tu bitácora personal (no en `bitacora.md`, en tu propio cuaderno), anota qué decidiste hacer al resolver el conflicto y por qué.

## Ejercicio 3: GitHub y tu primer Pull Request

1. Confirma que ya hiciste fork del repositorio del curso a tu propia cuenta de GitHub (ver el `README.md` de la raíz).
2. Desde tu fork clonado (o tu Codespace), crea una rama nueva:
   ```
   git checkout -b feature/sesion-01-<tu-usuario-github>
   ```
3. Dentro de `laboratorios/semana-01-sesion-01/`, crea un archivo `notas-sesion-01.md` con una respuesta corta (2-3 líneas) a esta pregunta: ¿en qué escenario usarías Cascada y en cuál usarías Ágil, con un ejemplo propio distinto a los vistos en clase?
4. Haz commit siguiendo el formato `tipo: descripción` (`feat:`, `fix:`, `docs:`, `refactor:`) visto en clase, y súbelo a tu fork:
   ```
   git add notas-sesion-01.md
   git commit -m "docs: notas sesion 1 sobre cascada vs agil"
   git push -u origin feature/sesion-01-<tu-usuario-github>
   ```
5. En GitHub, abre un Pull Request de tu rama hacia `main` de tu propio fork. Antes de abrirlo, verifica los 4 criterios vistos en clase:
   - **Código:** el archivo existe y no rompe nada.
   - **Descripción:** explica qué cambia y por qué.
   - **Commits:** mensaje descriptivo, siguiendo la convención.
   - **Sin secretos:** nunca subas contraseñas ni API keys (no aplica en este ejercicio, pero es el hábito que se evalúa desde hoy).

## Antes de la próxima sesión

Ven a clase listo para discutir: ¿qué problema tendríamos si programamos un sistema grande sin ninguna forma de organizar el código en unidades relacionadas (la pregunta que abre la Sesión 2, sobre arquitectura de sistemas)?
