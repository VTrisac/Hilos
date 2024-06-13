import threading
import time
import random
import logging


class participante(threading.Thread):
    def __init__(self, valor):
        self.nombre = valor
        super().__init__()

    def run(self):
        logging.info("Participante %s comienza!!", self.nombre)
        paro = random.randint(1, 15)
        time.sleep(paro)
        logging.info("Participante %s llega a la meta!! Tiempo: %d segundos", self.nombre, paro)
        self.tiempo = paro
        barrera.wait()


def carrera():
    logging.info("Preparando la carrera... hay %d participantes" % (barrera.parties-1))
    barrera.wait()
    podium = []
    podium.append((part1.tiempo, part1.nombre))
    podium.append((part2.tiempo, part2.nombre))
    podium.append((part3.tiempo, part3.nombre))
    podium.sort()
    logging.info("Fin de la carrera!! Ganador: Participante %s en %s segundos" % (podium[0][1], podium[0][0]))


logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
                    datefmt="%H:%M:%S")
barrera = threading.Barrier(4)
part1 = participante("Borja")
part2 = participante("Ingrid")
part3 = participante("Samuel")
micarrera = threading.Thread(target=carrera)
micarrera.start()
part1.start()
part2.start()
part3.start()
