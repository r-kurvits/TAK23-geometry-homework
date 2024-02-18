import math


class Cone:
    def __init__(self, radius, height):
        self.radius = radius if radius > 0 else 0
        self.height = height if height > 0 else 0

    def get_radius(self):
        return self.radius

    def get_height(self):
        return self.height

    def get_bottom_area(self):
        return round(math.pi * (self.radius ** 2), 2)

    def get_hypotenuse(self):
        return round(math.sqrt(self.radius**2 + self.height**2), 2)

    def get_volume(self):
        volume = round((1/3) * math.pi * self.radius**2 * self.height, 2)
        return volume
