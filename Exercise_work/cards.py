# File:         cards
# Author:       Niki Leppänen
# Description:  Class for creating cards and getting its value


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show_card(self):
        print("{} of {}".format(self.value, self.suit))

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def __str__(self):
        return f'''{self.value}{self.suit}'''

