# File:         Ex4_Car
# Author:       Niki Leppänen
# Description:  Create a car object. It has the following data attributes: make, model, mileage, price, color,
#               maximum load limit, size of trunk. Make them private. Write accessor and mutator methods to change them.
#               Add __str__method to print the state of the car.

class Car:

    def __init__(self):
        self.__make = "make"
        self.__model = "model"
        self.__mileage = 0
        self.__price = 0
        self.__color = "white"
        self.__max_load = 0
        self.__trunk_size = 0

    # Setters

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def set_color(self, color):
        self.__color = color

    def set_max_load(self, load):
        self.__max_load = load

    def set_trunk_size(self, trunk):
        self.__trunk_size = trunk

    # Getters

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def get_color(self):
        return self.__color

    def get_max_load(self):
        return self.__max_load

    def get_trunk_size(self):
        return self.__trunk_size

    # Returns objects state as a string
    def __str__(self):
        return f"""\nMaker: {self.__make}\nModel: {self.__model}\nMileage: {self.__mileage}km\nPrice: {self.__price}€
Color: {self.__color}\nMaximum load limit: {self.__max_load}kg\nSize of trunk: {self.__trunk_size}m^3"""

