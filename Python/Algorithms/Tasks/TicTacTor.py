import random
import itertools


class Cell:
    VALUES = {
        'FREE_CELL': 0,
        'HUMAN_X': 1,
        'COMPUTER_O': 2,
    }

    def __init__(self):
        self.value = Cell.VALUES['FREE_CELL']

    def __bool__(self):
        return not self.value


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2
    CHARS = {
        0: ' ',
        1: 'X',
        2: 'O',
    }

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.is_computer_win = False
        self.is_human_win = False
        self.is_draw = False
        self.user_steps = []
        self.computer_steps = []

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = Cell.VALUES['FREE_CELL']
        self.user_steps = []
        self.computer_steps = []
        self.is_draw = self.is_human_win = self.is_computer_win = False


    def human_go(self):
        while True:
            x, y = input('Type cell coordinates: ').split()
            x = int(x)
            y = int(y)
            chosen_cell = self.pole[x][y]
            if chosen_cell:
                self[x, y] = Cell.VALUES['HUMAN_X']
                self.user_steps.append((x, y))
                #chosen_cell.value = Cell.VALUES['HUMAN_X']
                break
            else:
                print('Cell is not empty! Type other coordinates...')
        self.show()

    def computer_go(self):
        print('Computer thinking...')
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            chosen_cell = self.pole[x][y]
            if chosen_cell:
                self[int(x), int(y)] = Cell.VALUES['COMPUTER_O']
                self.computer_steps.append((x, y))
                #chosen_cell.value = Cell.VALUES['COMPUTER_O']
                break
        self.show()

    @staticmethod
    def incline(point1, point2):
        return (point1[1]-point2[1])/(point1[0]-point2[0])

    def find_trio(self, points_list):
        if len(points_list) < 3:
            return False
        for trio in itertools.combinations(points_list, 3):
            if any([trio[0][0] == trio[1][0] == trio[2][0],
                    trio[0][1] == trio[1][1] == trio[2][1],
                    min(trio) == (0, 0) and max(trio) == (2, 2) and (1, 1) in trio,
                    min(trio) == (0, 2) and max(trio) == (2, 0) and (1, 1) in trio,
                    ]):
                return True
        return False

    def referee(self):
        if self.find_trio(self.user_steps):
            self.is_human_win = True
        elif self.find_trio(self.computer_steps):
            self.is_computer_win = True
        else:
            if len(self.user_steps) + len(self.computer_steps) == 9:
                self.is_draw = True

    def show(self):
        print(
            f"""
{self.CHARS[self.pole[0][0].value]}  |  {self.CHARS[self.pole[0][1].value]}  |  {self.CHARS[self.pole[0][2].value]}
---|-----|----
{self.CHARS[self.pole[1][0].value]}  |  {self.CHARS[self.pole[1][1].value]}  |  {self.CHARS[self.pole[1][2].value]}
---|-----|----
{self.CHARS[self.pole[2][0].value]}  |  {self.CHARS[self.pole[2][1].value]}  |  {self.CHARS[self.pole[2][2].value]}
            """
        )

    @staticmethod
    def check_indexes(row, col):
        if all([
            row in range(3) and col in range(3),
            isinstance(row, int),
            isinstance(col, int),
        ]): return True
        else:
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, coord):
        row, col = coord
        if TicTacToe.check_indexes(row, col):
            return self.pole[row][col].value

    def __setitem__(self, coord, value):
        row, col = coord
        if TicTacToe.check_indexes(row, col):
            self.pole[row][col].value = value
        self.referee()

    def __bool__(self):
        return not any([self.is_draw, self.is_human_win, self.is_computer_win])


if __name__ == "__main__":
    game = TicTacToe()
    game.init()

    test = [[1, 1, 1],
            [2, 1, 2],
            [2, 1, 2]]

    for i in range(3):
        for j in range(3):
            game[i, j] = test[i][j]

    game.show()

    if game.is_human_win:
        print("Поздравляем! Вы победили!")
    elif game.is_computer_win:
        print("Все получится, со временем")
    else:
        print("Ничья.")
