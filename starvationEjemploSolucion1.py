#solución 1 mover el lock
import threading
import time

def tarea(lock, identificador):

        # executa tarea
        for i in range(5):
            with lock:
                # simula procesamiento
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