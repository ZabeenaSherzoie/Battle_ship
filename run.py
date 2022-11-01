import random
# Most of this class's code credit is going to the Code Insititute's
# Portfolio Project 3 Scope
class Board:
    """
    Main board class.  Sets board size the number of ships,
    the player's name and the board type (player board or computer)
    Has methods for adding ships and guesses and printing the board.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = type
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
            return 'Hit', (x,y)
        else:
            return "Miss",(x,y)

    def add_ship(self, x, y, type):
        """Adds randomly generated ships to player board or
        appends it coordinates to the computer boards ships list."""
        if type == 'computer':
            self.ships.append((x, y))
        elif self.type == 'player':
            self.board[x][y] = '@'
            self.ships.append((x, y))
# This function's code was taken from the Code Institutes's
#  Portfolio Project 3 Scope video
def random_point(size):
    """Generates a random number used for computer guesses."""
    return random.randint(0, size - 1)

def level_input_validation():
    """Validates the input recived from the user for level selection."""
    print('Select the game level you want to play:\n')
    #Takes an input from the user to set the level of the game
    print('      Easy     Medium     Hard\n')
    level = input(">")
    #Validating the user input
    while level.lower() != 'hard' and level.lower() != "easy" and level.lower() != 'medium':
        print("Invalid input, please select from one of the provided levels")
        print('      Easy     Medium     Hard')
        level = input('>')
    return level
def size(level):
    """Returns the size of the board according to the game level."""
    #Decides the size of the board according to game level
    if level.lower() == "hard":
        return 8
    elif level.lower() == "medium":
        return 6
    elif level.lower() == 'easy':
        return 4
