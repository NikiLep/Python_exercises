# File:         Ex8_3
# Author:       Niki Leppänen
# Description:  Code cookie baker that asks user what flavor he wants. Includes random flavor method.
from random import randint


class Cookies:
    def __init__(self):

        self.__frosting = False

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
    while True:
        print("Let's bake 10 cookies!!\n")
        cookies = []

        while len(cookies) < 10:
            cookie = Cookies()
            cookies.append(cookie)

        print("Now we have ", len(cookies), " baked cookies\n")

        print("What flavor of frosting do you want?\nBy typing 'random' you get random flavor out of six option.")
        for i in cookies:
            if not i.get_frosting():
                print("\nCookie number", cookies.index(i) + 1)
                flavor = input()
                if flavor == "random":
                    i.random_flavor()
                else:
                    i.set_frosting(flavor)

        for i in cookies:
            print("[", cookies.index(i) + 1, "]", i)

        while True:
            ask = input("\nDo you like the flavors? [YES/NO]")
            if ask == "NO":
                print("Let's make a new batch!\n...")
                break
            elif ask == "YES":
                print("\nEnjoy your cookies :)")
                break
            else:
                print("\nIncorrect input")
        if ask == "YES":
            break


main()
