# DEAD LOCK
import threading


def producer():
    print('Set locking')
    with lock:
        # Потік, що взяв блокування може взяти його нескінченну кількість разів.
        # але інший потік чекатиме
        with lock:
            print("It's great")
    print('Locking release!')


# приклад аналогічний thread-lock.py, але вирішує проблему DEAD LOCK в рамках
# одного потоку.
lock = threading.RLock()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()
