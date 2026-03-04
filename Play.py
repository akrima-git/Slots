import Player as p
import Game as g


def play_game(player):
    entry = player.place_bet()
    game = g.Game(entry)
    player.winnings = game.play()

    return player.winnings

def main():

    name = input("What is your name? ")
    player1 = p.Player(name)
    player1.add_balance()
    again = True
    while again:


        player1.winnings += play_game(player1)
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
        again = player1.play_again()
        if player1.balance == 0:
            print("you are out of funds.")
            break

    print(f"{player1.name} ended with ${str(player1.balance)}.")

main()








