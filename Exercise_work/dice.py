import random

class Dice:
    def __init__(self):
        self.dice_number = 0

    def get_dice(self):
        return self.dice_number

    def roll_dice(self):
        number = random.randint(1, 6)

        if number == 1:
            self.dice_number = 1
        elif number == 2:
            self.dice_number = 2
        elif number == 3:
            self.dice_number = 3
        elif number == 4:
            self.dice_number = 4
        elif number == 5:
            self.dice_number = 5
        elif number == 6:
            self.dice_number = 6


