"""Sistema de estacionamientos, version monolito.

Un solo servicio Flask que junta la gestion de espacios y la gestion de
reservas: son dos responsabilidades distintas, pero hoy viven en el mismo
proceso, el mismo codigo y se despliegan siempre juntas. Vas a contenerizar
esta app tal cual esta, sin separarla en servicios.
"""

import socket

from flask import Flask, jsonify, request

app = Flask(__name__)

ESPACIOS = [
    {"id": 1, "ocupado": False},
    {"id": 2, "ocupado": True},
    {"id": 3, "ocupado": False},
    {"id": 4, "ocupado": False},
    {"id": 5, "ocupado": True},
]

RESERVAS = []


def espacios_disponibles(espacios):
    """Cuenta cuantos espacios de la lista NO estan ocupados.

    TODO: completa esta funcion. No cambies la firma ni el nombre:
    el archivo test_app.py depende de que se llame exactamente asi.
    """
    # TODO: reemplaza la linea siguiente por tu implementacion
    raise NotImplementedError


@app.route("/")
def salud():
    """Confirma que el servicio esta vivo y quien lo esta atendiendo.

    'atendido_por' cambia segun el contenedor que responda: uselo en el
    Ejercicio 2 para confirmar que ambas replicas funcionan.
    """
    return jsonify(
        {
            "servicio": "estacionamientos-monolito",
            "atendido_por": socket.gethostname(),
        }
    )


@app.route("/espacios")
def listar_espacios():
    return jsonify(
        {
            "espacios": ESPACIOS,
            "disponibles": espacios_disponibles(ESPACIOS),
        }
    )


@app.route("/reservas", methods=["POST"])
def crear_reserva():
    datos = request.get_json(force=True)
    RESERVAS.append(datos)
    return jsonify({"mensaje": "reserva registrada", "total_reservas": len(RESERVAS)}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
