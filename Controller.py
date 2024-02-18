from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def calculate_click(self, event=None):
        pass
