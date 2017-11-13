def print_game(game):
    # Prints the game to the console.

    print(" y")

    y = game['height'] - 1
    while 0 <= y:

        print(str(y)+"|", end="")

        for x in range(game['width']):
            print(get_cell_value(game, x, y), end="")
        print()

        y -= 1

    print("-+", end="")
    for x in range(game['width']):
        print("-", end="")
    print("x")
    print(" |", end="")
    for x in range(game['width']):
        print(x, end="")
    print(" ")

def get_cell_value(game, x, y):
    # Returns 'X' if a cross has been placed in the cell with the given coordinates.
    # Returns 'O' if a circle has been placed in the cell with the given coordinates.
    # Returns ' ' otherwise.
    cellValue = ' '
    for move in game['moves']:
        if move['x'] == x and move['y'] == y:
            cellValue = move['player']
    
    return cellValue

def make_move(game, x, y, player):
    # Adds a new move to the game with the information in the parameters.
    if does_cell_exist(game, x, y) and is_cell_free(game, x, y):
        move = {
            'x': x,
            'y': y,
            'player': player
        }
        game['moves'].append(move)

def does_cell_exist(game, x, y):
    # Returns True if the game contains a cell with the given coordinates.
    # Returns False otherwise.
    return (x < game['width'] and y < game['height'])

def is_cell_free(game, x, y):
    # Returns True if the cell at the given coordinates doesn't contain a cross or a circle.
    # Returns False otherwise.
    return (get_cell_value(game, x, y) == ' ')

def get_next_players_turn(game):
    # Returns 'X' if a cross should be placed on the board next.
    # Returns 'O' if a circle should be placed on the board next.
    previousPlayer = game['moves'][-1]['player'] if len(game['moves']) > 0 else 'O'
    return 'X' if previousPlayer == 'O' else 'O'

def find_diagonal_match(matrix, y, x, searchLeft=False):
    negator = -1 if searchLeft else 1
    match = True
    if len(matrix) < y+5 or (len(matrix[y]) < x+5 and x-5 > 0):
        match = False
    for i in range(1, 5):
        if not match:
            break
        newX = x + (negator*i)
        match = matrix[y+i][newX] == matrix[y][x]
    return match

def get_winner(game):
    # Returns 'X' if 5 crosses in a row is found in the game.
    # Returns 'O' if 5 circles in a row is found in the game.
    # Returns ' ' otherwise.
    
    return ' '