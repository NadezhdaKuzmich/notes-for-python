import socket

# створення TCP-сокету
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# підключення до сервера використовуючи доменне ім'я та порт
# можна також використовувати IP-адресу
sock.connect(('example.com', 80))
# готуємо дані запиту, записуємо у вигляді масиву, щоб розділяти
# логічні шматки - далі склеюватимемо рядки.
content_items = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    # два порожні рядки - завершення тіла запиту (на склеюванні буде два \n
    '\n'
]
# збираємо запит, використовуючи перенесення рядка як роздільник (\n)
content = '\n'.join(content_items)

print('--- HTTP MESSAGE ---')
print(content)
print('--- END OF MESSAGE ---')
# надсилаємо текстовий запит на відкритий сокет example.com:80
sock.send(content.encode())
# читаємо дані з сокету в розмірі 10024 - тут можна вказувати конкретне
# значення, яке описано в специфікації протоколу. В даному випадку 10024
# вказано просто як приклад - краще використовувати ступінь 2
# (наприклад: 1, 2, 4, 8, 16, 32, 64, 128, 512, 1024, 2048, ...)
result = sock.recv(10024)
# друкуємо дані, отримані з сокету, декодуючи байти в рядок
print(result.decode())
