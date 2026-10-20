# TODO 1: imagen base. Usa una imagen oficial de Python 3.12 en su variante
# "slim" (mas liviana que la imagen completa). Busca en Docker Hub el nombre
# exacto de la imagen "python" con el tag "3.12-slim" si no lo recuerdas.
FROM ???

# Directorio de trabajo dentro del contenedor: todo lo que sigue corre aqui.
WORKDIR /app

# Copiamos primero requirements.txt (y no todo el codigo) para que Docker
# reutilice esta capa si el codigo cambia pero las dependencias no.
COPY requirements.txt .

# TODO 2: instala las dependencias listadas en requirements.txt con pip.
RUN ???

# Ahora si copiamos el resto del codigo de la aplicacion.
COPY . .

# TODO 3: expone el puerto en el que corre la app. Revisa app.py: ¿en que
# puerto llama Flask a app.run()?
EXPOSE ???

# TODO 4: comando que arranca la aplicacion al iniciar el contenedor.
# Usa la forma de lista de CMD: ["ejecutable", "argumento"].
CMD ["python", "???"]
