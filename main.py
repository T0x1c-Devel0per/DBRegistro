from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultados import ControladorResultados




miControladorPartido = ControladorPartido()
miControladorCandidato = ControladorCandidato()
miControladorMesa = ControladorMesa()
miControladorResultados = ControladorResultados()




@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

########################################################################################################################
@app.route("/partido", methods=['GET'])
def getPartido():
    json = miControladorPartido.index()
    return jsonify(json)


@app.route("/partido", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)


@app.route("/partido/<string:id>", methods=['GET'])
def getPartido_id(id):
    json = miControladorPartido.show(id)
    return jsonify(json)


@app.route("/partido/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)


@app.route("/partido/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

########################################################################################################################

@app.route("/candidato", methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)


@app.route("/candidato", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)


@app.route("/candidato/<string:id>", methods=['GET'])
def getCandidato_id(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)


@app.route("/candidato/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)


@app.route("/candidato/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

@app.route("/candidato/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoCandidato(id,id_partido):
    json=miControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)

########################################################################################################################

@app.route("/mesa", methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)


@app.route("/mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)


@app.route("/mesa/<string:id>", methods=['GET'])
def getMesa_id(id):
    json = miControladorMesa.show(id)
    return jsonify(json)


@app.route("/mesa/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)
########################################################################################################################

@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultados.index()
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['GET'])
def getResultados_id(id):
    json=miControladorResultados.show(id)
    return jsonify(json)

@app.route("/resultados/mesa/<string:id_mesa>/partido/<string:id_partido>",methods=['POST'])
def crearResultados(id_mesa,id_partido):
    data = request.get_json()
    json=miControladorResultados.create(data,id_mesa,id_partido)
    return jsonify(json)

@app.route("/resultados/<string:id_resultado>/mesa/<string:id_mesa>/partido/<string:id_partido>",methods=['PUT'])
def modificarResultados(id_resultados,id_mesa,id_partido):
    data = request.get_json()
    json=miControladorResultados.update(id_resultados,data,id_mesa,id_partido)
    return jsonify(json)

@app.route("/resultados/<string:id_resultados>",methods=['DELETE'])
def eliminarResultados(id_resultados):
    json=miControladorResultados.delete(id_resultados)
    return jsonify(json)

########################################################################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
