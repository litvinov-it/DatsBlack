import json
import time
import requests

from predict_position import predict_position
from def_shoot import shoot
from move import generateMove
from map import map

BASE_URL = 'https://datsblack.datsteam.dev/api'
headers = {
    "x-api-Key": "dff47333-0c90-4954-be6f-60fa24043181"
}

def start():
    tick = 0
    while True:
        response = requests.get(f"{BASE_URL}/scan", headers=headers)

        data = response.json()
        data1 = response.json()

        if(data['success'] == False):
            print('success = false')
            break

        if tick == data1['scan']['tick']:
            continue
        else:
            tick = data1['scan']['tick']

        massMyShips = data.get('scan', {}).get('myShips', [])

        data_predict = predict_position(data)
        mass_shoots = shoot(data_predict)


        data = {'ships': []}
        for myShip in massMyShips:
            data['ships'].append( generateMove(myShip) )

        near_ships = {'ships': []}
        for myShip in massMyShips:

            ship = generateMove(myShip)
            
            if mass_shoots[ship['id']]['fire']:
                ship['cannonShoot'] = {
                    "x": mass_shoots[ship['id']]['coordinates'][0],
                    "y": mass_shoots[ship['id']]['coordinates'][1]
                } 

            near_ships['ships'].append(ship)


        for myShip in massMyShips:
            for i in data:
                if i == 'ships':
                    for ship in data[i]:
                        if ship['id'] == myShip['id']:
                            print(f"ID: {myShip['id']}")
                            print(f"Hp: {myShip['hp']}  MaxHp: {myShip['maxHp']}")
                            print(f"Speed: {myShip['speed']}  CheangeSpeed: {ship['changeSpeed']}")
                            print(f"Direction: {myShip['direction']}  CheangeRotate: {ship['rotate']}\n")
                            


        response = requests.post(f"{BASE_URL}/shipCommand", data=json.dumps(data), headers=headers).json()

        print(f"\n-----------------------{response['tick']}----------------------------\n")

        print('Наших кораблей: ', len(data1['scan']['myShips']))
        print('Вражеских кораблей рядом: ', len(data1['scan']['enemyShips']))

        if response['tick'] == 0:
            print("Game Over")
            break

while True:
    response = requests.post(f'{BASE_URL}/royalBattle/registration', headers=headers).json()
    if response['errors']:
        if response['errors'][0]['message'] == 'Вы уже участвуете в битве':
            print('Битва началась')
            start()
        else:
            print(response['errors'][0]['message'])
    if response['success']:
        print('Битва началась')
        start()

    time.sleep(2)