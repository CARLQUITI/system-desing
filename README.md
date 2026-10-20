# Diseno de Sistemas

Repositorio base del curso.

Aqui vive el ambiente de desarrollo estandarizado, los laboratorios y los PSets. Es la fuente de verdad: todo tu trabajo del semestre va aqui, no en otro lado.

## Antes de empezar

No clones ni hagas push a este repositorio directamente. Cada estudiante trabaja en su propio fork:

1. Arriba a la derecha, clic en **"Fork"** y crealo en tu propia cuenta de GitHub.
2. Todo tu trabajo del semestre (laboratorios, PSets) va en tu fork, no aqui.

## Como abrir tu ambiente de desarrollo

En tu copia del repositorio: clic en el boton verde **"Code" -> pestana "Codespaces" -> "Create codespace on main"**. Espera uno o dos minutos mientras se construye el contenedor la primera vez. Se abre VS Code en el navegador, ya con Python, pytest y Docker instalados.

Ambiente local: instala [Docker Desktop](https://www.docker.com/products/docker-desktop/) y la extension **Dev Containers** de VS Code, clona tu copia del repositorio y usa "Reopen in Container".

## Verifica tu ambiente

Dentro del Codespace, abre una terminal y corre:

```
python --version    # debe decir Python 3.12.x
docker --version
pytest --version
python main.py
```

Si ves el mensaje "Ambiente de Diseno de Sistemas funcionando correctamente.", tu ambiente esta listo.

## Estructura del repositorio

```
.devcontainer/          Configuracion del contenedor (no editar)
main.py                 Programa de verificacion del ambiente
requirements.txt        Dependencias de Python del curso
laboratorios/           Laboratorio de cada clase, uno por carpeta
  semana-01-sesion-01/
  semana-01-sesion-02/
  ...
psets/                  Tus entregas de PSet, una carpeta por PSet
  pset-01/
  pset-02/
  ...
```

Cada carpeta de `laboratorios/` y `psets/` tiene su propio `README.md` con las instrucciones de esa entrega.

## Como actualizar tu fork cada semana

Cuando se agregue una semana nueva, sincroniza tu fork:

1. En la pagina de tu fork en GitHub: boton **"Sync fork" -> "Update branch"**.
2. En tu Codespace o tu clon local, haz `git pull` para traer esos cambios.

Por terminal, en vez del boton:
```
git fetch upstream
git merge upstream/main
```
(la primera vez, agrega el remoto: `git remote add upstream <URL de este repositorio>`)

## Como trabajar aqui

- Ejecuta y prueba siempre desde la terminal (no solo el boton "Run" del editor), dentro del Codespace o del contenedor local.
- Corre `pytest` dentro de la carpeta del laboratorio o del PSet antes de dar por terminado un ejercicio con pruebas.
- Haz commit de tu avance seguido, con mensajes que digan que hiciste, no `"cambios"` o `"fix"`.
