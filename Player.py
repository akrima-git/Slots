class Player:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.winnings = 0

    def __str__(self):
        return self.name + ", " +  str(self.balance)

    def add_balance(self, amount):
        self.balance += amount

    def withdraw_winnings(self):
        self.balance += self.winnings * 0.9

if __name__ == "__main__":

    player1 = Player("Akrima", 120)

    print(player1)