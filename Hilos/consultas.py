import threading
import json
import logging


def ciudades(lista):
    logging.info("Comienzo a recorrer las ciudades")
    for miciudad in lista:
        with condicion:
            ciudad.clear()
            ciudad.append(miciudad)  # Posición 0
            # Si no se encontrase la ciudad, ya dejamos rellenados los datos con (no encontrado)
            ciudad.append("(no encontrado)")  # Posición 1
            ciudad.append("(no encontrado)")  # Posición 2
            logging.info("Espero datos de %s", ciudad[0])
            condicion.wait()
            logging.info("Los datos encontrados son: Nombre: %s Habitantes: %s Alcalde: %s\n", ciudad[0], ciudad[1], ciudad[2])


def info():
    archivo = open("lista_ciudades.json", "r")
    mijson = json.load(archivo)
    archivo.close()
    while True:
        with condicion:
            for miciudad in mijson["ciudades"]:
                if miciudad["nombre"] == ciudad[0]:
                    ciudad[1] = miciudad["habitantes"]
                    ciudad[2] = miciudad["alcalde"]
            condicion.notifyAll()


logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
                    datefmt="%H:%M:%S")
condicion = threading.Condition()
ciudad = []
lista = ("Camelot", "Macondo", "Sevilla", "Reisburgo")
hiloCiudades = threading.Thread(target=ciudades, args=(lista,))
hiloInfo = threading.Thread(target=info, daemon=True)
hiloCiudades.start()
hiloInfo.start()
