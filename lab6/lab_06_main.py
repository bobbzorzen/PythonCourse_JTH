from lab_06_connect_four import ConnectFour
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

game = ConnectFour(7)
winner = game.get_winner()
while winner == " ":
    cls()
    game.print_game()
    column = int(input("enter a column: "))
    game.make_move(column)
    winner = game.get_winner()
    if winner != " ":
        cls()
        game.print_game()
        print("Winner winner, chicken dinner: ", winner)