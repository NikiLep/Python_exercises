# File:         Ex7_Cards
# Author:       Niki Leppänen
# Description:  Class for showing the card player got

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show_card(self):
        print("{} of {}".format(self.value, self.suit))

    def get_value(self):
        return self.value
