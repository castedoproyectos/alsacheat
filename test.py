from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Firefox(executable_path = '/Users/carlos.castedo/PProyectos/alsacheat/geckodriver')
driver.get("https://www.alsa.es/")
driver.maximize_window()

elem = driver.find_element_by_xpath("//span[@ class='icn-user']")
elem.click()

time.sleep(1)
user = driver.find_element_by_id("busplusDocumentNumber")
user.send_keys("12423439N")

pasw = driver.find_element_by_id("busplusPassword")
pasw.send_keys("carlitos5")

entrar = driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(text(),'Entrar')]")
entrar.click()
time.sleep(5)


boton_origen = driver.find_element_by_xpath("//button[@id='_originStationNameId_']")
boton_origen.click()
time.sleep(1)
#origen = driver.find_element_by_xpath("//button[@id='_originStationNameId_']/span")
#origen.send_keys("Madrid")

sub_origin = driver.find_element_by_xpath("//li/span[contains(text(),'Madrid (Todas las paradas)')]")
sub_origin.click()

destino = driver.find_element_by_xpath("//button[@id='_destinationStationNameId_']")
destino.click()

destino_escribir = driver.find_element_by_xpath("//input[@data-test-id='destinationStationName']")
destino_escribir.send_keys("Valladolid")

time.sleep(1)
sub_destino = driver.find_element_by_xpath("//li/span[contains(text(),'Valladolid (Todas las paradas)')]")
sub_destino.click()

fecha_ida = driver.find_element_by_xpath("//span[text()='Fecha de ida']")
fecha_ida.click()

time.sleep(1)
dia_ida = driver.find_element_by_xpath("//a[@class='ui-state-default' and text()='18']")
dia_ida.click()


fecha_vuelta = driver.find_element_by_xpath("//span[text()='Añadir vuelta']")
fecha_vuelta.click()

time.sleep(1)
dia_vuelta = driver.find_element_by_xpath("//a[@class='ui-state-default' and text()='20']")
dia_vuelta.click()

buscar_mejor_precio = driver.find_element_by_id("journeySearchFormButtonjs")
buscar_mejor_precio.click()

try:
    pop_up = driver.find_element_by_id("ab_overlay")
    pop_up_style = pop_up.get_attribute("style")
    a = 2
except:
    print("No se encuentra el pop up de carga")

time.sleep(10)
hora_salida_origen = '09:15'
horas_salida_origen_web = driver.find_elements_by_xpath("//span[@data-test-id='departureTime']")
pos = 0
for it in range(len(horas_salida_origen_web)):
    if horas_salida_origen_web[it].text == hora_salida_origen:
        pos = it
        break
 
xpath_bloque_precio_origen = "(//div[@class='bg-info price-travel'])["+str(pos+1)+"]/p/span"
bloque_precio_origen = driver.find_element_by_xpath(xpath_bloque_precio_origen)
try:
    bloque_precio_origen.click()
except:
    driver.execute_script("window.scrollTo(0, "+str(bloque_precio_origen.rect['y'])+")")
    bloque_precio_origen.click()

time.sleep(10)
hora_salida_destino = '04:15'
horas_salida_destino_web = driver.find_elements_by_xpath("//span[@data-test-id='departureTime']")
pos = 0
for it in range(len(horas_salida_origen_web)):
    if horas_salida_destino_web[it].text == hora_salida_destino:
        pos = it
        break
ab_overlay
time.sleep(5)
xpath_bloque_precio_destino = "(//div[@class='bg-info price-travel'])["+str(pos+1)+"]"
bloque_precio_destino = driver.find_element_by_xpath(xpath_bloque_precio_destino)
#TODO Mirar donde se queda la posicion
try:
    bloque_precio_destino.click()
except:
    driver.execute_script("window.scrollTo(0, "+str(bloque_precio_destino.rect['y'])+")")
    bloque_precio_destino.click()


continuar = driver.find_element_by_xpath("(//span[text()='Continuar'])[1]")
continuar.click()

cambiar_asientos = driver.find_element_by_id("btn-collapse-bus")
cambiar_asientos.click()

time.sleep(2)
asiento = driver.find_element_by_xpath("//span[@data-ng-bind='seat.seatNumber' and text()='41']")
asiento.click()

pestania_vuelta = driver.find_element_by_class_name("vuelta information-services-vuelta ng-scope")
pestania_vuelta.click()

asiento = driver.find_element_by_xpath("//span[@data-ng-bind='seat.seatNumber' and text()='53']")
asiento.click()


continuar = driver.find_element_by_xpath("(//span[text()='Continuar'])[1]")
continuar.click()

aceptar_condiciones = driver.find_element_by_id("acceptConditions")
aceptar_condiciones.click()

aceptar_privacidad = driver.find_element_by_id("acceptPrivacy")
aceptar_privacidad.click()

pagar = driver.find_element_by_xpath("//span[text()='Pagar']")
pagar.click()

driver.quit()
