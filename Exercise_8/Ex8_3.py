# File:         Ex8_1
# Author:       Niki Leppänen
# Description:  Code cookie baker that asks user what flavor he wants. Includes random flavor method.
from random import randint


class Cookies:
    def __init__(self):

        self.__frosting = "flavor"

    def set_frosting(self, frosting):
        self.__frosting = frosting

    def get_frosting(self):
        return self.__frosting

    def random_flavor(self):
        r = randint(1, 6)
        if r == 1:
            self.__frosting = "double chocolate"
        elif r == 2:
            self.__frosting = "caramel"
        elif r == 3:
            self.__frosting = "lemon"
        elif r == 4:
            self.__frosting = "buttercream"
        elif r == 5:
            self.__frosting = "coconut pecan"
        elif r == 6:
            self.__frosting = "dark chocolate"

    def __str__(self):
        return f"""Cookie flavor: {self.__frosting}"""


def main():
    c_amount = int(input("How many cookies do you want to be baked?\n"))
    cookies = []

    for i in range(c_amount):
        cookie = Cookies()
        print("\nWhat flavor do you want on your cookie number ", i + 1)
        flavor = input('Write down desired flavor or write "random" for random flavor.\n')

        if flavor == "random":
            cookie.random_flavor()
        else:
            cookie.set_frosting(flavor)

        print(cookie)
        cookies.append(cookie)

    print()
    print("Baked cookies:")
    for i in cookies:
        print(i)


main()
