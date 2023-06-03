from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config


app = Flask(__name__)

conexion = MySQL(app)


@app.route("/cliente", methods=["POST"])
def index():
    try:
        # print(request.json)
        sql = "INSERT INTO clientes (code, name) VALUES ('{0}', '{1}')".format(
            request.json["code"], request.json["name"]
        )
        cursor = conexion.connection.cursor()
        cursor.execute(sql)
        conexion.connection.commit()  # Confirma la acción de inserción.
        return jsonify({"mensaje": "Cliente registrado con exito.", "exito": True})
    except Exception as ex:
        return jsonify({"mensaje": "Error", "exito": False})


if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.run()
