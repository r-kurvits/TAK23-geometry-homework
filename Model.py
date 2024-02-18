from Cone import Cone


class Model:
    def __init__(self):
        pass

    @staticmethod
    def is_number(user_input):
        try:
            num = int(user_input)
            if num > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def get_user_input(self, radius, height):
        if self.is_number(radius) and self.is_number(height):
            radius = int(radius)
            height = int(height)
            cone = Cone(radius, height)
            radius = cone.get_radius()
            bottom_area = cone.get_bottom_area()
            hypotenuse = cone.get_hypotenuse()
            volume = cone.get_volume()
            return (f''
                    f'Raadius: {radius} \n'
                    f'Kõrgus: {height} \n'
                    f'Hüpotenuus {hypotenuse}\n'
                    f'Põhja pindala {bottom_area} \n'
                    f'Ruumala {volume}'
                    )
        else:
            return False
