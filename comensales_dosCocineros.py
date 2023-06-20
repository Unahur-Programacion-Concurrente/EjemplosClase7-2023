import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

lockCocinero = threading.Lock()

class Cocinero(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.name = f'Cocinero {numero}'

    def run(self):
        global platosDisponibles
        while (True):
            semaforoCocinero.acquire() 
            lockCocinero.acquire()
            try:
                # el hilo cocinero intentara adquirir el lock, pero no podra hacerlo 
                # hasta que un hilo comensal libere el lock del cocinero cuando no haya mas platos disponibles, 
                # por lo que el hilo cocinero al intentar adquirir su lock se va a suspender.
                if lockCocinero.locked():
                    logging.info('Reponiendo los platos...')
                    platosDisponibles = 3
                else:
                    pass    
            finally:
                lockCocinero.release()
                semaforoPlatos.release()


class Comensal(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.name = f'Comensal {numero}'

    def run(self):
        global platosDisponibles
        semaforoPlatos.acquire() 
        try:    
            while platosDisponibles == 0: # cuando no hay platos disponibles.
                semaforoCocinero.release() # se libera al cocinero
                semaforoPlatos.acquire() # se adquiere el "asiento"
            platosDisponibles -= 1 # y cuando el cocinero termina de preparar los platos, el comensal descuenta uno.
            logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
        finally:
            semaforoPlatos.release() # para finalizar el comensal libera el "asiento"    

platosDisponibles = 3 
semaforoPlatos = threading.Semaphore(1)
semaforoCocinero = threading.Semaphore(0) # se inicia en 0 (bloqueado) para que el cocinero no pueda cocinar 
# hasta que un comensal haga release al semaforo del cocinero.

for l in range(2):
    Cocinero(l).start()

for i in range(5):
    Comensal(i).start()