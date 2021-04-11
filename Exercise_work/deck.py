# File:         deck
# Author:       Niki Leppänen
# Description:  Class for creating deck and getting cards out of the deck for player

import random
from Exercise_work.cards import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.build()


    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(2, 15):
                self.cards.append(Card(s, v))

    def show_deck(self):
        for c in self.cards:
            c.show_card()

    def shuffle_deck(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop()
