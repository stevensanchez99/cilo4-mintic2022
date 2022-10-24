#Importacion de librerias
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app) #instancia del cors, pruebas en el servidor

#importar controladores
#CANDIDATOS
from Controladores.CandidatoController import CandidatoController
controladorCandidato = CandidatoController()
#MESAS
from Controladores.MesaController import MesaController
controladorMesa = MesaController()
#PARTIDOS
from Controladores.PartidoController import PartidoController
controladorPartido = PartidoController()
#RESULTADOS
from  Controladores.ResultadoController import ResultadoController
controladorResultado = ResultadoController()


#Micro servicio de creacion candidato
@app.route("/candidatos",methods=['POST'])
#definir funcion
def crearCandidato():
    datos = request.get_json()
    json=controladorCandidato.create(datos)
    return jsonify(json)

#Microservicio de listado de  Candidatos
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json = controladorCandidato.index()
    return jsonify(json)

#Microservicio de borrar Candidato
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def borrarCandidato(id):
    json=controladorCandidato.delete(id)
    return jsonify(json)

#Microservicio de actualizar Candidato
@app.route("/candidatos/<string:id>",methods=['PUT'])
def actualizarCandidato(id):
    datos = request.get_json()
    json=controladorCandidato.update(id,datos)
    return jsonify(json)

#Microservicio de  consultar candidato
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=controladorCandidato.show(id)
    return jsonify(json)

#*************************************************************************************************************
#Micro servicio de creacion de la mesa de votación
@app.route("/mesa",methods=['POST'])
#definir funcion
def crearMesa():
    datos = request.get_json()
    json=controladorMesa.create(datos)
    return jsonify(json)

#Microservicio de listado de las mesas de votación
@app.route("/mesa",methods=['GET'])
def getMesas():
    json = controladorMesa.index()
    return jsonify(json)

#Microservicio de borrar Candidato
@app.route("/mesa/<string:id>",methods=['DELETE'])
def borrarMesa(id):
    json=controladorMesa.delete(id)
    return jsonify(json)

#Microservicio de actualizar mesa de votación
@app.route("/mesa/<string:id>",methods=['PUT'])
def actualizarMesa(id):
    datos = request.get_json()
    json=controladorMesa.update(id,datos)
    return jsonify(json)

#Microservicio de  consultar mesa de votación
@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    json=controladorMesa.show(id)
    return jsonify(json)

#*************************************************************************************************************

#*************************************************************************************************************
#Micro servicio de creacion de los partidos politicos
@app.route("/partidos",methods=['POST'])
#definir funcion
def crearPartido():
    datos = request.get_json()
    json=controladorPartido.create(datos)
    return jsonify(json)

#Microservicio de listado de los partidos politicos
@app.route("/partidos",methods=['GET'])
def getPartidos():
    json = controladorPartido.index()
    return jsonify(json)

#Microservicio de borrar partidos politicos
@app.route("/partidos/<string:id>",methods=['DELETE'])
def borrarPartido(id):
    json=controladorPartido.delete(id)
    return jsonify(json)

#Microservicio de actualizar partido politico
@app.route("/partidos/<string:id>",methods=['PUT'])
def actualizarPartido(id):
    datos = request.get_json()
    json=controladorPartido.update(id,datos)
    return jsonify(json)

#Microservicio de  consultar partidos politicos
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=controladorPartido.show(id)
    return jsonify(json)

#*************************************************************************************************************

#*************************************************************************************************************
#Micro servicio de creacion de los resultados de las votaciones
@app.route("/resultados",methods=['POST'])
#definir funcion
def crearResultados():
    datos = request.get_json()
    json=controladorResultado.create(datos)
    return jsonify(json)

#Microservicio de listado de los resultados
@app.route("/resultados",methods=['GET'])
def getResultados():
    json = controladorResultado.index()
    return jsonify(json)

#Microservicio de borrar resultados de las votaciones
@app.route("/resultados/<string:id>",methods=['DELETE'])
def borrarResultado(id):
    json=controladorResultado.delete(id)
    return jsonify(json)

#Microservicio de actualizar resultados de las votaciones
@app.route("/resultados/<string:id>",methods=['PUT'])
def actualizarResultado(id):
    datos = request.get_json()
    json=controladorResultado.update(id,datos)
    return jsonify(json)

#Microservicio de  consultar resultados de las votaciones
@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=controladorResultado.show(id)
    return jsonify(json)

#**********************************************************************************
def loadFileConfig(): #Metodo que lee un archivo
    with open('config.json') as f:
        data = json.load(f)
    return data

#micrtoservicio de prueba el cual retorna el json
@app.route("/",methods=['GET']) #ruta de la cual responde el server y el get genera una consulta
def test():
    json = {}
    json["message"]="Servidor en ejecución....Team Developer JR - 2022"
    return jsonify(json)

if __name__=='__main__': #se ejecuta al iniciar el main
    dataConfig = loadFileConfig() #carga el archivo
    print("Servidor ejecutandose : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"]) #publicar aplicación en el local host, por le 999 que es el que tenemos configurado en json

