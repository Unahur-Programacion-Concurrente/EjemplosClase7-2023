#Solución 1 - Utilizar un número fijo de intentos (evitar loops infinitos)
from time import sleep
from threading import Thread
from threading import Lock

def tarea(numero, lock1, lock2):
    # loop until the task is completed
    for i in range(10):
        # adquiere el primer lock
        with lock1:
            sleep(0.1)
            # chequea si el segundo lock esta disponible
            if lock2.locked():
                print(f'Tarea {numero} no puede adquirir el segundo lock, abandonando...')
            else:
                # acquire lock2
                with lock2:
                    print(f'Tarea {numero} pudo adquirir los dos locks, todo listo!.')
                    break

lock1 = Lock()
lock2 = Lock()

thread1 = Thread(target=tarea, args=(0, lock1, lock2))
thread2 = Thread(target=tarea, args=(1, lock2, lock1))

thread1.start()
thread2.start()

thread1.join()
thread2.join()