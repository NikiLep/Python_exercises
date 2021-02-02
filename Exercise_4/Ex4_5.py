# File:         Ex4_5
# Author:       Niki Leppänen
# Description:  Create different cell phone objects (which have different data attribute values,
#               use mutator methods to change the data attribute values).
#               Print out each object’s state (use the __str__ method in the cell phone class).


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
    cell1 = CellPhone()
    cell2 = CellPhone()

    cell1.set_id(input("Give id: "))
    cell1.set_manufact(input("What manufacturer: "))
    cell1.set_model(input("What model: "))
    cell1.set_retail_price(float(input("What is the retail price: ")))

    cell2.set_id(input("Give id: "))
    cell2.set_manufact(input("What manufacturer: "))
    cell2.set_model(input("What model: "))
    cell2.set_retail_price(float(input("What is the retail price: ")))

    print("\nHere is the data you provided:")

    print(cell1)
    print(cell2)


main()