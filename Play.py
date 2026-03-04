import Player as p
import Game as g


def playGame(player):
    while True:
        try:
            entry = int(input("How much money would you like to bet? "))
            break
        except:
            print("Invalid number entered. Please enter a whole number.")
    player.balance -= entry
    game = g.Game(entry)
    player.winnings = game.play()

    return player.winnings

def play():
    again = input("Would you like to play again? (Y/N)")
    while True:
        if again.upper() == "Y":
            return True
        elif again.upper() == "N":
            return False

def main():

    name = input("What is your name? ")
    while True:
        try:
            balance = int(input("How much money would you like to deposit? "))
            break
        except:
            print("Invalid number entered. Please enter a whole number.")
    player1 = p.Player(name, balance)
    again = True
    while again:


        player1.winnings += playGame(player1)
        print("Your current balance is: " + str(player1.balance))

        if player1.winnings > 0:
            print(f"You have {player1.winnings} in winnings")
            while True:
                withdraw_money = input("Would you like to withdraw your winnings? (Y/N)")
                if withdraw_money.upper() == "Y":
                    player1.withdraw_winnings()
                    break
                elif withdraw_money.upper() == "N":
                    break
                else:
                    continue
        again = play()

    print(player1.name, "ended with", str(player1.balance))

main()








