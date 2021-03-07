from Exercise_7.Pets import Pets


class Student:
    def __init__(self):
        self.__fname = ""
        self.__lname = ""
        self.__student_ID = 0
        self.__pets = []
        self.pets()

    def set_fname(self, f):
        self.__fname = f

    def set_lname(self, l):
        self.__lname = l

    def set_student_ID(self, id):
        self.__student_ID = id

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_student_ID(self):
        return self.__student_ID

    def add_pets(self):
        species = input("Species of the pet: ")
        name = input("Name of the pet: ")
        self.__pets.append(Pets(name, species))

    def remove_pets(self, num):
        self.__pets.pop(num - 1)

    def print_pets(self):
        print("\nList of your pets: ")
        for i in range(len(self.__pets)):
            print("[", i + 1, "]", self.__pets[i])

    def pets(self):
        self.set_fname(input("First name: "))
        self.set_lname(input("First name: "))
        self.set_student_ID(int(input("ID: ")))

        for p in range(int(input("How many pets do you have: "))):
            species = input("Species of the pet: ")
            name = input("Name of the pet: ")
            self.__pets.append(Pets(name, species))

    def __str__(self):
        return f"""\nName: {self.__fname} {self.__lname}\nStudent ID: {self.__student_ID}"""