from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name_and_surname(self):
        return self.name, self.surname

    @abstractmethod
    def check_spelling(self, content =''):
        pass


class RealPerson(Person):

    def check_spelling(self, content=''):
        print("Real Subject is doing something...")


class ProxyPerson(Person):

    def __init__(self, name, surname, subject):
        super().__init__(name, surname)
        self.real_subject = subject

    def check_spelling(self, content =''):
        self.pre_check_spelling()

        if self.real_subject is not None:
            self.real_subject.check_spelling(content)
        self.after_check_spelling()

    def pre_check_spelling(self):
        print("before check_spelling()")

    def after_check_spelling(self):
        print("after check_spelling()")


class NotInAHurry(Person):

    def __init__(self, name, surname, additional_info=''):
        super().__init__(name, surname)
        self.additional_info = additional_info

    def get_additional_info(self):
        return self.additional_info

    def check_spelling(self, content =''):
        print(" Officer insert {} {} with proper spelling to the database".format(self.get_name_and_surname()[0], self.get_name_and_surname()[1]))


class InAHurry(ProxyPerson):

    def __init__(self, name, surname, program):
        super().__init__(name, surname, program)

    def pre_check_spelling(self):
        print("[Proxy] {} saying: I`m going to check if the data is valid on behalf of {}".format(self.get_name_and_surname(), self.real_subject.get_name_and_surname()))

    def after_check_spelling(self):
        print("[Proxy] {} saying: I`ve checked the validation of the data on behalf of {}".format(
                self.get_name_and_surname(), self.real_subject.get_name_and_surname()))


if __name__ == "__main__":
    print("===========================")
    officer = NotInAHurry("Banyk", "Andrii")
    officer.check_spelling("Rose")

    print("===========================")

    program = InAHurry("banYk", "aNdrii", officer)
    program.check_spelling("chocolate")