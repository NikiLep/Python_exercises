# File:         Ex7_4
# Author:       Niki Leppänen
# Description:  Take the code main.py from Itslearning,do not change it. Implement classes Card and Deck
#               (in their own modules) so that the main.py can be run and the output is exactly the same than in file
#               Ex7_task4_output.txt

from Exercise_7 import Ex7_cards as card
from Exercise_7 import Ex7_deck as deck


# Draw 3 cards, highest value wins
def highest_value_game():
    cards = []
    my_deck = deck.Deck()

    print("\nLet's draw 3 cards and take the highest value.")
    for c in range(1, 4):
        card2 = my_deck.draw_card()
        cards.append(card2)

    print("Cards are:\n")
    for i in cards:
        i.show_card()

    highest(cards)

    winner(cards)


# sorting function
def highest(list):
    for step in range(1, len(list)):
        key = list[step]
        j = step - 1

        while j >= 0 and key.get_value() > list[j].get_value():
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = key


# function for checking winner or tie
def winner(list):
    my_deck = deck.Deck()

    # prints out the winner
    if list[0].get_value() > list[1].get_value():
        print("\nHighest value card is: ")
        list[0].show_card()
        return

    # two of the cards had the same value
    elif list[0].get_value() == list[1].get_value() and list[0].get_value() != list[2].get_value():
        while True:
            print("\nThere is a tie, two highest value cards will be drawn again!")

            list[0] = my_deck.draw_card()
            list[1] = my_deck.draw_card()

            list[0].show_card()
            list[1].show_card()

            if list[0].get_value() > list[1].get_value():
                print("\nHighest value card is: ")
                list[0].show_card()
                break
            elif list[1].get_value() > list[0].get_value():
                print("\nHighest value card is: ")
                list[1].show_card()
                break

    # all the cards had same value
    elif list[0].get_value() == list[2].get_value():
        print("\nAll the values were the same, all the cards will be drawn again!")
        list[0] = my_deck.draw_card()
        list[1] = my_deck.draw_card()
        list[2] = my_deck.draw_card()

        highest(list)

        winner(list)


# function for showing dealers hand
def dealer_cards(list):
    dealer_hand = ""

    for i in list:
        dealer_hand += i.show_card() + ", "

    return dealer_hand


# function for showing players hand
def player_cards(list):
    player_hand = ""

    for i in list:
        player_hand += i.show_card() + ", "

    return player_hand


# function for checking sum of card values in hand
def hand_value(list):
    value = 0

    for i in list:
        if i.get_value() > 10:
            value += 10
        elif 1 < i.get_value() < 11:
            value += i.get_value()
        else:
            int(input("You have a ace, is it 1 or 11: "))

    return value


def twentyone():
    print("\nBLACK JACK\n")

    dealer = []
    player = []

    # Draws the first 2 cards for player and dealer
    my_deck = deck.Deck()
    my_deck.shuffle_deck()

    player_1st = my_deck.draw_card()
    player.append(player_1st)

    dealer_1st = my_deck.draw_card()
    dealer.append(dealer_1st)

    player_2nd = my_deck.draw_card()
    player.append(player_2nd)

    dealer_2nd = my_deck.draw_card()
    dealer.append(dealer_2nd)

    print("Dealer: \n", dealer[0].show_card(), ", other not showing yet.")

    print("Player: \n", player_cards(player))
    print("Players hand value: ", hand_value(player))

    # adding cards to players hand as long as player wants, value goes over or gets value equal to 21
    while True:
        ans = input("\nHIT or STAY: ")
        if ans == "HIT":
            print("\nDrawing a new card...")
            player_card = my_deck.draw_card()
            player.append(player_card)
            print(player_cards(player))
            print("Players hand value: ", hand_value(player))
            if hand_value(player) > 21:
                print("BUST, you lose!")
                return
            elif hand_value(player) == 21:
                print("21, you win!")
                return
        else:
            print("Stay\n")
            break

    print("\nRevealing dealers other card...")

    # adding cards for dealer and checking who wins
    while True:
        print(dealer_cards(dealer))
        if 17 <= hand_value(dealer) <= 21:
            print("Players hand value: ", hand_value(player))
            print("Dealers hand value: ", hand_value(dealer))
            if hand_value(dealer) > hand_value(player):
                print("\nDealer won!!")
                break
            elif hand_value(dealer) == hand_value(player):
                print("\nTie")
                break
            elif hand_value(dealer) < hand_value(player):
                print("\nYou win!!")
                break
        elif hand_value(dealer) < 17:
            print("\nDealer takes another card...")
            dealer_card = my_deck.draw_card()
            dealer.append(dealer_card)
        elif hand_value(dealer) > 21:
            print("Dealers hand value: ", hand_value(dealer))
            print("\nDealer went over, you won!!")
            break
        else:
            break


def main():
    print("Let's test that a single card works...")

    my_card = card.Card("Hearts", 12)
    my_card.show_card()
    print(my_card)

    print("Single card testing is over.\n")

    print("Let's test that a deck of card is created...")

    my_deck = deck.Deck()
    my_deck.show_deck()

    print("Card deck testing is over.\n")

    print("Let's shuffle the deck.")
    my_deck.shuffle_deck()

    print("Let's test that a deck of card is shuffled...")

    my_deck.show_deck()

    print("Cards should be suffled now.\n")

    print("Let's draw 2 cards and show them.")
    print("You draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
    print("Your opponent draw:")
    card1 = my_deck.draw_card()
    card1.show_card()

    # Code your Exercise 7 task 4 game here.

    # highest_value_game()

    twentyone()


main()
