

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show_card(self):
        return "{} of {}".format(self.value, self.suit)

    def get_value(self):
        return self.value

