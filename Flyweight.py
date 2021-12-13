import random
from Proxy import *


class Surname(object):
    def __init__(self, surname):
        self.surname = surname


class SurnameFactory:
    _surname: dict[str, Surname] = {}

    @staticmethod
    def get_person(surname):
        return SurnameFactory._surname.setdefault(surname, Surname(surname))

    @classmethod
    def show_surname_flyweights(cls):
        print("==============================================================")
        print("Surnames registered in database(surname flyweights):\n[" + " ".join(map(str, cls._surname.keys())), end="]\n")


class Name(object):
    def __init__(self, name):
        self.name = name

    def add_person_to_dictionary(self, surname):
        # print("Add {} surname with id [{}] to name dictionary {} with id [{}]".format(surname.surname, id(surname), self.name, id(self)))
        return surname.surname, id(surname), self.name, id(self)


class Database(object):
    _names: dict[str, Name] = {}

    def __init__(self):
        self.persons: dict[tuple, tuple] = {}
        self.people_count = 0

    def get_name(self, name):
        return self._names.setdefault(name, Name(name))

    def add_to_the_database(self, name, surname):
        tmp = ProxyPerson()
        checked_name, checked_surname = tmp.check_spelling(name, surname)
        added_surname, surname_id, added_name, name_id = self.get_name(checked_name)\
            .add_person_to_dictionary(SurnameFactory.get_person(checked_surname))

        if (added_name, added_surname) not in self.persons.keys():
            self.persons.setdefault((added_name, added_surname), (random.uniform(51.5, 53.95), random.uniform(23.15, 23.95)))
            print("Add '{}' surname with id [{}] to name dictionary '{}' with id [{}]".format(added_surname, surname_id, added_name, name_id))
            self.people_count += 1
        else:
            print(f"Person with the name '{added_name}' and surname '{added_surname}' already exists in base,"
                  f" was detained at the coordinates of "
                  f"{self.persons[(added_name, added_surname)][0]},{self.persons[(added_name, added_surname)][1]}")

        # print("Person dict length: ", len(self.persons))
        # print("Surname dict length:", self.get_name(checked_name).add_person_to_dictionary)

    def show_name_flyweights(self):
        print("==============================================================")
        print("Names registered in database(name_flyweights):\n["+" ".join(map(str, self._names.keys())), end=']\n')


# 53.93676763666636, 23.573060900509603
# 52.74302534181399, 23.92462340294286
# 52.234611402168106, 23.177553085272187
# 51.54300323270001, 23.59503355691168