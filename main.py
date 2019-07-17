from viaje import Viaje
from handler import Handler

v = Viaje()
hd = Handler()

hd.login(v._usuario, v._password)
hd.set_viaje(v._datos_ida['origen'], 
             v._datos_ida['destino'],
             v._datos_ida['dia'],
             v._datos_vuelta['dia'],
             len(v._datos_ida['plazas']))

hd.set_horas(v._datos_ida['origen'], 
             v._datos_ida['hora_salida'],
             v._datos_vuelta['origen'], 
             v._datos_vuelta['hora_salida'])
             
hd.cambio_asientos(v._datos_ida['plazas'], v._datos_vuelta['plazas'])
hd.exit()

