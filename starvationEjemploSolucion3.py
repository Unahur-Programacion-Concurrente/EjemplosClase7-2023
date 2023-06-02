#solución 3 agregar una llamada bloqueante antes de adquirir la primitiva de concurrencia (lock)
import threading
import time

def tarea(lock, identificador):

        # executa tarea
        for i in range(5):
           # time.sleep(0.001)
            time.sleep(0.000001)
            with lock:
                print(f'Hilo {identificador} ejecutando')
                time.sleep(1)


lock = threading.Lock()
# crea hilos
hilos = [threading.Thread(target=tarea, args=(lock,i)) for i in range(2)]
# arranca hilos
for hilo in hilos:
    hilo.start()
# Espera a que terminen los hilos
for hilo in hilos:
    hilo.join()