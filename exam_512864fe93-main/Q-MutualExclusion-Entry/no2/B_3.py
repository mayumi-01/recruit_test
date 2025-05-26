import threading


lock = threading.Lock()
readers_lock = threading.Lock()
readers = 0


def write_data():
    lock.acquire()
    write_shared_memory()
    lock.release()


def read_data():
    global readers
    readers_lock.acquire()
    if readers == 0:
        lock.acquire()
    readers += 1
    readers_lock.release()

    read_shared_memory()

    readers_lock.acquire()
    readers -= 1
    if readers == 0:
        lock.release()
    readers_lock.release()
