# File:         Ex4_3
# Author:       Niki Leppänen
# Description:  Take the cell phone class of last week and divide the cell phone class into another file
#               (name the file clearly). Leave the main function in the original file. Test, that your code still works.

from Ex4_CellPhone import CellPhone


def main():
    cell = CellPhone()

    cell.set_manufact(input("What manufacturer: "))

    cell.set_model(input("What model: "))

    cell.set_retail_price(float(input("What is the retail price: ")))

    print("\nHere is the data you provided:")

    cell.provided_data()


main()
