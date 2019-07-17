from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class Handler(object):

    def __init__(self):

        self.driver = webdriver.Firefox(executable_path = '/Users/carlos.castedo/PProyectos/alsacheat/geckodriver')
        self.driver.get("https://www.alsa.es/")
        self.driver.maximize_window()

    def login(self, user, passw):
        elem = self.driver.find_element_by_xpath("//span[@ class='icn-user']")
        elem.click()

        time.sleep(1)
        user_input = self.driver.find_element_by_id("busplusDocumentNumber")
        user_input.send_keys(user)

        pasw_input = self.driver.find_element_by_id("busplusPassword")
        pasw_input.send_keys(passw)

        entrar = self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(text(),'Entrar')]")
        entrar.click()
        time.sleep(5)

    def set_viaje(self, origen, destino, dia_ida, dia_vuelta, num_pasajeros):

        boton_origen = self.driver.find_element_by_xpath("//button[@id='_originStationNameId_']")
        boton_origen.click()
        time.sleep(1)

        # TODO: Hay que escribir en el origen

        sub_origin = self.driver.find_element_by_xpath("//li/span[contains(text(),'Madrid (Todas las paradas)')]")
        sub_origin.click()

        destino = self.driver.find_element_by_xpath("//button[@id='_destinationStationNameId_']")
        destino.click()

        destino_escribir = self.driver.find_element_by_xpath("//input[@data-test-id='destinationStationName']")
        destino_escribir.send_keys("Valladolid")

        time.sleep(1)
        sub_destino = self.driver.find_element_by_xpath("//li/span[contains(text(),'Valladolid (Todas las paradas)')]")
        sub_destino.click()

        fecha_ida = self.driver.find_element_by_xpath("//span[text()='Fecha de ida']")
        fecha_ida.click()

        time.sleep(1)
        dia_ida = self.driver.find_element_by_xpath("//a[@class='ui-state-default' and text()='18']")
        dia_ida.click()


        fecha_vuelta = self.driver.find_element_by_xpath("//span[text()='Añadir vuelta']")
        fecha_vuelta.click()

        time.sleep(1)
        dia_vuelta = self.driver.find_element_by_xpath("//a[@class='ui-state-default' and text()='20']")
        dia_vuelta.click()

        # TODO: Parametrizar el numero de pasajeros
        personas = self.driver.find_element_by_xpath("//a[@title='Modificar pasajeros']")
        personas.click()

        time.sleep(1)
        add_persona = self.driver.find_element_by_xpath("//a[@data-test-id='addPassenger']")
        add_persona.click()
        time.sleep(1)
        add_persona.click()
        aceptar_personas = self.driver.find_element_by_xpath("//a[@data-test-id='closePassengersLink']")
        aceptar_personas.click()

        time.sleep(2)
        buscar_mejor_precio = self.driver.find_element_by_xpath("//div[@id='btSearchDiv']")
        buscar_mejor_precio.click()
        time.sleep(15)

    def set_horas(self, ida, ida_hora, vuelta, vuelta_hora):

        horas_salida = self.driver.find_elements_by_xpath("//div[@class='departure-hora']/span[@data-ng-bind='journey.departureTime']")
        destino_salida = self.driver.find_elements_by_xpath("//div[@class='departure-salida']/span[@data-ng-bind='journey.originName']")

        pos_origen = 0
        for idx, val in enumerate(horas_salida):
            if val.text == ida_hora:
                if destino_salida[idx].text.find(ida) >= 0:
                    pos_origen = idx + 1
        
        xpath_precio_origen = "((//li[contains(@id,'outwardJourneyItinerary')])["+str(pos_origen)+"]//div[@class='lista-precios']/div)[1]"
        bloque_precio_origen = self.driver.find_element_by_xpath(xpath_precio_origen)
        try:
            bloque_precio_origen.click()
        except:
            self.driver.execute_script("window.scrollTo(0, "+str(bloque_precio_origen.rect['y'])+")")
            bloque_precio_origen.click()
        
        time.sleep(1)
        try:
            aceptar_cnd = self.driver.find_element_by_xpath("//button[contains(text(),'Aceptar condiciones')]")
            aceptar_cnd.click()
        except:
            pass
        
        time.sleep(1)
        horas_salida = self.driver.find_elements_by_xpath("//div[@class='departure-hora']/span[@data-ng-bind='journey.departureTime']")
        destino_salida = self.driver.find_elements_by_xpath("//div[@class='departure-salida']/span[@data-ng-bind='journey.originName']")

        pos_destino = 0
        for idx, val in enumerate(horas_salida):
            if val.text == vuelta_hora:
                if destino_salida[idx].text.find(vuelta) >= 0:
                    pos_destino = idx + 1
        

        xpath_precio_destino = "((//li[contains(@id,'returnJourneyItinerary')])["+str(pos_destino)+"]//div[@class='lista-precios']/div)[1]"
        bloque_precio_destino = self.driver.find_element_by_xpath(xpath_precio_destino)
        try:
            bloque_precio_destino.click()
        except:
            self.driver.execute_script("window.scrollTo(0, "+str(bloque_precio_destino.rect['y'])+")")
            bloque_precio_destino.click()
        
        time.sleep(1)

        try:
            aceptar_cnd = self.driver.find_element_by_xpath("//button[contains(text(),'Aceptar condiciones')]")
            aceptar_cnd.click()
        except:
            pass
        time.sleep(1)
        continuar = self.driver.find_element_by_xpath("(//span[text()='Continuar'])[1]")
        continuar.click()

        time.sleep(5)

    def cambio_asientos(self, asientos_ida, asientos_vuelta):

        cambiar_asientos = self.driver.find_element_by_id("btn-collapse-bus")
        cambiar_asientos.click()

        time.sleep(2)
        self.driver.execute_script("window.scrollTo(200, 400)")

        for num in asientos_ida:
            time.sleep(1)
            xpath_asiento_ida = "//div[@class='available' and ./span[@data-ng-bind='seat.seatNumber' and text()='"+str(num)+"']]"
            try:
                asiento_ida = self.driver.find_element_by_xpath(xpath_asiento_ida)
                asiento_ida.click()
            except:
                print("Asiento ida "+str(num)+" ocupado")


        time.sleep(2)
        pestania_vuelta = self.driver.find_element_by_xpath("//div[@class='vuelta information-services-vuelta ng-scope']")
        pestania_vuelta.click()

        time.sleep(2)
        self.driver.execute_script("window.scrollTo(200, 400)")
        
        for num in asientos_vuelta:
            time.sleep(1)
            xpath_asiento_vuelta = "(//div[@class='available' and ./span[@data-ng-bind='seat.seatNumber' and text()='"+str(num)+"']])[2]"
            try:
                asiento_vuelta = self.driver.find_element_by_xpath(xpath_asiento_vuelta)
                asiento_vuelta.click()
            except:
                print("Asiento vuelta "+str(num)+" ocupado")

        continuar = self.driver.find_element_by_xpath("(//span[text()='Continuar'])[1]")
        continuar.click()

        time.sleep(5)

    def exit(self):
        self.driver.quit()