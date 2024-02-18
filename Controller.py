from tkinter import messagebox
from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def calculate_click(self, event=None):
        radius = self.view.radius_entry.get().strip()
        height = self.view.height_entry.get().strip()
        if not self.model.is_number(radius):
            self.invalid_value("Raadius")
        if not self.model.is_number(height):
            self.invalid_value("Kõrgus")

        result = self.model.get_user_input(radius, height)
        self.view.radius_entry.delete(0, 'end')
        self.view.height_entry.delete(0, 'end')
        if result:
            self.view.text_box.config(state='normal')
            self.view.text_box.insert('insert', result + '\n')
            self.view.text_box.see('end')
            self.view.text_box.config(state='disabled')

    def invalid_value(self, entry):
        invalid_value = messagebox.showerror("Viga", f"{entry} on vigane. {entry} peab olema positiivne arv")
        return invalid_value
