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


while True:
    print('---------------------------------')
    response = requests.get(f"{BASE_URL}/scan", headers=headers)

    data = response.json()
    massMyShips = data.get('scan', {}).get('myShips', [])

    data_predict = predict_position(data)
    mass_shoots = shoot(data_predict)



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

    print('Наших кораблей: ', len(data['scan']['myShips']))
    print('Вражеских кораблей рядом: ', len(data['scan']['enemyShips']))

    time.sleep(3)

    if response['tick'] == 0:
        print("Game Over")
        break





# {
#     "ships": [
#         {
#             "id": 207,
#             "changeSpeed": 0,
#             "rotate": 90
#             // "cannonShoot": {
#             //     "x":1522,
#             //     "y":252
#             // }
#         }
#     ]
# }




# while True:


#     for key in mass_shoots:
#         if mass_shoots[key]['fire']:
#             body['ships'].append({
#                 "id": key,
#                 "cannonShoot": {
#                     "x": mass_shoots[key]['coordinates'][0],
#                     "y": mass_shoots[key]['coordinates'][1]
#                 }
#             })

#     # print(body)


#     if len(body['ships']) == 0:
#         time.sleep(3)
#         continue


#     body = json.dumps(body)

#     print('FFFFFFFFFFFFFIIIIIIIIIIIIIIIIIRRRRRRRRRRRRRRREEEEEEEEEEEEE')
#     response = requests.post(f"{BASE_URL}/scan", headers=headers, data=body).json()

#     print(response)
#     time.sleep(3)


















# while True:

    





#     print('---------------------------------')
#     response = requests.get(f"{BASE_URL}/scan", headers=headers)
#     print(requests)

#     near_ships = response.json()
#     print(near_ships['success'])
#     data_predict = predict_position(near_ships)

#     mass_shoots = shoot(data_predict)

#     # print(mass_shoots)

#     body = {
#         "ships": []
#     }

#     for key in mass_shoots:
#         if mass_shoots[key]['fire']:
#             body['ships'].append({
#                 "id": key,
#                 "cannonShoot": {
#                     "x": mass_shoots[key]['coordinates'][0],
#                     "y": mass_shoots[key]['coordinates'][1]
#                 }
#             })

#     # print(body)


#     if len(body['ships']) == 0:
#         time.sleep(3)
#         continue


#     body = json.dumps(body)

#     print('FFFFFFFFFFFFFIIIIIIIIIIIIIIIIIRRRRRRRRRRRRRRREEEEEEEEEEEEE')
#     response = requests.post(f"{BASE_URL}/scan", headers=headers, data=body).json()

#     print(response)
#     time.sleep(3)




