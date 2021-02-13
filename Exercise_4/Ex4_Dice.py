# File:         Ex4_Dice
# Author:       Niki Leppänen
# Description:  Includes dice class which returns 1 - 6 as a value of six side dice.

from random import randint


class Dice:

    # initialize side of the dice, color of the side and color of the number
    def __init__(self):
        self.__sidenumber = 1
        self.__sum = 0
        self.__id = 1

    # The roll method generated random number.
    def roll(self):
        self.__sidenumber = randint(1, 6)

    def get_sidenumber(self):
        return self.__sidenumber

    def sum(self):
        self.__sum += self.__sidenumber

    def get_sum(self):
        return self.__sum

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id
