class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not self.value


class TicTacToe:
    FREE_CELL = 0  # Represents a free cell on the board
    HUMAN_X = 1  # Represents the symbol for the human player (cross)
    COMPUTER_O = 2  # Represents the symbol for the computer player (zero)
    SHOW_CHARS = '_X0'  # Characters used to display the board

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]  # Create a 3x3 board using Cell objects

    def __getitem__(self, item):
        self.__check_ind(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__check_ind(key)
        self.pole[key[0]][key[1]].value = value

    @staticmethod
    def __check_ind(tup):
        for v in tup:
            if type(v) != int or not 0 <= v < 3:
                raise IndexError('Indices are out of game pole size')

    def init(self):
        # Initialize the board by setting all cell values to the FREE_CELL value
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL

    def show(self):
        # Display the current state of the board
        for row in self.pole:
            for cell in row:
                print(self.SHOW_CHARS[cell.value], end=' ')
            print()
        print()

    def reset(self):
        # Reset the game by calling the init method to clear the board
        self.init()  # Call the init method to reset the game state

    def computer_go(self):
        # Implement the computer player's move using the minimax algorithm to find the best move
        best_score = float('-inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.pole[i][j]:
                    self[i, j] = self.COMPUTER_O
                    score = self.minimax(self.pole, 0, False)
                    self[i, j] = self.FREE_CELL

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            self[best_move] = self.COMPUTER_O

    def minimax(self, state, depth, is_maximizing):
        # Implement the minimax algorithm to determine the best move for the computer player
        if self.is_human_win:
            return -1
        elif self.is_computer_win:
            return 1
        elif self.is_draw:
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j].value == self.FREE_CELL:
                        state[i][j].value = self.COMPUTER_O
                        score = self.minimax(state, depth + 1, False)
                        state[i][j].value = self.FREE_CELL
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j].value == self.FREE_CELL:
                        state[i][j].value = self.HUMAN_X
                        score = self.minimax(state, depth + 1, True)
                        state[i][j].value = self.FREE_CELL
                        best_score = min(score, best_score)
            return best_score

    def _is_win(self, cell_value):
        """check is there a row, column or diagonal in a pole with a specified value"""
        for i in range(3):
            if self[i, 0] == self[i, 1] == self[i, 2] == cell_value:
                return True
            if self[0, i] == self[1, i] == self[2, i] == cell_value:
                return True
        if all([self[0, 0] == self[1, 1] == self[2, 2] == cell_value]):
            return True
        if all([self[0, 2] == self[1, 1] == self[2, 0] == cell_value]):
            return True
        return False

    @property
    def is_human_win(self):
        # Check if a player has won the game
        return self._is_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        # Check if the computer player has won
        return self._is_win(self.COMPUTER_O)

    @property
    def is_draw(self):
        # Check if the game is a draw
        return not self.is_human_win and not self.is_computer_win and not any(
            [cell for row in self.pole for cell in row])

    def __bool__(self):
        # Check if the game is over
        return not self.is_human_win and not self.is_computer_win and any([cell for row in self.pole for cell in row])

    def get_winning_cells(self, cell_value):
        # Retrieve the coordinates of the winning cells for a given player
        winning_cells = []
        for i in range(3):
            if self[i, 0] == self[i, 1] == self[i, 2] == cell_value:
                winning_cells.append((i, 0))
                winning_cells.append((i, 1))
                winning_cells.append((i, 2))
            if self[0, i] == self[1, i] == self[2, i] == cell_value:
                winning_cells.append((0, i))
                winning_cells.append((1, i))
                winning_cells.append((2, i))
        if all([self[0, 0] == self[1, 1] == self[2, 2] == cell_value]):
            winning_cells.append((0, 0))
            winning_cells.append((1, 1))
            winning_cells.append((2, 2))
        if all([self[0, 2] == self[1, 1] == self[2, 0] == cell_value]):
            winning_cells.append((0, 2))
            winning_cells.append((1, 1))
            winning_cells.append((2, 0))
        return winning_cells


game = TicTacToe()
game.init()
step_game = 0
