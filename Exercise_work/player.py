class Player:
    def __init__(self):
        self.__money = 100

    def set_money(self, money):
        self.__money = money

    def get_money(self):
        return self.__money

    def __str__(self):
        return f"""Money: {self.__money}"""
