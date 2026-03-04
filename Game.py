import random

class Game:
    def __init__(self, deposit):
        self.deposit = deposit

    def play(self):
        won = 0
        number = random.randint(0,10)
        print(number)
        if number > 5:
            won = self.deposit*2
        self.deposit = 0
        return won
