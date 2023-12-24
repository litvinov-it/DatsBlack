import math


class Zona_Radius:

    def __init__(self, zone, count=1):
        self.zone = zone
        self.count = count

    def change_zone(self, new_zone):
        self.count = self.zone["radius"] - new_zone["radius"]
        self.zone = new_zone

    def change_count(self, new_count):
        """
        Поменять значение сужения зоны. То есть, у нас есть зона и она сужается на определённое значение(count)
        """
        self.count = new_count

    def reduce_radius(self):
        self.zone['radius'] = self.zone['radius'] - self.count


    def are_inside(self, x,y):
        len_x = self.zone['x'] - x
        len_y = self.zone['y'] - y
        gipo = math.sqrt(len_x**2 + len_y**2)
        if gipo <= self.zone['radius']:
            return True
        else:
            return False

    def well_be_inside(self, x, y, time=1):
        len_x = self.zone['x'] - x
        len_y = self.zone['y'] - y
        gipo = math.sqrt(len_x**2 + len_y**2)
        if gipo <= (self.zone['radius'] - (self.count * time)):
            return True
        else:
            return False
        




if __name__ == '__main__':
    zona = Zona_Radius({'x': 1, 'y': 1, 'radius': 4}, 1)
    print(zona.are_inside(1, 5))