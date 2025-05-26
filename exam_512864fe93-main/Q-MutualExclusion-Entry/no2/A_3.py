import threading


write_lock = threading.Lock()
read_lock = threading.Lock()


def write_data():
    while read_lock.locked():
        pass
    write_lock.acquire()
    write_shared_memory()
    write_lock.release()


def read_data():
    while write_lock.locked():
        pass
    read_lock.acquire()
    read_shared_memory()
    read_lock.release()
