from lab_06_connect_four import ConnectFour
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

nr_of_moves = 0
game = ConnectFour(7)
winner = game.get_winner()
while winner == " ":
    cls()
    game.print_game()
    column = int(input("enter a column: "))
    game.make_move(column)
    winner = game.get_winner()
    if winner != " ":
        print("Winner winner, chicken dinner: ", winner)