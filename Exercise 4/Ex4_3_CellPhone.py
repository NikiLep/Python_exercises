# File:         Ex4_3
# Author:       Niki Leppänen
# Description:  Take the cell phone class of last week and divide the cell phone class into another file
#               (name the file clearly). Leave the main function in the original file. Test, that your code still works.

class CellPhone:

    def __init__(self):
        self.__manufact = 'manufacturer'
        self.__model = 'model'
        self.__retailPrice = 0

    def set_manufact(self, manufacturer):
        self.__manufact = manufacturer

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail_price):
        self.__retailPrice = retail_price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retailPrice

    def provided_data(self):
        print("Manufacturer: ", self.get_manufact())
        print("Model number: ", self.get_model())
        print("Retail price: ", self.get_retail_price())