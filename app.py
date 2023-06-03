from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import sys

sys.path.append('src')
from config import config
from validations import *

app = Flask(__name__)

conexion = MySQL(app)


@app.route("/cliente", methods=["POST"])
def index():
    if (validate_code(request.json['code'])):
        try:
            sql = "INSERT INTO clientes (code, name) VALUES ('{0}', '{1}')".format(
                request.json["code"], request.json["name"]
            )
            cursor = conexion.connection.cursor()
            cursor.execute(sql)
            conexion.connection.commit()
            return jsonify({"mensaje": "Cliente registrado con exito.", "exito": True})
        except Exception as ex:
            return jsonify({"mensaje": "Error", "exito": False})
    else:
        return jsonify({'mensaje': "Parámetros incorrectos...", 'exito': False})


def page_not_found(error):
    return "<h1>La pagina que intentas buscar no existe... </h1>"


if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.register_error_handler(404, page_not_found)
    app.run()
