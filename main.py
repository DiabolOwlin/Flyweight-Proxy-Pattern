from Flyweight import *

if __name__ == '__main__':
     person_database = Database()
     person_database.add_to_the_database("Andrii", "BanYk")
     person_database.add_to_the_database("mAx", "BanYK")
     person_database.add_to_the_database("Arsenii", "Banyk")
     person_database.add_to_the_database("andrII", "Sizomin")
     person_database.add_to_the_database("andrII", "Sizomin")
     person_database.add_to_the_database("Maria", "Skladowska")
     person_database.add_to_the_database("PatI", "SklAdowska")
     person_database.add_to_the_database("MaX", "Bujalski")
     person_database.add_to_the_database("mAx", "Bujalski")


     person_database.show_name_flyweights()
     SurnameFactory.show_surname_flyweights()
