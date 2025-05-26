import threading


lock = threading.Lock()
readers = 0


def write_data():
    while readers > 0:
        pass
    lock.acquire()
    write_shared_memory()
    lock.release()


def read_data():
    global readers
    if readers == 0:
        lock.acquire()
    readers += 1
    read_shared_memory()
    readers -= 1
    if readers == 0:
        lock.release()
