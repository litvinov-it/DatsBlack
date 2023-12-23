import copy

def predict_position(data):

    data = copy.deepcopy(data)

    for ship in data['scan']['enemyShips']:
        speed = ship['speed']
        
        if ship['direction'] == 'north':
            ship['y'] -= speed
        elif ship['direction'] == 'south':
            ship['y'] += speed
        elif ship['direction'] == 'east':
            ship['x'] -= speed
        elif ship['direction'] == 'west':
            ship['x'] += speed

    return data

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

data_predict = predict_position(data)

for i in range(len(data["scan"]['enemyShips'])):
    print('Корабль врага ', i+1)
    print('X: ', data['scan']['enemyShips'][0]['x'], 'Y: ', data['scan']['enemyShips'][0]['y'])
    print('X: ', data_predict['scan']['enemyShips'][0]['x'], 'Y: ', data_predict['scan']['enemyShips'][0]['y'])