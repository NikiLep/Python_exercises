# File:         player
# Author:       Niki Leppänen
# Description:  Class for keeping up who is playing and their money

class Player:
    def __init__(self, name):
        self.__money = 100
        self.__player_ID = 0
        self.__name = name
        self.__score = 0
        self.__hand = ""

    def set_money(self, money):
        self.__money = money

    def set_ID(self, id):
        self.__player_ID = id

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def set_hand(self, hand):
        self.__hand = hand

    def get_money(self):
        return self.__money

    def get_id(self):
        return self.__player_ID

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_hand(self):
        return self.__hand

    def __str__(self):
        return f"""Money: {self.__money}"""
