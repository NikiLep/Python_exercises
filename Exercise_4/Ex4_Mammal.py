# File:         Ex4_Mammal
# Author:       Niki Leppänen
# Description:  Create a mammal object. It has the following data attributes:
#               ID, species, name, size, weight and dimensions (height etc.).
#               Roll the dice, based on the result check if the correct mammal(based on ID)fits into your car’s trunk
#               (that you created in previous task).Also check that your mammal does not exceed the car’s load limit.

class Mammal:

    def __init__(self):
        self.__id = 0
        self.__species = ""
        self.__name = ""
        self.__size = ""
        self.__weight = 0
        self.__height = 0
        self.__width = 0
        self.__length = 0

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_species(self, species):
        self.__species = species

    def set_name(self, name):
        self.__name = name

    def set_size(self, size):
        self.__size = size

    def set_weight(self, weight):
        self.__weight = weight

    def set_height(self, height):
        self.__height = height

    def set_width(self, width):
        self.__width = width

    def set_length(self, length):
        self.__length = length

    # Getters
    def get_id(self):
        return self.__id

    def get_species(self):
        return self.__species

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def __str__(self):
        return f"""\nId: {self.__id}\nSpecies: {self.__species}\nName: {self.__name}\nSize: {self.__size}
Weight: {self.__weight}\nHeight: {self.__height}\nWidth: {self.__width}\nLength: {self.__length}"""

