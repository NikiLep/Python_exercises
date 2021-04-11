
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

    # Straight flush = 120 - 134
    # Four of a kind = 105 - 119
    # Full house = 90 - 104
    # Flush = 75 - 89
    # Straight = 60 - 74
    # Three of a kind = 45 - 59
    # Two pair = 30 - 44
    # Pair = 15 - 29
    # High Card = 2 - 14
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

        if hand[0].get_value() == hand[1].get_value() and hand[2].get_value() == hand[3].get_value():
            pairs.append(hand[0].get_value())
            pairs.append(hand[1].get_value())
            pairs.append(hand[2].get_value())
            pairs.append(hand[3].get_value())

        elif hand[0].get_value() == hand[1].get_value() and hand[3].get_value() == hand[4].get_value():
            pairs.append(hand[0].get_value())
            pairs.append(hand[1].get_value())
            pairs.append(hand[3].get_value())
            pairs.append(hand[4].get_value())

        elif hand[1].get_value() == hand[2].get_value() and hand[3].get_value() == hand[4].get_value():
            pairs.append(hand[1].get_value())
            pairs.append(hand[2].get_value())
            pairs.append(hand[3].get_value())
            pairs.append(hand[4].get_value())

        if len(pairs) == 4:
            score = 0
            print("kaks paria")
            for i in pairs:
                score += i

            score = score / 4 + 30

            return score

    def check_straight(hand):
        highest(hand)

        if (hand[0].get_value() - 1 == hand[1].get_value() and hand[1].get_value() - 1 == hand[2].get_value() and
                hand[2].get_value() - 1 == hand[3].get_value() and hand[3].get_value() - 1 == hand[4].get_value()):

            score = 60 + hand[0].get_value()
            print("Suora")
            return score

        else:
            return 0

    def check_flush(hand):

        highest(hand)

        if (hand[0].get_suit() == hand[1].get_suit() and hand[1].get_suit() == hand[2].get_suit() and
                hand[2].get_suit() == hand[3].get_suit() and hand[3].get_suit() == hand[4].get_suit()):
            score = 75 + hand[0].get_value()
            print("Väri")
            return score

        else:
            return 0

    def check_straight_flush(hand):

        if check_flush(hand) > 75 and check_straight(hand) > 60:
            highest(hand)
            score = 120 + hand[0].get_value()
            print("Väri suora")

        else:
            return

    def check_full_house(hand):
        highest(hand)

        score = 0

        if (hand[0].get_value() == hand[1].get_value()
                and hand[2].get_value() == hand[3].get_value() == hand[4].get_value()):

            for i in hand:
                score += i.get_value()

            score /= 5
            score += 90

            print(score)
            print("Täyskäsi")

        elif (hand[0].get_value() == hand[1].get_value() == hand[2].get_value()
              and hand[3].get_value() == hand[4].get_value()):

            for i in hand:
                score += i.get_value()

            score /= 5
            score += 90

            print(score)
            print("Täyskäsi")

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
    # for n in range(5):
        # for i in players_cards:
            # i.append(deck.draw_card())
    player_c.append(Card("Spades", 14))
    player_c.append(Card("Spades", 14))
    player_c.append(Card("Spades", 14))
    player_c.append(Card("Spades", 13))
    player_c.append(Card("Spades", 13))


    print()

    for i in players_cards:
        print()
        for c in i:
            c.show_card()

    print()


    check_full_house(player_c)


game()
