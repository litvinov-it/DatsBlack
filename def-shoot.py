import math

def shoot(data):
    '''
    Отдаёт словарь по каждому кароблю, с информацией о том, нужно ли стрелять и куда стрелять
    Например:
    {
        "id": 1811,    ----  айди текущего корабля
        "fire": True,    ---- бывает что false. Это значит, что стрелять не нужно и тогда coordinates будет равен [0,0]
        "coordinates": [1402, 1454]    ---- координаты, куда стрелять [x, y]
    }
    '''

    shapes_shoot = {}

    for i in range(len(data['scan']['myShips'])):
        print(f"id - {data['scan']['myShips'][i]['id']}   x - {data['scan']['myShips'][i]['x']}   y - {data['scan']['myShips'][i]['y']}   radius - {data['scan']['myShips'][i]['scanRadius']}")
        fire = False
        coordinates = [0,0]
        for j in range(len(data['scan']['enemyShips'])):
            len_x = abs(data['scan']['myShips'][i]['x'] - data["scan"]["enemyShips"][j]["x"])
            len_y = abs(data['scan']['myShips'][i]['y'] - data["scan"]["enemyShips"][j]["y"])
            gipo = math.sqrt(len_x**2 + len_y**2)
            print(len_x,len_y)
            print(gipo)
            if gipo <= data['scan']['myShips'][i]['scanRadius']:
                fire = True
                coordinates = [data["scan"]["enemyShips"][j]["x"], data["scan"]["enemyShips"][j]["y"]]
                print('FIRE!!!!')
            print(f'        enemy: x - {data["scan"]["enemyShips"][j]["x"]}    y - {data["scan"]["enemyShips"][j]["y"]}')
        shapes_shoot[data['scan']['myShips'][i]['id']] = {'fire': fire, 'coordinates': coordinates}
    
    print('-----------------------')
    print('-----------------------')
    print('-----------------------')
    print('-----------------------')
    return shapes_shoot








if __name__ == '__main__':

    data = {
    "success": True,
    "scan": {
        "myShips": [
            {
                "id": 1811,
                "x": 1362,
                "y": 1413,
                "size": 3,
                "hp": 3,
                "maxHp": 3,
                "direction": "north",
                "speed": 0,
                "maxSpeed": 10,
                "minSpeed": -1,
                "maxChangeSpeed": 5,
                "cannonCooldown": 3,
                "cannonCooldownLeft": 0,
                "cannonRadius": 20,
                "scanRadius": 60,
                "cannonShootSuccessCount": 0
            },
            {
                "id": 1812,
                "x": 1365,
                "y": 1414,
                "size": 2,
                "hp": 2,
                "maxHp": 2,
                "direction": "north",
                "speed": 0,
                "maxSpeed": 10,
                "minSpeed": -1,
                "maxChangeSpeed": 5,
                "cannonCooldown": 3,
                "cannonCooldownLeft": 0,
                "cannonRadius": 20,
                "scanRadius": 60,
                "cannonShootSuccessCount": 0
            },
            {
                "id": 1813,
                "x": 1368,
                "y": 1414,
                "size": 3,
                "hp": 3,
                "maxHp": 3,
                "direction": "north",
                "speed": 0,
                "maxSpeed": 10,
                "minSpeed": -1,
                "maxChangeSpeed": 5,
                "cannonCooldown": 3,
                "cannonCooldownLeft": 0,
                "cannonRadius": 20,
                "scanRadius": 60,
                "cannonShootSuccessCount": 0
            },
            {
                "id": 1814,
                "x": 1371,
                "y": 1414,
                "size": 2,
                "hp": 2,
                "maxHp": 2,
                "direction": "north",
                "speed": 0,
                "maxSpeed": 10,
                "minSpeed": -1,
                "maxChangeSpeed": 5,
                "cannonCooldown": 3,
                "cannonCooldownLeft": 0,
                "cannonRadius": 20,
                "scanRadius": 60,
                "cannonShootSuccessCount": 0
            },
            {
                "id": 1815,
                "x": 1374,
                "y": 1413,
                "size": 4,
                "hp": 4,
                "maxHp": 4,
                "direction": "north",
                "speed": 0,
                "maxSpeed": 10,
                "minSpeed": -1,
                "maxChangeSpeed": 5,
                "cannonCooldown": 3,
                "cannonCooldownLeft": 0,
                "cannonRadius": 20,
                "scanRadius": 60,
                "cannonShootSuccessCount": 0
            },
            {
                "id": 1816,
                "x": 1377,
                "y": 1415,
                "size": 2,
                "hp": 2,
                "maxHp": 2,
                "direction": "north",
                "speed": 0,
                "maxSpeed": 10,
                "minSpeed": -1,
                "maxChangeSpeed": 5,
                "cannonCooldown": 3,
                "cannonCooldownLeft": 0,
                "cannonRadius": 20,
                "scanRadius": 60,
                "cannonShootSuccessCount": 0
            },
            {
                "id": 1817,
                "x": 1380,
                "y": 1415,
                "size": 2,
                "hp": 2,
                "maxHp": 2,
                "direction": "north",
                "speed": 0,
                "maxSpeed": 10,
                "minSpeed": -1,
                "maxChangeSpeed": 5,
                "cannonCooldown": 3,
                "cannonCooldownLeft": 0,
                "cannonRadius": 20,
                "scanRadius": 60,
                "cannonShootSuccessCount": 0
            },
            {
                "id": 1818,
                "x": 1383,
                "y": 1414,
                "size": 3,
                "hp": 3,
                "maxHp": 3,
                "direction": "north",
                "speed": 0,
                "maxSpeed": 10,
                "minSpeed": -1,
                "maxChangeSpeed": 5,
                "cannonCooldown": 3,
                "cannonCooldownLeft": 0,
                "cannonRadius": 20,
                "scanRadius": 60,
                "cannonShootSuccessCount": 0
            },
            {
                "id": 1819,
                "x": 1386,
                "y": 1414,
                "size": 4,
                "hp": 4,
                "maxHp": 4,
                "direction": "north",
                "speed": 0,
                "maxSpeed": 10,
                "minSpeed": -1,
                "maxChangeSpeed": 5,
                "cannonCooldown": 3,
                "cannonCooldownLeft": 0,
                "cannonRadius": 20,
                "scanRadius": 60,
                "cannonShootSuccessCount": 0
            },
            {
                "id": 1820,
                "x": 1389,
                "y": 1414,
                "size": 5,
                "hp": 5,
                "maxHp": 5,
                "direction": "north",
                "speed": 0,
                "maxSpeed": 10,
                "minSpeed": -1,
                "maxChangeSpeed": 5,
                "cannonCooldown": 3,
                "cannonCooldownLeft": 0,
                "cannonRadius": 20,
                "scanRadius": 60,
                "cannonShootSuccessCount": 0
            }
        ],
        "enemyShips": [
            {
                "x": 1375,
                "y": 1454,
                "hp": 2,
                "maxHp": 2,
                "size": 2,
                "direction": "north",
                "speed": 0
            },
            {
                "x": 1378,
                "y": 1453,
                "hp": 2,
                "maxHp": 2,
                "size": 2,
                "direction": "north",
                "speed": 0
            },
            {
                "x": 1381,
                "y": 1453,
                "hp": 4,
                "maxHp": 4,
                "size": 4,
                "direction": "north",
                "speed": 0
            },
            {
                "x": 1384,
                "y": 1453,
                "hp": 3,
                "maxHp": 3,
                "size": 3,
                "direction": "north",
                "speed": 0
            },
            {
                "x": 1387,
                "y": 1454,
                "hp": 3,
                "maxHp": 3,
                "size": 3,
                "direction": "north",
                "speed": 0
            },
            {
                "x": 1390,
                "y": 1454,
                "hp": 2,
                "maxHp": 2,
                "size": 2,
                "direction": "north",
                "speed": 0
            },
            {
                "x": 1393,
                "y": 1454,
                "hp": 4,
                "maxHp": 4,
                "size": 4,
                "direction": "north",
                "speed": 0
            },
            {
                "x": 1396,
                "y": 1454,
                "hp": 3,
                "maxHp": 3,
                "size": 3,
                "direction": "north",
                "speed": 0
            },
            {
                "x": 1399,
                "y": 1454,
                "hp": 5,
                "maxHp": 5,
                "size": 5,
                "direction": "north",
                "speed": 0
            },
            {
                "x": 1402,
                "y": 1454,
                "hp": 2,
                "maxHp": 2,
                "size": 2,
                "direction": "north",
                "speed": 0
            }
        ],
        "zone": None,
        "tick": 994
    }
}


    print(shoot(data))