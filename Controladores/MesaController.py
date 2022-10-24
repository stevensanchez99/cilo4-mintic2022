from Modelos.Mesa import Mesa
class MesaController():
    def __init__(self):
        print("*** Creando Controlador para la mesa de votación ***")

    def index(self):
        print("Listado de todas las mesas de votación")
        # estructura de la base
        mesa = {
            "numero mesa": "00",
            "cantidad inscritos": "385",
        }
        return [mesa]

    # Creacion de la mesa
    def create(self, unaMesa):
            print("Estamos creando la mesa de votación")
            mesa = Mesa(unaMesa)
            return mesa.__dict__

    # Borrar un candidato
    def delete(self, id):
            print("Borrando la mesa:  ", id)
            return {"La mesa ": id + " fue elimanda con exito"}

    # actualizacion
    def update(self, id, mesa):
            print("Actualizando datos de la mesa de votación: ", id)
            cto = Mesa(mesa)
            return cto.__dict__

    # consulta
    def show(self, id):
            print("Consultando... Mesa: ", id)
            mesa = {
                "numero mesa": id,
                "cantidad inscritos": "385",
            }
            return [mesa]