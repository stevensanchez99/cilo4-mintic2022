from Modelos.Resultado import Resultado
class ResultadoController():
    def __init__(self):
        print("*** Creando Controlador para los resultados de las votaciones ***")

    def index(self):
        print("Listado de todos los resultados de las votaciones")
        # estructura de la base
        resultado = {
            "id": "00",
            "numero de votos": "385",
            "id del partido": "1",
        }
        return [resultado]

    # Creacion de los resultados
    def create(self, unResultado):
            print("Estamos creando los resultados de las votaciónes")
            resultado = Resultado(unResultado)
            return resultado.__dict__

    # Borrar un resultado
    def delete(self, id):
            print("Borrando resultados:  ", id)
            return {"Los resultados de ": id + " fueron eliminados con exito"}

    # actualizacion de resultados
    def update(self, id, resultados):
            print("Actualizando los resultados de las votaciónes: ", id)
            result = Resultado(resultados)
            return result.__dict__

    # consulta de resultados
    def show(self, id):
        print("Consultando... Resultados: ", id)
        resultado = {
            "id": id,
            "numero de votos": "385",
            "id del partido": "1",
        }
        return [resultado]