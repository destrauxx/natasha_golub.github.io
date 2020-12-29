import requests

url = 'https://paurbx.github.io/main.html'

response = requests.get(url)

with open('./python_is_cool.html', 'wb') as f:
    f.write(response.content)