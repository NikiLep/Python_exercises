# File:         Ex4_8
# Author:       Niki Leppänen
# Description:  Create a mammal object. It has the following data attributes:
#               ID, species, name, size, weight and dimensions (height etc.).
#               Roll the dice, based on the result check if the correct mammal(based on ID)fits into your car’s trunk
#               (that you created in previous task).Also check that your mammal does not exceed the car’s load limit.

from Exercise_4.Ex4_Dice import Dice
from Exercise_4.Ex4_Car import Car
from Exercise_4.Ex4_Mammal import Mammal

mammal1 = Mammal()
mammal2 = Mammal()
mammal3 = Mammal()
mammal4 = Mammal()
mammal5 = Mammal()
mammal6 = Mammal()

car = Car()

dice = Dice()


def main():

    mammal_list = []

    dice.roll()

    car.set_make(input("\nGive maker: "))
    car.set_model(input("Give model: "))
    car.set_mileage(int(input("Give mileage: ")))
    car.set_price(float(input("Give price: ")))
    car.set_color(input("Give color: "))
    car.set_max_load(int(input("Give maximum load: ")))
    car.set_trunk_size(float(input("Give trunk size(m^3): ")))

    def ask_mammals(mammal):
        mammal.set_id(int(input("\nGive id: ")))
        mammal.set_species(input("Give species: "))
        mammal.set_name(input("Give name: "))
        mammal.set_size(input("Give size: "))
        mammal.set_weight(float(input("Give weight: ")))
        mammal.set_height(float(input("Give height: ")))
        mammal.set_width(float(input("Give width: ")))
        mammal.set_length(float(input("Give length: ")))

        mammal_list.append(mammal)

    ask_mammals(mammal1)
    ask_mammals(mammal2)
    ask_mammals(mammal3)
    ask_mammals(mammal4)
    ask_mammals(mammal5)
    ask_mammals(mammal6)

    for item in mammal_list:
        if item.get_id() == dice.get_sidenumber():
            print(item)

            dimensions = item.get_height() * item.get_width() * item.get_length() * 1 * 10**-6

            if dimensions <= car.get_trunk_size() and item.get_weight() <= car.get_max_load():
                print("\nMammal fits into the car and do not exceed the car's load limit")
            else:
                print("\nMammal ether does not fit into your car or it is too heavy.")


main()
