# File:         Ex6_5
# Author:       Niki Leppänen
# Description:  Change your task 3 code like this: Inherit a domestic animal from Mammal.
#               Also inherit a wild animal from Mammal.
#               Then inherit a few domestic and wild animals from those classes and print them out.
#               Each mammal should make unique noise and have a certain diet as additional data attributes.
#               Add some relevant attributes. Display your objects on screen.

from Exercise_4 import Ex4_Mammal


class DAnimal(Ex4_Mammal.Mammal):
    def __init__(self):
        super().__init__()
        self.__noise = "squeak"
        self.__diet = "vegetables"
        self.__info = ""

    def set_noise(self, noise):
        self.__noise = noise

    def set_diet(self, diet):
        self.__diet = diet

    def set_info(self, info):
        self.__info = info

    def get_noise(self):
        return self.__noise

    def get_diet(self):
        return self.__diet

    def get_info(self):
        return self.__info

    def __str__(self):
        return f"""\nAnimal makes {self.__noise} noises and it eats {self.__diet}.\n Other info: {self.__info}"""


class WAnimal(Ex4_Mammal.Mammal):
    def __init__(self):
        super().__init__()
        self.__noise = "roar"
        self.__diet = "meat"
        self.__appear = "savanna"

    def set_noise(self, noise):
        self.__noise = noise

    def set_diet(self, diet):
        self.__diet = diet

    def set_appear(self, appear):
        self.__appear = appear

    def get_noise(self):
        return self.__noise

    def get_diet(self):
        return self.__diet

    def get_appear(self):
        return self.__appear

    def __str__(self):
        return f"""\nAnimal makes {self.__noise} noises and it eats {self.__diet}.\nAppears in {self.__appear}."""


def domestic(list):
    dom = DAnimal()
    dom.set_species(input("Give a domestic animal: "))
    dom.set_noise(input("What kind of noise it makes: "))
    dom.set_diet(input("What does it eat: "))
    dom.set_info(input("Other useful info for owner: "))
    list.append(dom)

def wild_ani(list):
    wild = WAnimal()
    wild.set_species(input("Give a wild animal: "))
    wild.set_noise(input("What kind of noise it makes: "))
    wild.set_diet(input("What does it eat: "))
    wild.set_appear(input("Where this animal appears: "))
    list.append(wild)


def main():
    domestic_list = []

    wild_list = []

    domestic(domestic_list)
    domestic(domestic_list)

    wild_ani(wild_list)
    wild_ani(wild_list)

    for i in domestic_list:
        print("\nAnimal: ", i.get_species())
        print(i)

    for i in wild_list:
        print("\nAnimal: ", i.get_species())
        print(i)

main()