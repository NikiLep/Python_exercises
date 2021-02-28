# File:         Ex6_3
# Author:       Niki Leppänen
# Description:  Inherit some animals from the Mammal class (that you created in Exercise 4).
#               Add data attribute for the noise the animal makes and the diet they have. Display your objects on screen
#               (= Print out the state of each object (use str-method)).

from Exercise_4 import Ex4_Mammal


class Animal(Ex4_Mammal.Mammal):
    def __init__(self):
        Ex4_Mammal.Mammal.__init__(self)
        self.__noise = "roar"
        self.__diet = "meat"

    def set_noise(self, noise):
        self.__noise = noise

    def set_diet(self, diet):
        self.__diet = diet

    def get_noise(self):
        return self.__noise

    def get_diet(self):
        return self.__diet

    def __str__(self):
        return f"""\nAnimal makes {self.__noise} noises and it eats {self.__diet}."""


def main():
    ani = Animal()
    ani.set_species(input("\nGive Species: "))
    ani.set_noise(input("\nGive Noise: "))
    ani.set_diet(input("\nGive Diet: "))
    print(ani)


main()
