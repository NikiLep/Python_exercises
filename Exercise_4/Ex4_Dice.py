# File:         Ex4_Dice
# Author:       Niki Leppänen
# Description:  Create different cell phone objects (which have different data attribute values,
#               use mutator methods to change the data attribute values).
#               Print out each object’s state (use the __str__ method in the cell phone class).

from random import randint


class Dice:

    # initialize side of the dice, color of the side and color of the number
    def __init__(self):
        self.sidenumber = 1

    # The roll method generated random number.
    def roll(self):
        self.sidenumber = randint(1, 6)

    def get_sidenumber(self):
        return self.sidenumber
