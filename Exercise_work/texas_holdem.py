from collections import Counter

from Exercise_work.player import Player
from Exercise_work.deck import Deck
from Exercise_work.cards import Card


def game():
    # adds card to table
    def add_to_table():
        table.append(deck.draw_card())

    # Straight flush = 1
    # Four of a kind = 2
    # Full house = 3
    # Flush = 4
    # Straight = 5
    # Three of a kind = 6
    # Two pair = 7
    # Pair = 8
    # High Card = 9
    def check_pairs(hand):
        first = 0
        second = 0
        r = 0
        pair_in_hand = False
        for c in hand:
            r += 1
            for i in table:
                if c.get_value() == i.get_value():
                    if r == 1:
                        first += 1
                    elif r == 2:
                        second += 1

        if hand[0].get_value() == hand[1].get_value():
            pair_in_hand = True

        # check for full house
        if first == 2 and second == 1 or second == 2 and first == 1:
            return 3
        # check for two pairs
        elif first == 1 and second == 1 and first != second:
            return 7
        # check same cards with first card in hand
        elif first > second:
            # four of a kind
            if first == 3 or pair_in_hand and first == 2:
                return 2
            # three of a kind
            elif first == 2 or pair_in_hand and first == 1:
                return 6
            # pair
            elif first == 1 or pair_in_hand:
                return 8
        # check same cards with second card in hand
        elif first < second:
            # four of a kind
            if second == 3:
                return 2
            # three of a kind
            elif second == 2:
                return 6
            # pair
            elif second == 1:
                return 8

    table = []

    deck = Deck()
    # !!!!PLAYER POIS!!!!
    player = Player()
    computer1 = Player()
    computer2 = Player()
    computer3 = Player()

    players = [player, computer1, computer2, computer3]
    comp_c1 = []
    comp_c2 = []
    comp_c3 = []
    player_c = []
    players_cards = [comp_c1, comp_c2, comp_c3, player_c]

    deck.shuffle_deck()

    # Gives everyone two cards at the beginning
    for n in range(2):
        for i in players_cards:
            i.append(deck.draw_card())

    # Places three cards on the table
    for c in range(3):
        card = deck.draw_card()
        table.append(card)

    add_to_table()
    add_to_table()

    for i in table:
        i.show_card()

    print()

    for i in players_cards:
        print()
        for c in i:
            c.show_card()

    check_pairs(player_c)


game()