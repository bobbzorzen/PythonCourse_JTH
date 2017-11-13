import five_in_a_row as five

# This dictonary contains the entire state of the game.
game = {
    'width': 10,
    'height': 10,
    'moves': [
        {'x': 0, 'y': 0, 'player': 'X'},
        {'x': 1, 'y': 1, 'player': 'O'},
        {'x': 2, 'y': 2, 'player': 'X'},
        {'x': 3, 'y': 3, 'player': 'O'},
        {'x': 4, 'y': 4, 'player': 'X'},
        {'x': 5, 'y': 5, 'player': 'O'},
        {'x': 6, 'y': 6, 'player': 'X'},
        {'x': 7, 'y': 7, 'player': 'O'},
        {'x': 8, 'y': 8, 'player': 'X'},
        {'x': 9, 'y': 9, 'player': 'O'}
    ]
}

while five.get_winner(game) == ' ':

    # Print the game board.
    five.print_game(game)

    # Ask the user to enter coordinates.
    next_player = five.get_next_players_turn(game)

    print("Enter the x and y coordinate for the cell to place "+next_player+" in.")
    print("Separate the coordinates by space, e.g: 3 5")

    are_entered_coordinates_ok = False

    while not are_entered_coordinates_ok:

        coordinates_string = input()
        coordinates = coordinates_string.split(" ")

        x = int(coordinates[0])
        y = int(coordinates[1])

        if not five.does_cell_exist(game, x, y):
            print("No cell with the coordinates x="+str(x)+" y="+str(y)+" exists, try again!")
        elif not five.is_cell_free(game, x, y):
            print("The cell with the coordinates x="+str(x)+" y="+str(y)+" is not free, try again!")
        else:
            are_entered_coordinates_ok = True

    five.make_move(game, x, y, next_player)

five.print_game(game)
print("The game is over, and the winner is: "+five.get_winner(game)+"!")