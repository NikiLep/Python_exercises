# File:         Ex7_4
# Author:       Niki Leppänen
# Description:  Take the code main.py from Itslearning,do not change it. Implement classes Card and Deck
#               (in their own modules) so that the main.py can be run and the output is exactly the same than in file
#               Ex7_task4_output.txt

from Exercise_7 import Ex7_cards as card
from Exercise_7 import Ex7_deck as deck


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

    # Draw 3 cards, highest value wins

    cards = []

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


main()
