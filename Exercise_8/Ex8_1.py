# File:         Ex8_1
# Author:       Niki Leppänen
# Description:  Code a cleaning bot using following data attributes: floor, windows, surfaces, bed. In addition bot
#               needs to prepare for the lockdown by filling fridge and hoard toilet paper.

class Flat:
    def __init__(self):
        self.__floor = "dirty"
        self.__windows = "dirty"
        self.__surfaces = "dusty"
        self.__bed_made = "a mess"
        self.__food = "a little bit"
        self.__paper = "a little bit"

    def set_floor(self, floors):
        self.__floor = floors

    def set_windows(self, windows):
        self.__windows = windows

    def set_surfaces(self, surfaces):
        self.__surfaces = surfaces

    def set_bed(self, bed):
        self.__bed_made = bed

    def set_food_amount(self, food):
        self.__food = food

    def set_paper(self, paper):
        self.__paper = paper

    def get_floor(self):
        return self.__floor

    def get_windows(self):
        return self.__windows

    def get_surfaces(self):
        return self.__surfaces

    def get_bed(self):
        return self.__bed_made

    def get_food(self):
        return self.__food

    def get_paper(self):
        return self.__paper

    def __str__(self):
        return f"""###STATE OF SPRING CLEAN###
Floor is {self.__floor}.\nWindows are {self.__windows}.\nSurfaces are {self.__surfaces}.
Bed is {self.__bed_made}.\nThere is {self.__food} amount of food in fridge and {self.__paper} toilet paper in storage.
-----------------------------------------------------------------------------------------"""


def main():
    flat = Flat()

    print(flat)
    print("First Object: Clean windows and make bed.")
    print("\nCleaning windows\n...")
    flat.set_windows("clean")
    print("Windows are clean\n\nMaking bed now\n...")
    flat.set_bed("made")
    print("Bed has been made\n")

    print(flat)

    print("Next object: Vacuum floors and dust surfaces.")
    print("\nVacuuming floors\n...")
    flat.set_floor("clean")
    print("Floors are vacuumed\n\nDusting surfaces\n...")
    flat.set_surfaces("dusted")
    print("Surfaces are dusted\n")

    print(flat)

    print("Next object: Buy food and hoard toilet paper.")
    print("Going to store\n...\nGetting canned food\n...")
    flat.set_food_amount("great")
    print("Food storage is filled\nNow hoarding toilet paper\n...")
    flat.set_paper("too much")
    print("Paper storage is filled and overflowing.\n")

    print(flat)

    print("Spring cleaning is done!")
    print("Shutting down...")


main()
