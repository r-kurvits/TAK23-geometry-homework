from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as font


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.__width = 450
        self.__height = 300
        self.default_font = font.Font(family='Verdana', size=12)

        self.title("Koonuse GUI")

        self.center_window(self.__width, self.__height)

        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        (self.radius_entry,
         self.height_entry,
         self.btn_calculate,
         self.text_box
         ) = self.create_frame_widgets()

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_top_frame(self):
        frame = Frame(self, bg='#DBDBDB', height=15)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg='grey')
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_frame_widgets(self):
        radius_label = Label(self.top_frame, text='Koonuse raadius', font=self.default_font)
        radius_label.grid(row=1, column=0, padx=5, pady=5)

        radius_entry = Entry(self.top_frame, font=self.default_font)
        radius_entry.grid(row=1, column=1, padx=5, pady=5)
        radius_entry.focus()

        height_label = Label(self.top_frame, text='Koonuse kõrgus', font=self.default_font)
        height_label.grid(row=2, column=0, padx=5, pady=5)

        height_entry = Entry(self.top_frame, font=self.default_font)
        height_entry.grid(row=2, column=1, padx=5, pady=5)

        btn_calculate = Button(self.top_frame,
                               text='Arvuta',
                               font=self.default_font,
                               command=self.controller.calculate_click
                               )
        btn_calculate.grid(row=1, column=2, rowspan=2, columnspan=24, padx=5, pady=5, sticky='nsew')

        text_box = Text(self.bottom_frame, font=self.default_font, state='disabled')
        scrollbar = Scrollbar(self.bottom_frame, orient='vertical')
        scrollbar.config(command=text_box.yview)
        text_box.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        text_box.pack(expand=True, fill=BOTH, padx=5, pady=5)

        self.bind('<Return>', self.controller.calculate_click)

        return radius_entry, height_entry, btn_calculate, text_box
