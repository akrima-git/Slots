class Player:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.winnings = 0

    def __str__(self):
        return self.name + ", " +  str(self.balance)

    def add_balance(self):
        while True:
            amount = int(input("How much would you like to deposit? "))
            if amount > 0:
                self.balance += amount
                return
            else:
                print("Enter an integer value greater than 0.")
                pass

    def withdraw_winnings(self):
        self.balance += self.winnings * 0.9
        print(f"Your new balance is {self.balance}")
        self.winnings = 0

    def place_bet(self):
        while True:
            try:
                bet = int(input("How much would you like to bet? "))
                if bet < 0:
                    print("You have entered an invalid amount.")
                elif bet > self.balance:
                    print("You have insufficient funds.")
                else:
                    self.balance -= bet
                    return bet
            except:
                print("You have entered an invalid number.")

    def add_winnings(self, winnings):
        self.winnings += winnings

    def display_balance(self):
        print(f"Your balance is {self.balance}")

    def return_balance(self):
        return self.balance