import requests

# pip install requests
# запускаємо різні види запитів, але вже з використанням
# бібліотеки requests
response1 = requests.get('http://example.com')
response2 = requests.put('https://jsonplaceholder.typicode.com/posts/')
response3 = requests.post('https://jsonplaceholder.typicode.com/posts/')
response4 = requests.delete('https://jsonplaceholder.typicode.com/posts/')
