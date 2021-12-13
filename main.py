from Flyweight import *
import tkinter as tk

from tkinter.messagebox import showinfo
from tkinter import ttk


class InputFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        # field options
        options = {'padx': 5, 'pady': 5}

        # # Identity Finder label
        # self.identity_finder_label = ttk.Label(self, width=15, text='Identity Finder')
        # self.identity_finder_label.grid(column=0, row=0, columnspan=2, **options)

        # Name field label
        self.name_field_label = ttk.Label(self, width=15, text='Enter name :')
        self.name_field_label.grid(column=0, row=1, **options)

        # Surname field label
        self.surname_field_label = ttk.Label(self, width=15, text='Enter surname :')
        self.surname_field_label.grid(column=1, row=1, **options)

        # name input field
        self.name_field = tk.StringVar()
        self.name_field = ttk.Entry(self, width=25, textvariable=self.name_field)
        self.name_field.grid(column=0, row=2, **options)
        self.name_field.focus()

        # surname input field
        self.surname_field = tk.StringVar()
        self.surname_field = ttk.Entry(self, width=25, textvariable=self.surname_field)
        self.surname_field.grid(column=1, row=2, **options)

        self.find_button = ttk.Button(self, text='Find', command=self.action)
        self.find_button.grid(column=0, row=3, columnspan=2, **options)

        # # result label
        # self.result_label = ttk.Label(self)
        # self.result_label.grid(row=4, columnspan=2, **options)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def action(self):
        name = self.name_field.get()
        surname = self.surname_field.get()

        added_name, added_surname, name_id, surname_id, coordinates = person_database.add_to_the_database(name, surname)

        if coordinates is None:
            showinfo("Result",  f"Add '{added_surname}' surname with id"
                                f" [{surname_id}] to name dictionary '{added_name}' with id [{name_id}]")

            print(f"Add '{added_surname}' surname with id [{surname_id}] "
                  f"to name dictionary '{added_name}' with id [{name_id}]")

        else:
            showinfo("Result", f"Person with the name '{added_name}' and surname '{added_surname}' "
                               f"already exists in database and was detained at the coordinates of {coordinates}")

            print(f"Person with the name '{added_name}' and surname "
                  f"'{added_surname}' already exists in database and was detained at the coordinates of {coordinates}")


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Borderline Database')
        self.geometry('355x200')
        # self.resizable(False, False)


if __name__ == '__main__':
    app = App()
    person_database = Database()
    InputFrame(app)
    app.mainloop()

    # person_database.add_to_the_database("Andrii", "BanYk")
    # person_database.add_to_the_database("mAx", "BanYK")
    # person_database.add_to_the_database("Arsenii", "Banyk")
    # person_database.add_to_the_database("andrII", "Sizomin")
    # person_database.add_to_the_database("andrII", "Sizomin")
    # person_database.add_to_the_database("Maria", "Skladowska")
    # person_database.add_to_the_database("PatI", "SklAdowska")
    # person_database.add_to_the_database("MaX", "Bujalski")
    # person_database.add_to_the_database("mAx", "Bujalski")

    # person_database.show_name_flyweights()
    # SurnameFactory.show_surname_flyweights()
