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
        temporary_hand = []
        for i in hand:
            temporary_hand.append(i.get_value())
        for i in table:
            temporary_hand.append(i.get_value())

        values = Counter(temporary_hand)
        values.most_common()
        first = 0
        for k,v in values:
            print(k)
            print(v)
        print(values)
        print(first)


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