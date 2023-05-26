import random as r


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not self.value


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)
    SHOW_CHARS = '_X0'

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

    @staticmethod
    def __check_ind(tup):
        for v in tup:
            if type(v) != int or not 0 <= v < 3:
                raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_ind(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__check_ind(key)
        self.pole[key[0]][key[1]].value = value

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
        print('Input X coordinates:')
        i, j = int(input()), int(input())
        self.__check_ind((i, j))
        if self.pole[i][j]:
            self[i, j] = self.HUMAN_X
        else:
            self.human_go()

    def computer_go(self):
        while 1:
            i = r.randint(0, 2)
            j = r.randint(0, 2)
            if self.pole[i][j]:
                self[i, j] = self.COMPUTER_O
                break

    @property
    def is_human_win(self):
        for i in range(3):
            if self[i, 0] == self[i, 1] == self[i, 2] == self.HUMAN_X:
                return True
            if self[0, i] == self[1, i] == self[2, i] == self.HUMAN_X:
                return True
        if all([self[0, 0] == self[1, 1] == self[2, 2] == self.HUMAN_X]):
            return True
        if all([self[0, 2] == self[1, 1] == self[2, 0] == self.HUMAN_X]):
            return True
        return False

    @property
    def is_computer_win(self):
        for i in range(3):
            if self[i, 0] == self[i, 1] == self[i, 2] == self.COMPUTER_O:
                return True
            if self[0, i] == self[1, i] == self[2, i] == self.COMPUTER_O:
                return True
        if all([self[0, 0] == self[1, 1] == self[2, 2] == self.COMPUTER_O]):
            return True
        if all([self[0, 2] == self[1, 1] == self[2, 0] == self.COMPUTER_O]):
            return True
        return False

    @property
    def is_draw(self):
        return not self.is_human_win and not self.is_computer_win and not any([cell for row in self.pole for cell in row])

    def __bool__(self):
        return not self.is_human_win and not self.is_computer_win and any([cell for row in self.pole for cell in row])


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
