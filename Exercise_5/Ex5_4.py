# File:         Ex4_3
# Author:       Niki Leppänen
# Description:  Create multiple dices (at least three) and put them in a list.
# See that your dice can be rolled and the side can be shown.
# Create a small game where the best sum of three rolls wins.
# If the sum is a tie, tied dices are rolled as long as a winner is found (best side wins).
# Use functions and pass objects (or list of objects) as arguments. Use informative and clear output prints.

from Exercise_4.Ex4_Dice import Dice


# insertion sort for game after some sums are tied
def insert(list):
    for i in list:
        print("Player"+str(i.get_id()), "rolled: ", str(i.get_sidenumber()))

    for step in range(1, len(list)):
        key = list[step]
        j = step - 1

        while j >= 0 and key.get_sidenumber() > list[j].get_sidenumber():
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = key

    # takes then largest sums and adds them to a different list
    n = 1
    largest = [list[0]]
    for item in list:
        while n < len(list):
            if item.get_sidenumber() == list[n].get_sidenumber():
                largest.append(list[n])
            n += 1

    # if theres many same sums, rolls those again as long as winner is found
    if len(largest) == 1:
        print("\nWinner is player" + str(largest[0].get_id()) + "!!")
        return
    else:
        print("\nTie between ", len(largest), " sidenumbers, rolling once again.")
        for i in largest:
            i.roll()
        return insert(largest)


def winner(list):

    for i in list:
        print("Player"+str(i.get_id()), "rolled: ", str(i.get_sum()))

    for step in range(1, len(list)):
        key = list[step]
        j = step - 1

        while j >= 0 and key.get_sum() > list[j].get_sum():
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = key

    # takes then largest sums and adds them to a different list
    n = 1
    largest = [list[0]]
    for item in list:
        while n < len(list):
            if item.get_sum() == list[n].get_sum():
                largest.append(list[n])
            n += 1

    # if theres many same sums, rolls those again as long as winner is found
    if len(largest) == 1:
        print("\nWinner is player" + str(largest[0].get_id()) + "!!")
        return
    else:
        print("\nTie between ", len(largest), " sums, rolling once again.")
        for i in largest:
            i.roll()
        return insert(largest)


def main():
    player_list = []
    amount = int(input("How many players: "))

    for a in range(amount):
        my_dice = Dice()
        my_dice.set_id(a+1)
        player_list.append(my_dice)

    for r in range(3):
        print("Rolling round: ", r+1, "\n")

        for item in player_list:
            item.roll()

        for item in player_list:
            item.sum()

    winner(player_list)


main()


