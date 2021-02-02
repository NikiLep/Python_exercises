# File:         Ex4_3
# Author:       Niki Leppänen
# Description:  Add and ID data attribute (integer between 1-6) to the cell phone.Cell phone class shall have accessor
#               and mutator methods for all data attributes. Also check the __str__ method is up to date.

class CellPhone:

    def __init__(self):
        self.__manufact = 'manufacturer'
        self.__model = 'model'
        self.__retailPrice = 0
        self.id = 1

    def set_manufact(self, manufacturer):
        self.__manufact = manufacturer

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail_price):
        self.__retailPrice = retail_price

    def set_id(self, id_number):
        self.id = id_number

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retailPrice

    def get_id(self):
        return self.id

    def provided_data(self):
        print("Manufacturer: ", self.get_manufact())
        print("Model number: ", self.get_model())
        print("Retail price: ", self.get_retail_price())

    def __str__(self):
        return f"""Id: {self.id}\nManufacturer: {self.__manufact}
Model: {self.__model}\nRetail price: {self.__retailPrice}"""


def main():
    cell = CellPhone()

    cell.set_id(input("Give id: "))

    cell.set_manufact(input("What manufacturer: "))

    cell.set_model(input("What model: "))

    cell.set_retail_price(float(input("What is the retail price: ")))

    print("\nHere is the data you provided:")

    print(cell)


main()

