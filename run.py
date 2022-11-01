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
