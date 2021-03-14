# File:         Ex8_5
# Author:       Niki Leppänen
# Description:  Continue with the “Countries and Capitals” quiz. Give the user a chance to test his/her knowledge with
#               countries based on capitals.

d = {}

with open("/Users/Niki/Desktop/Olio-ohjelmointi/CountriesAndCapitals.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[val] = key


def game(dictionary):
    count = 0

    for i in range(10):
        key, value = dictionary.popitem()
        print(key, "is capital of...")
        capital = input()

        if capital == value:
            count += 1
            print("Correct!!")
        if capital != value:
            print("Wrong!!")

    print("\nThe number of correct answers: ", count)
    print("The number of incorrect answers: ", 10 - count)


def main():
    dictionary = d
    game(dictionary)


main()

