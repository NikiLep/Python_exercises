# File:         Ex4_6
# Author:       Niki Leppänen
# Description:  Create different cell phone objects (which have different data attribute values,
#               use mutator methods to change the data attribute values).
#               Print out each object’s state (use the __str__ method in the cell phone class).

from Exercise_4.Ex4_Dice import Dice
from Exercise_4.Ex4_CellPhone import CellPhone

cell1 = CellPhone()
cell2 = CellPhone()
cell3 = CellPhone()
cell4 = CellPhone()
cell5 = CellPhone()
cell6 = CellPhone()


def main():

    phone_list = []

    def ask_phones(cell):
        cell.set_id(int(input("\nGive id: ")))
        cell.set_manufact(input("What manufacturer: "))
        cell.set_model(input("What model: "))
        cell.set_retail_price(float(input("What is the retail price: ")))

        phone_list.append(cell)

    my_dice = Dice()

    my_dice.roll()

    ask_phones(cell1)
    ask_phones(cell2)
    ask_phones(cell3)
    ask_phones(cell4)
    ask_phones(cell5)
    ask_phones(cell6)

    for item in phone_list:
        if item.get_id() == my_dice.get_sidenumber():
            print(item)


main()
