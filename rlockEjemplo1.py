import threading
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

lock = threading.Lock()

def funcA():
    lock.acquire()
    try:
        logging.info(f'funcion A')
        funcB()

    finally:
        lock.release()

def funcB():
    lock.acquire()
    try:
        logging.info(f'funcion B')
    finally:
        lock.release()




t1 = threading.Thread(target=funcA)
t2 = threading.Thread(target=funcB)

t1.start()
t2.start()

