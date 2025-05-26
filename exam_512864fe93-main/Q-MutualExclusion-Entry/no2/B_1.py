import threading


lock = threading.Lock()


def write_data():
    lock.acquire()
    write_shared_memory()
    lock.release()


def read_data():
    while lock.locked():
        pass
    read_shared_memory()
