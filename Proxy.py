from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):

    @abstractmethod
    def check_spelling(self, name, surname):
        pass


class ProxyPerson(Person):

    def __init__(self):
        pass

    def check_spelling(self, name, surname):
        name = name.lower()
        name = name.capitalize()

        surname = surname.lower()
        surname = surname.capitalize()

        return name, surname


