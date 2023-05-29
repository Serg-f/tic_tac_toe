class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not self.value


class TicTacToe:
    FREE_CELL = 0  # free cell
    HUMAN_X = 1  # cross (player - human)
    COMPUTER_O = 2  # zero (player - computer)
    SHOW_CHARS = '_X0'

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

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
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL

    def show(self):
        for row in self.pole:
            for cell in row:
                print(self.SHOW_CHARS[cell.value], end=' ')
            print()
        print()

    def human_go(self):
        print('Input X coordinates (horizontal, vertical), each on a separated row:')
        i, j = int(input()), int(input())
        self.__check_ind((i, j))
        if self.pole[i][j]:
            self[i, j] = self.HUMAN_X
        else:
            raise IndexError('The cell is not empty')

    def computer_go(self):
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
        return self._is_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self._is_win(self.COMPUTER_O)

    @property
    def is_draw(self):
        return not self.is_human_win and not self.is_computer_win and not any(
            [cell for row in self.pole for cell in row])

    def __bool__(self):
        return not self.is_human_win and not self.is_computer_win and any([cell for row in self.pole for cell in row])


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        try:
            game.human_go()
        except (ValueError, IndexError) as ex:
            if ex.__class__ == ValueError:
                ex.args = 'Invalid value, input an integer',
            print(f'{ex.__class__.__name__}: {ex}')
            continue
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Congratulations! You won!")
elif game.is_computer_win:
    print("You lost :(")
else:
    print("Draw.")