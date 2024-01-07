import os
import threading


def exec_watcher():
    # запускаємо функцію print_files кожні 5 секунд в окремому потоці
    timer = threading.Timer(5.0, print_files)
    timer.start()


def print_files():
    for i in os.listdir('.'):
        print(i)


exec_watcher()
