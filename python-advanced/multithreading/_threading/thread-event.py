import threading
import time


def producer():
    time.sleep(5)
    print('Product found!')
    # встановлюємо події
    product.set()
    # очищуємо подію
    product.clear()


def consumer():
    print('product wait')
    # очікуємо події рівно стільки, поки не викличеться product.set в будь-якому
    # з потоків
    product.wait()
    print('Product exists!')


# створюємо подію, яку будемо використовувати в потоку - чекати і встановлювати
# створимо блокування потоку до появи події product
product = threading.Event()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task1.start()
task2.start()

task1.join()
task2.join()
