import requests

BASE_URL = 'https://datsblack.datsteam.dev/api'
headers = {
    "x-api-Key": "dff47333-0c90-4954-be6f-60fa24043181"
}

response = requests.get(f"{BASE_URL}/scan", headers=headers)

data = response.json()

# print('Наших кораблей: ', len(data['scan']['myShips']))
# print('Вражеских кораблей рядом: ', len(data['scan']['enemyShips']))