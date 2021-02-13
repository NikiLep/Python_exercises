# File:         Ex5_5
# Author:       Niki Leppänen
# Description:  Create a class called Player. Player has at least the following data attributes: first name,
# last name and a player id. Remember to code accessor and mutator methods and str-method.
# Create a dictionary so that the player id is a key and each player has one dice.
# Roll each player’s dice and print out each player’s dice’s side. Use informative and clear output print.
from Exercise_4.Ex4_Dice import Dice


class Player(Dice):

    def __init__(self):
        super().__init__()
        self.first_name = "first"
        self.last_name = "last"
        self.id = 0

    def set_first_name(self, first):
        self.first_name = first

    def set_last_name(self, last):
        self.last_name = last

    def set_id(self, id):
        self.id = id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_id(self):
        return self.id

    def __str__(self):
        return f'''\nID: {self.id}\nFirst name: {self.first_name}\nLast name: {self.last_name}
Rolled: {self.get_sidenumber()}'''


def main():
    player = Player()

    player_dct = {}

    amount = int(input("How many players: "))

    for i in range(amount):
        id = int(input("Give id: "))
        first = input("First name: ")
        last = input("Last name: ")

        player.set_id(id)
        player.set_first_name(first)
        player.set_last_name(last)

        print("Rolling dice for ", player.get_first_name(), player.get_last_name())

        player.roll()

        player_dct[str(player.get_id())] = player.get_sidenumber()

    print("Players rolled:")

    for key, value in player_dct.items():
        print("Player"+key, " : ", value)


main()
