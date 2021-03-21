# File:         Ex8_5
# Author:       Niki Leppänen
# Description:  “Countries and Capitals” quiz.

d = {}

with open("/Users/Niki/Desktop/Olio-ohjelmointi/CountriesAndCapitals.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[key] = val


def game(dictionary):
    count = 0

    for i in range(10):
        key, value = dictionary.popitem()
        print("What is the capital of", key)
        capital = input()

        if capital == value:
            count += 1
            print("Correct!!")
        if capital != value:
            print("Wrong!!\nDid you mean ", value, "?")

    print("\nThe number of correct answers: ", count)
    print("The number of incorrect answers: ", 10 - count)


def main():
    dictionary = d
    game(dictionary)


main()
