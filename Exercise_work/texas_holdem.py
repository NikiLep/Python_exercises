
from Exercise_work.player import Player
from Exercise_work.deck import Deck
from Exercise_work.cards import Card


def game():

    # sorting function
    def highest(list):
        for step in range(1, len(list)):
            key = list[step]
            j = step - 1

            while j >= 0 and key.get_value() > list[j].get_value():
                list[j + 1] = list[j]
                j = j - 1

            list[j + 1] = key

    # Straight flush = 1
    # Four of a kind = 2
    # Full house = 3
    # Flush = 4
    # Straight = 5
    # Three of a kind = 6
    # Two pair = 7
    # Pair = 8
    # High Card = 9
    def check_pair(hand):
        highest(hand)

        if len(hand) < 2:
            return
        elif hand[0].get_value() == hand[1].get_value():
            score = 15 + hand[0].get_value()
            print("pari")
            return score
        else:
            check_pair(hand[1:])

    def check_triple(hand):
        highest(hand)

        if len(hand) < 3:
            return
        elif hand[0].get_value() == hand[1].get_value() == hand[2].get_value():
            score = 45 + hand[0].get_value()
            print("kolmoset")
            return score
        else:
            check_triple(hand[1:])

    def check_four(hand):
        highest(hand)

        if len(hand) < 4:
            return
        elif hand[0].get_value() == hand[1].get_value() == hand[2].get_value() == hand[3].get_value():
            score = 105 + hand[0].get_value()
            print("neloset")
            return score
        else:
            check_four(hand[1:])

    def check_two_pairs(hand):
        highest(hand)
        pairs = []

        def check(hand2):
            if len(hand2) < 2:
                return
            elif hand2[0].get_value() == hand2[1].get_value():
                pairs.append(hand2[:2])
            else:
                check(hand2[1:])

        check(hand)

        if len(pairs) == 4:
            score = 30
            for i in pairs:
                score + i.get_value()
            print("kaksi paria")
            return score
        else:
            return




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

    # Gives everyone 5 cards at the beginning
    for n in range(5):
        for i in players_cards:
            i.append(deck.draw_card())


    print()

    for i in players_cards:
        print()
        for c in i:
            c.show_card()

    print()


    check_pair(player_c)
    check_triple(player_c)
    check_four(player_c)
    check_two_pairs(player_c)


game()
