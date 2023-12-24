from predict_position import predict_position
from def_shoot import shoot
from map import map

import time
import requests
import json



BASE_URL = 'https://datsblack.datsteam.dev/api'
headers = {
    "x-api-Key": "dff47333-0c90-4954-be6f-60fa24043181"
}





# navigation = map()
        




while True:
    print('---------------------------------')
    response = requests.get(f"{BASE_URL}/scan", headers=headers)
    print(requests)

    near_ships = response.json()
    print(near_ships['success'])
    data_predict = predict_position(near_ships)

    mass_shoots = shoot(data_predict)

    # print(mass_shoots)

    body = {
        "ships": []
    }

    for key in mass_shoots:
        if mass_shoots[key]['fire']:
            body['ships'].append({
                "id": key,
                "cannonShoot": {
                    "x": mass_shoots[key]['coordinates'][0],
                    "y": mass_shoots[key]['coordinates'][1]
                }
            })

    # print(body)


    if len(body['ships']) == 0:
        time.sleep(3)
        continue


    body = json.dumps(body)

    print('FFFFFFFFFFFFFIIIIIIIIIIIIIIIIIRRRRRRRRRRRRRRREEEEEEEEEEEEE')
    response = requests.post(f"{BASE_URL}/scan", headers=headers, data=body).json()

    print(response)
    time.sleep(3)




