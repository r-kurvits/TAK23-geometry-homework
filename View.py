from tkinter import *
from tkinter import messagebox, font


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.__width = 550
        self.__height = 300
        self.default_font = font.Font(family='Verdana', size=12)

        self.title("Ringi GUI")

        self.center_window(self.__width, self.__height)

        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        self.btn_calculate = self.create_frame_widgets()

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_top_frame(self):
        frame = Frame(self, bg='#DBDBDB')
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg='grey')
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_frame_widgets(self):
        lbl_info = Label(self.top_frame, text='Sisesta number', font=self.default_font)
        lbl_info.grid(row=1, column=0, padx=5, pady=5)

        btn_calculate = Button(self.top_frame,
                               text='Arvuta',
                               font=self.default_font,
                               command=self.controller.calculate_click
                               )
        btn_calculate.grid(row=1, column=2, padx=5, pady=5, sticky='ew')

        text_box = Text(self.bottom_frame, font=self.default_font, state='disabled')
        text_box.pack(expand=True, fill=BOTH, padx=5, pady=5)

        num_entry = Entry(self.top_frame, font=self.default_font)
        num_entry.grid(row=1, column=1, padx=5, pady=5)
        num_entry.focus()

        return num_entry, btn_calculate, text_box
