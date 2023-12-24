import json
import time
import requests
from predict_position import predict_position
from def_shoot import shoot
from move import generateMove

BASE_URL = 'https://datsblack.datsteam.dev/api'
headers = {
    "x-api-Key": "dff47333-0c90-4954-be6f-60fa24043181"
}

while True:
    response = requests.get(f"{BASE_URL}/scan", headers=headers)

    data = response.json()
    massMyShips = data.get('scan', {}).get('myShips', [])

    data = {'ships': []}
    for myShip in massMyShips:
        data['ships'].append( generateMove(myShip) )

    print(data)
    response = requests.post(f"{BASE_URL}/shipCommand", data=json.dumps(data), headers=headers).json()
    print(response)

    time.sleep(3)


