import math
import random
from map import map as map

map = map()
ship = {
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
            }
class Move():

    def __init__(self, map, ship):
        self.map = map
        self.speed = ship['speed']
        self.direction = ship['direction']
        self.maxSpeed = ship['maxSpeed']
        self.minSpeed = ship['minSpeed']
        self.maxChangeSpeed = ship['maxChangeSpeed']
        self.data = {
                        "id": ship['id'],
                        "changeSpeed": 0,
                        "rotate": 0
                    }

    def up(self, speed = 1):
        # Если скорость после изменения - больше максимальной мы делаем ее просто максимальной
        if self.data['changeSpeed'] + speed + self.speed >= self.maxSpeed:
            self.data['changeSpeed'] = self.maxSpeed - self.speed
        else:
            self.data['changeSpeed'] = speed

    def down(self, speed = 1):
        if self.data['changeSpeed'] - speed + self.speed <= self.minSpeed:
            self.data['changeSpeed'] = int(-1 * ( math.fabs(self.minSpeed) + self.speed ))
        else:
            self.data['changeSpeed'] = -1 * speed

    def left(self):
        self.data['rotate'] = 90

    def right(self):
        self.data['rotate'] = -90

    def renderDirection(self, rotate):
        if self.direction == 'north':
            if rotate == 90:
                self.direction = 'east'
            elif rotate == -90:
                self.direction = 'west'

        elif self.direction == 'east':
            if rotate == 90:
                self.direction = 'south'
            elif rotate == -90:
                self.direction = 'north'

        elif self.direction == 'south':
            if rotate == 90:
                self.direction = 'west'
            elif rotate == -90:
                self.direction = 'east'
        
        elif self.direction == 'west':
            if rotate == 90:
                self.direction = 'north'
            elif rotate == -90:
                self.direction = 'south'

    @staticmethod
    def generatePlusMinus(num):
        return random.randint(num-1, num+1)
    
randSpeed = Move.generatePlusMinus

def generateMove(ship):
    MoveShip = Move(map, ship)
    randDirection = random.randint(1, 2)
    randGo = random.randint(1, 2)

    if randDirection == 1:
        MoveShip.left()
    elif randDirection == 2:
        MoveShip.right()

    if randGo == 1:
        MoveShip.up(randSpeed(0))
    elif randGo == 2:
        MoveShip.down(randSpeed(0))

    return MoveShip.data