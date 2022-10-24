from Modelos.Candidato import Candidato
class  CandidatoController():
    def __init__(self):
        print("*** Creando Controlador para el Candidato ***")
    #Listado
    def index(self):
        print("Listado de todos los candidatos")
        # estructura de la base
        candidato = {
            "_id": "1",
            "cedula": "1073720321",
            "nombre": "Steven ",
            "numero de resolucion": "0001",
            "apellido": "Sanchez"
        }
        return [candidato]

    # Creacion de candidato
    def create(self, unCandidato):
            print("Estamos creando el candidato")
            candidato = Candidato(unCandidato)
            return candidato.__dict__

    # Borrar un candidato
    def delete(self, id):
            print("Borrando un candidato:  ", id)
            return {"candidato eliminado": id}

    # actualizacion
    def update(self, id, candidato):
            print("Actualizando candidato: ", id)
            cto = Candidato(candidato)
            return cto.__dict__

    # consulta
    def show(self, id):
            print("Consultando... Candidato: ", id)
            candidato = {
                "_id": id,
                "cedula": "1073720321",
                "nombre": "Steven ",
                "numero de resolucion": "0001",
                "apellido": "Sanchez"
            }
            return candidato