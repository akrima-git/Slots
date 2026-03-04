import Player as p
import Game as g


def take_name():
    name = input("What is your name? ")
    return name

def create_player(name):
    player = p.Player(name)
    player.add_balance()
    return player

def play_game(player):
    entry = player.place_bet()
    game = g.Game(entry)
    player.winnings = game.play()

    return player.winnings

def ask_to_withdraw(player):
    if player.winnings > 0:
        print(f"You have {player.winnings} in winnings")
        while True:
            withdraw_money = input("Would you like to withdraw your winnings? (Y/N)")
            if withdraw_money.upper() == "Y":
                player.withdraw_winnings()
                break
            elif withdraw_money.upper() == "N":
                break
            else:
                continue

def play_again(player):
    if player.winnings == 0:
        again = input("Would you like to play again? (Y/N)")
        while True:
            if again.upper() == "Y":
                return True
            elif again.upper() == "N":
                return False
    return True

def main():

    name = take_name()
    player1 = create_player(name)
    again = True
    while again:

        player1.winnings += play_game(player1)

        player1.display_balance()

        ask_to_withdraw(player1)

        again = play_again(player1)

        if player1.return_balance() == 0:
            print("You are out of funds.")
            break

    print(f"{player1.name} ended with ${str(player1.balance)}.")

main()








