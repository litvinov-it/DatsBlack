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

    for myShip in massMyShips:
        for i in data:
            if i == 'ships':
                for ship in data[i]:
                    if ship['id'] == myShip['id']:
                        print(f"ID: {myShip['id']}")
                        print(f"Hp: {myShip['hp']}  MaxHp: {myShip['maxHp']}")
                        print(f"Speed: {myShip['speed']}  CheangeSpeed: {ship['changeSpeed']}")
                        print(f"Direction: {myShip['direction']}  CheangeRotate: {ship['rotate']}\n")
                        


    # print(data)
    response = requests.post(f"{BASE_URL}/shipCommand", data=json.dumps(data), headers=headers).json()


    print(f"\n-----------------------{response['tick']}----------------------------\n")

    print('Наших кораблей: ', len(data['scan']['myShips']))
    print('Вражеских кораблей рядом: ', len(data['scan']['enemyShips']))

    time.sleep(3)

    if response['tick'] == 0:
        print("Game Over")
        break


