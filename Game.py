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


if __name__ == "__main__":
    import Player as p

    player1 = p.Player("Akrima",50)

    Game1 = Game(30)
    player1.balance -= Game1.deposit
    player1.winnings = Game1.play()
    player1.withdraw_winnings()
    print(player1.balance)
