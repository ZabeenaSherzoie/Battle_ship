"""Imports random module"""
import random


#  Keep track of the score
scores = {"computer": 0, "player": 0}
# Most of this class's code credit is going to the Code Insititute's
# Portfolio Project 3 Scope


class Board:
    """
    Main board class.  Sets board size the number of ships,
    the player's name and the board type (player board or computer)
    Has methods for adding ships and guesses and printing the board.
    """

    def __init__(self, size, num_ships, name, typee):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = typee
        self.board = [['.' for x in range(size)]for y in range(size)]
        self.guesses = []
        self.ships = []

    def print(self):
        """Prints the game board and it's row and column numbering."""
        num = 0
        print('   ', end=' ')
        for i in range(self.size):
            print(i, end=' ')
        print('\n'+'-'*(2*self.size+5))
        for row in self.board:
            print(num, '|', end=' ')
            print(' '.join(row), end=' ')
            print('| ',)
            num += 1

    def guess(self, x, y):
        """Gets the guess's coordinates and decides whether
         it is a hit or a miss."""
        self.guesses.append((x, y))
        self.board[x][y] = 'X'
        if (x, y) in self.ships:
            self.board[x][y] = '*'
            return 'Hit', (x, y)
        else:
            return "Miss", (x, y)

    def add_ship(self, x, y, board):
        """Adds randomly generated ships to player board or
        appends it coordinates to the computer boards ships list."""
        if board.type == 'computer':
            self.ships.append((x, y))
        elif board.type == 'player':
            self.board[x][y] = '#'
            self.ships.append((x, y))
# This function's code was taken from the Code Institutes's
#  Portfolio Project 3 Scope video


def random_point(size):
    """Generates a random number used for computer guesses."""
    return random.randint(0, size - 1)


def level_input_validation():
    """Validates the input recived from the user for level selection."""
    print('Select the game level you want to play:\n')
    # Takes an input from the user to set the level of the game
    print('      Easy     Medium     Hard\n')
    level = input(">").lower()
    # Validating the user input
    while (level != 'hard' and level != "easy" and level != 'medium'):
        print("Invalid input, please select from one of the provided levels")
        print('      Easy     Medium     Hard')
        level = input('>')
    return level


def size_b(level):
    """Returns the size of the board according to the game level."""
    # Decides the size of the board according to game level
    if level.lower() == "hard":
        return 8
    elif level.lower() == "medium":
        return 6
    elif level.lower() == 'easy':
        return 4


def num_ships_b(level):
    """Decides how many ships should be in the board
     according to the game level."""
    if level.lower() == 'hard':
        return 8
    elif level.lower() == 'medium':
        return 6
    elif level.lower() == "easy":
        return 4


def populate_board(board):
    """Generates two random numbers and uses the add ship function
     to add ships to the board."""
    x = random_point(board.size)
    y = random_point(board.size)
    # Regenerates two coordinates if the first generated one
    # is already have been populated
    while (x, y) in board.ships:
        x = random_point(board.size)
        y = random_point(board.size)
    board.add_ship(x, y, board)


def make_guess(board):
    """Generates two random numbers as a guess if it is computer's
     turn or will ask the user for guess."""
    if board.type == 'computer':
        # A list used for validating x and ys' data
        n = []
        for num in range(board.size):
            n.append(str(num))
        print()
        x = input("guess a row:")
        # Validates x's input data
        while x not in n:
            print(
                f"Please enter a number from 0 to {board.size -1 }")
            x = input("guess a  row:")
        y = input("guess a column: ")
        # Validates y's input data
        while y not in n:
            print(
                f"Please enter a number from 0 to {board.size -1 }")
            y = input("guess a column: ")
    elif board.type == 'player':
        x = random_point(board.size)
        y = random_point(board.size)
    coordinate = (int(x), int(y))
    return coordinate


def validate_coordinate(board, coordinates):
    """Validates the coordinates to prevent duplicate entries"""
    if coordinates in board.guesses:
        print('You have already guessed that spot')
        print('Please enter different coordinates!')
        make_guess(board)
        return coordinates
    else:
        # Passes the coordinates to the Board's guess function
        guess = board.guess(coordinates[0], coordinates[1])
        print(guess)
        # Returnes the status of the guessed coordinate
        return guess


def play_game(computer_board, player_board):
    """Prints the player and computers board and counts the scores
    Allows the user to keep the control of the game.
    """
    # Prints blank initial boardes with no guess coordinates marked
    print(f"{player_board.name.capitalize()}'s Board: ")
    player_board.print()
    print()
    print("Computer's Board: ")
    computer_board.print()
    play = 'yes'
    # Continues the game until the user wants to quit
    while play.lower() != 'n':
        p = validate_coordinate(computer_board, make_guess(computer_board))
        c = validate_coordinate(player_board, make_guess(player_board))
        print(f"{player_board.name.capitalize()}'s Board: ")
        player_board.print()
        print()
        print("Computer's Board: ")
        computer_board.print()
        print("-"*35)
        # Prints the coordinates guessed by both the computer
        # and the player
        print(f'Computer guessed:{c[1]}')
        print(f"Computer's guess was a {c[0]}")
        print(f'{player_board.name.capitalize()} guessed:{p[1]}')
        print(f"{player_board.name.capitalize()}'s guess was a {p[0]}")
        # Counts the player and the computer's scores
        if c[0] == 'Hit' and p[0] == "Hit":
            scores["computer"] += 1
            scores["player"] += 1
        elif p[0] == "Hit":
            scores['player'] += 1
        elif c[0] == "Hit":
            scores['computer'] += 1
        # prints scores after each round
        print(f"Computer's score:{scores['computer']}")
        print(f"{player_board.name.capitalize()}'s score:{scores['player']}")
        print("-"*35)
        # Checks whether one of the players have found all the
        # ships or not
        n_s = player_board.num_ships
        if scores["player"] == n_s or scores['computer'] == n_s:
            break
        else:
            print('Do you want to continue?')
            print("Press any key to continue or N to quit")
            play = input('')
    # Decides about the winner of the game
    if scores['computer'] == computer_board.num_ships:
        print("The winner is computer!!!")
        print(f"Computer's score:{scores['computer']}")
        print(f"{player_board.name.capitalize()}'s score:{scores['player']}")
    elif scores['player'] == player_board.num_ships:
        print(f"The winner is  {player_board.name.capitalize()}!!!")
        print(f"Computer's score:{scores['computer']}")
        print(f"{player_board.name.capitalize()}'s score:{scores['player']}")
    else:
        print()
        print("You Quited the game...")
        print(f"Computer's score:{scores['computer']}")
        print(f"{player_board.name.capitalize()}'s score:{scores['player']}")
        print("Click the run program if you want to start a new game!!")


# Most of this function's code credit is going
#  to the Code Insititute's Portfolio Project 3 Scope
def new_game():
    """Starts a new game, Sets the board size and number of ships, resets the
    scores and initialises the boards."""
    print("-"*35)
    # prints a welcome message
    print("Welcome to the BATTLESHIPS game!!!")
    print("-"*35)
    # Getting the player's name
    player_name = input("please enter your name:\n")
    print("-"*35)
    # Calling the level validation function
    valid_level = level_input_validation().capitalize()
    b_size = size_b(valid_level)
    num_ship = num_ships_b(valid_level)
    print("-"*47)
    print(
        f"Level:{valid_level}, {b_size}X{b_size} , Num of ships:{num_ship} ")
    print("-"*47)
    scores["computer"] = 0
    scores['player'] = 0
    # Creating to instances of the Board class
    computer_board = Board(b_size, num_ship, "Computer", typee="computer")
    player_board = Board(b_size, num_ship, player_name, typee="player")
    # Populating the board with the ships in range of number
    # of the ships
    for _ in range(num_ship):
        populate_board(player_board)
        populate_board(computer_board)
    play_game(computer_board, player_board)


new_game()
