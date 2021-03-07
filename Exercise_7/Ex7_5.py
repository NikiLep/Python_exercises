# File:         Ex7_5
# Author:       Niki Leppänen
# Description:  Implement the following UML diagram. Try to figure out the best way to have animals in appropriate data
#               structure in the Student class (see the link in Task 4 above, there is an example of Deck class creating
#               a deck of cards, pay attention to the relationship between the Deck class and Card class and think how
#               that information can be applied in the relationship between the Student class and Animal class).
#               Pet Class can also be called Animal (you most likely have implemented that in previous exercises).Think
#               (carefully), do you need to have the owner of the pet information in the Pet/Animal class
#               (in order to make the relationship between Student and Pet)If yes, add that.

from Exercise_7.Student import Student
from Exercise_7.Pets import Pets


def main():
    student = Student()

    print(student)

    while True:
        student.print_pets()
        print("____________________________________________")
        print("\n[1] ADD A PET \n[2]REMOVE A PET\n[3]EXIT")
        choice = int(input("Select: "))

        if choice == 1:
            student.add_pets()
        elif choice == 2:
            i = int(input("Which pet you wish to remove(give number): "))
            student.remove_pets(i)
        elif choice == 3:
            break
        else:
            print("Incorrect answer")


main()