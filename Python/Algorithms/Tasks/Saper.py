import random

class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

    def __repr__(self):
        return f"{self.around_mines}:{self.mine}"


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell(0, False) for _ in range(N)] for _ in range(N)]
        self.init()

    def neighboor_cells_add_one(self, base_raw, base_column):
        for raw_offset in range(-1, 2):
            current_raw = base_raw + raw_offset
            if 0 <= current_raw < self.N:
                for column_offset in range(-1, 2):
                    current_column = base_column + column_offset
                    if 0 <= current_column < self.N:
                        self.pole[current_raw][current_column].around_mines += 1


    def init(self):
        rand_cells = random.sample(range(self.N * self.N), self.M)
        for rand_cell in rand_cells:
            raw = rand_cell//self.N
            column = rand_cell%self.N
            self.pole[raw][column].mine = True
            self.neighboor_cells_add_one(raw, column)

    def show(self):
        for raw in self.pole:
            for cell in raw:
                if cell.mine:
                    print('*', end='')
                else:
                    print(cell.around_mines, end='') if cell.fl_open else print('#', end='')
            print()


pole_game = GamePole(10, 12)
