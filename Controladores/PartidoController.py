from Modelos.Partido import Partido
class  PartidoController():
    def __init__(self):
        print("*** Creando Controlador para el Partido de las votaciones ***")
    #Listado de los partidos
    def index(self):
        print("Listado de todos los partidos")
        # estructura de la base
        partido = {
            "id": "1",
            "nombre": "Partido MinTic 2022",
            "lema": "Programación para la vida "
        }
        return [partido]

    # Creacion de los partidos
    def create(self, unPartido):
            print("Estamos creando el partido")
            partido = Partido(unPartido)
            return partido.__dict__

    # Borrar un partido
    def delete(self, id):
            print("Borrando el partido:  ", id)
            return {"El partido ": id + " fue elimando con exito"}

    # actualizacion
    def update(self, id, partido):
            print("Actualizando partido: ", id)
            pto = Partido(partido)
            return pto.__dict__

    # consulta
    def show(self, id):
            print("Consultando... Partido: ", id)
            partido = {
                "id": id,
                "nombre": "Partido MinTic 2022",
                "lema": "Programación para la vida "
            }
            return [partido]