import random
from typing import List
from utils import Queue, distance


class GameOptions:
    ONE_DECKS = 4
    TWO_DECKS = 3
    THREE_DECKS = 2
    FOUR_DECKS = 1
    COLLIDE_DIST = 1.99

    HORIZONTAL = 1
    VERTICAL = 2


class Ship:
    __slots__ = ('_length', '_x', '_y', '_tp', '_is_move', '_cells')

    def __init__(self, length, tp=GameOptions.HORIZONTAL, x=None, y=None):
        self._length = length
        self._x = x
        self._y = y
        self._tp = tp
        self._is_move = True
        self._cells = [1 for _ in range(length)]

    @property
    def length(self):
        return self._length

    @property
    def orientation(self):
        return self._tp

    @orientation.setter
    def orientation(self, value):
        if value in (GameOptions.HORIZONTAL, GameOptions.VERTICAL):
            self._tp = value

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def isPlaced(self):
        return not None in self.get_start_coords()

    def move(self, go):
        if self._is_move:
            if self._tp == GameOptions.HORIZONTAL:
                self._x += go
            else:
                self._y += go

    def is_collide(self, ship):
        if self.isPlaced() and ship.isPlaced():
            for cell_first_ship in self.get_all_cells_of_ship():
                for cell_second_ship in ship.get_all_cells_of_ship():
                    dist = distance(cell_first_ship, cell_second_ship)
                    if dist < GameOptions.COLLIDE_DIST:
                        return True
        return False

    def is_out_pole(self, size):
        ship_coords = list(self.get_start_coords())
        cell_coords = ship_coords.copy()
        for cell_counter in range(self.length):
            if self.orientation == GameOptions.HORIZONTAL:
                cell_coords[0] = ship_coords[0] + cell_counter
            else:
                cell_coords[1] = ship_coords[1] + cell_counter

            if any([cell_coords[0] < 0,
                    cell_coords[0] >= size,
                    cell_coords[1] < 0,
                    cell_coords[1] >= size,
                    ]):
                return True

        return False

    def get_all_cells_of_ship(self):
        start_x, start_y = self.get_start_coords()
        out = []
        for i in range(self.length):
            if self.orientation == GameOptions.HORIZONTAL:
                out.append((start_x + i, start_y))
            else:
                out.append((start_x, start_y + i))
        return out

    def get_cell_neighboors(self, cell, size):
        neighboors = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                x = cell[0] + dx
                y = cell[1] + dy
                if  0 <= x < size and 0 <= y < size:
                    neighboors.append((x, y))

        return neighboors

    def get_restricted_ship_area(self, size):
        restricted_cells = set()
        for cell in self.get_all_cells_of_ship():
            neighboors = self.get_cell_neighboors(cell, size)
            restricted_cells.update(neighboors)
        return restricted_cells

    def __getitem__(self, index):
        return self._cells[index]

    def __setitem__(self, key, value):
        if value in (1, 2):
            try:
                self._cells[key] = value
            except IndexError as e:
                print('Wrong index for ship cells!' + str(e))

    def __repr__(self):
        return f'Ship with {self.length} decks'

    def __str__(self):
        return f'Ship with {self.length} decks, coords: x = {self._x}, y = {self._y}'


class ShipsMover:
    def __init__(self, size, ships, parent):
        self.size = size
        self._ships = ships
        self.__parent = parent

    def __call__(self, step=1):
        move_queue = Queue()
        for ship in self._ships:
            move_queue.add(ship)

        count = 0
        while move_queue:
            ship = move_queue.pop()
            ship.move(step)
            if self.__parent.is_collision(ship) or ship.is_out_pole(self.size):
                ship.move(-step)
                move_queue.add(ship)
                count += 1
            else:
                count = 0

            if count == len(move_queue):
                break


class ShipConstellator:
    def __init__(self, size, ships, parent):
        self.size = size
        self.__ships = ships
        self.allowed_cells = list(range(size*size))
        self.__parent = parent

    def place_ships(self):
        for ship in self.__ships:
            local_allowed_cells = self.allowed_cells.copy()
            while local_allowed_cells:
                position_absolute = random.choice(local_allowed_cells)
                x, y = CoordConverter.absolute_to_matrix(position_absolute, self.size)
                ship.set_start_coords(x, y)
                if self.__parent.is_collision(ship) or ship.is_out_pole(self.size):
                    local_allowed_cells.remove(position_absolute)
                else:
                    break

            restricted_area = ship.get_restricted_ship_area(self.size)
            for cell in restricted_area:
                abs_cell = CoordConverter.matrix_to_absolute(cell[0], cell[1], self.size)
                if abs_cell in self.allowed_cells:
                    self.allowed_cells.remove(abs_cell)


class CoordConverter:
    @staticmethod
    def absolute_to_matrix(abs_coord, size):
        y = abs_coord//size
        x = abs_coord - y*size
        return x, y

    @staticmethod
    def matrix_to_absolute(x, y, size):
        return y*size + x


class GamePole:
    __slots__ = ('_size', '_ships', '__allowed_cells', '__pole', 'ships_mover', 'ships_constelattor')

    def __init__(self, size):
        self._size = size
        self._ships: List[Ship] = []
        self.__pole = [[0 for _ in range(size)] for _ in range(size)]
        self.ships_mover = ShipsMover(size, self._ships, self)
        self.ships_constelattor = ShipConstellator(size, self._ships, self)

    def is_collision(self, ship):
        collision = False
        for other_ship in self._ships:
            if id(ship) != id(other_ship):
                collision = ship.is_collide(other_ship)
                if collision:
                    break
        return collision

    def init(self):
        ships = [
            [Ship(1) for i in range(GameOptions.ONE_DECKS)],
            [Ship(2) for i in range(GameOptions.TWO_DECKS)],
            [Ship(3) for i in range(GameOptions.THREE_DECKS)],
            [Ship(4) for i in range(GameOptions.FOUR_DECKS)],
        ]
        for ship_type in ships:
            self._ships.extend(ship_type)
        # Implement ships placing
        # hardcode
        # temporary
        # ONE DECK

        self.ships_constelattor.place_ships()
        self.update_pole()

    def move_ships(self):
        self.ships_mover()
        self.update_pole()

    def update_pole(self):
        self.__pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            ship_cells_coords = ship.get_all_cells_of_ship()
            for x, y in ship_cells_coords:
                self.__pole[y][x] = 1

    def show(self):
        print('-'*15, ' Pole ', '-'*15, sep='')
        for row in self.__pole:
            print(*row)

    def get_pole(self):
        return tuple(map(tuple, self.__pole))

    def get_ships(self):
        return self._ships


if __name__ == "__main__":
    gp = GamePole(10)
    gp.init()
    gp.show()
    gp.move_ships()
    gp.show()
