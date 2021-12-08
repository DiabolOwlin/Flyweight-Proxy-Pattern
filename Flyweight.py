class Surname(object):
    def __init__(self, surname):
        self.surname = surname


class PersonFactory:
    people = {}

    @staticmethod
    def get_person(surname):
        return PersonFactory.people.setdefault(surname, Surname(surname))


class NameBranch(object):
    def __init__(self, name):
        self.name = name

    def add_person_to_dictionary(self, surname):
        print("Add {} surname with id [{}] to name dictionary {} with id [{}]".format(surname.surname, id(surname), self.name, id(self)))


class Database(object):
    def __init__(self):
        self.people_count = 0
        self.names = {}

    def get_name(self, name):
        return self.names.setdefault(name, NameBranch(name))

    def add_to_the_database(self, surname, name):
        self.get_name(name).add_person_to_dictionary(PersonFactory.get_person(surname))
        self.people_count += 1


# if __name__ == '__main__':
#     registered_people = Database()
#     registered_people.add_to_the_database("Banyk", "Andrii")
#     registered_people.add_to_the_database("Sizomin", "Bohdan")
#     registered_people.add_to_the_database("Sizomin", "Andrii")
#     registered_people.add_to_the_database("Alexey", "Plakhin")