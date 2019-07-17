import json
import pprint

class Viaje(object):

    def __init__(self):
        self._row_data = dict()

        self._usuario = str()
        self._password = str()

        self._datos_ida = dict()
        self._datos_vuelta = dict()

        self._load_values()

    def print_data(self):
        pp = pprint.PrettyPrinter()
        pp.pprint(self._row_data)
    
    def _load_values(self, name_inp = None):
        name = "datos_viaje.json"
        
        # Se define nombre del fichero de carga
        if name_inp is not None:
            name = name_inp
        
        data = None
        with open(name, "r") as read_file:
            data = json.load(read_file)

        self._usuario = data['usuario']
        self._password = data['password']
        self._datos_ida = data['datos ida']
        self._datos_vuelta = data['datos vuelta']

        self._row_data = data
