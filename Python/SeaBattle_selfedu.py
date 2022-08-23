import math
import random
from typing import List


class Queue:
    def __init__(self):
        self.__queue = []

    def add(self, element):
        self.__queue.insert(0, element)

    def pop(self):
        if not self.isEmpty():
            return self.__queue.pop()

    def isEmpty(self):
        return not bool(self.__queue)


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


class GameOptions:
    ONE_DECKS = 4
    TWO_DECKS = 3
    THREE_DECKS = 2
    FOUR_DECKS = 1
    COLLIDE_DIST = 1.99

    @property
    def HORIZONTAL(self):
        return 1

    @property
    def VERTICAL(self):
        return 2


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

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == GameOptions.HORIZONTAL:
                self._x += go
            else:
                self._y += go

    def is_collide(self, ship):
        ship1_coord = list(self.get_start_coords())
        cell_ship1 = ship1_coord.copy()
        for counter_ship1 in range(self.length):
            if self.orientation == GameOptions.HORIZONTAL:
                cell_ship1[0] = ship1_coord[0] + counter_ship1
            else:
                cell_ship1[1] = ship1_coord[1] + counter_ship1

            ship2_coord = list(ship.get_start_coords())
            cell_ship2 = ship2_coord.copy()
            for counter_ship2 in range(ship.length):
                if ship.orientation == GameOptions.HORIZONTAL:
                    cell_ship2[0] = ship2_coord[0] + counter_ship2
                else:
                    cell_ship2[1] = ship2_coord[1] + counter_ship2

                dist = distance(cell_ship1, cell_ship2)
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

    def __getitem__(self, index):
        return self._cells[index]

    def __setitem__(self, key, value):
        if value in (0, 1):
            try:
                self._cells[key] = value
            except IndexError as e:
                print('Wrong index for ship cells!' + str(e))


class ShipsMover:
    def __init__(self, size, ships):
        self.size = size
        self.ships = ships

    def is_collision(self, ship):
        collision = False
        for other_ship in self.ships:
            if id(ship) != id(other_ship):
                collision = ship.is_collide(other_ship)
        return collision

    def __call__(self, step=1):
        move_queue = Queue()
        for ship in self.ships:
            move_queue.add(ship)

        while move_queue:
            count = 0
            ship = move_queue.pop()
            ship.move(step)
            if self.is_collision(ship) or ship.is_out_pole(self.size):
                ship.move(-step)
                move_queue.add(ship)
                count += 1
            else:
                count = 0
            
            if count == len(self.ships):
                break


class GamePole:
    __slots__ = ('_size', '_ships', '__allowed_cells', 'ships_mover')

    def __init__(self, size):
        self._size = size
        self._ships: List[Ship] = []
        self.__allowed_cells = [[0 for _ in range(size)] for _ in range(size)]
        self.ships_mover = ShipsMover(size, self._ships)

    def place_ship(self, ship):
        pass

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

    def move_ships(self):
        self.ships_mover()


if __name__ == "__main__":
    ship4 = Ship(4, GameOptions.HORIZONTAL, 0, 0)
    ship3 = Ship(3, GameOptions.VERTICAL, 0, 2)
    ship2 = Ship(2, GameOptions.HORIZONTAL, 8, 9)
    print(ship4.is_collide(ship3))
    print(ship3.is_collide(ship4))
    print(ship2.is_out_pole(10))

