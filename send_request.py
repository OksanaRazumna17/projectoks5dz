import requests

# URL для создания категории
url = 'http://localhost:5000/categories'

# Данные для создания категории
data = {
    "name": "Science",
    "description": "All about science"
}

# Отправляем POST-запрос
response = requests.post(url, json=data)

# Выводим статус ответа и данные
print(f'Status Code: {response.status_code}')
print(f'Response: {response.json()}')
