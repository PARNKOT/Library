import random
from typing import List, Set
from utils import Queue, Point, CoordConverter
from ship import (
        Ship,
        OneDeckShip,
        TwoDeckShip,
        ThreeDeckShip,
        FourDeckShip,
        GameOptions
    )


class GamePole:
    __slots__ = ('_size', '_ships', '__allowed_cells', '__pole', 'ships_mover', 'ships_constelattor')

    def __init__(self, size):
        self._size = size
        self._ships: List[Ship] = []
        self.__pole = [[0 for _ in range(size)] for _ in range(size)]
        self.ships_mover = ShipsMover(self)

    def init(self):
        self._ships.clear()
        ships = [
            [OneDeckShip() for _ in range(GameOptions.ONE_DECKS)],
            [TwoDeckShip() for _ in range(GameOptions.TWO_DECKS)],
            [ThreeDeckShip() for _ in range(GameOptions.THREE_DECKS)],
            [FourDeckShip() for _ in range(GameOptions.FOUR_DECKS)],
        ]
        for ship_type in ships:
            self._ships.extend(ship_type)

        ShipConstellator(self).place_ships()
        self.update_pole()

    def move_ships(self):
        self.ships_mover.move_all_ships()
        self.update_pole()

    def update_pole(self):
        self.__pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            ship_cells_coords = ship.get_all_cells_of_ship()
            for point in ship_cells_coords:
                self.__pole[point.y][point.x] = 1

    def show(self):
        print('-'*15, ' Pole ', '-'*15, sep='')
        for row in self.__pole:
            for el in row:
                if el == 0:
                    print('- ', end='')
                else:
                    print('* ', end='')
            print()

    def get_ships(self):
        return self._ships

    def is_collision(self, ship):
        collision = False
        for other_ship in self._ships:
            if id(ship) != id(other_ship):
                collision = ship.is_collide(other_ship)
                if collision:
                    break
        return collision

    def get_cell_neighbours(self, point: Point) -> List[Point]:
        neighbours = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                x = point.x + dx
                y = point.y + dy
                if 0 <= x < self._size and 0 <= y < self._size:
                    neighbours.append(Point(x, y))
        return neighbours

    def get_restricted_ship_area(self, ship) -> Set[Point]:
        restricted_cells = set()
        for point in ship.get_all_cells_of_ship():
            neighbours = self.get_cell_neighbours(point)
            restricted_cells.update(neighbours)
        return restricted_cells

    def find_hitted_point(self, ship, point: Point) -> Point:
        for cell in ship.get_all_cells_of_ship():
            if point == cell:
                return cell

    def is_ship_on_point(self, point: Point):
        for ship in self._ships:
            if point in ship.get_all_cells_of_ship():
                return True
        return False

    def hit(self, point: Point):
        for ship in self._ships:
            hitted_point = self.find_hitted_point(ship, point)
            if hitted_point:
                hitted_point.isHitted = True
                ship._is_move = False
                break
        print(f'Hit on {point}')


class GamePoleOwner:
    def __init__(self, gamepole: GamePole):
        self.gamepole = gamepole

    @property
    def ships(self):
        return self.gamepole._ships

    @property
    def size(self):
        return self.gamepole._size


class ShipsMover(GamePoleOwner):
    def __init__(self, gamepole: GamePole):
        super().__init__(gamepole)

    def move_all_ships(self, step=1):
        self(step)

    def move_forward(self, ship, step):
        ship.move(step)
        if self.gamepole.is_collision(ship) or ship.is_out_pole(self.size):
            ship.move(-step)
            return False
        return True

    def move_backward(self, ship, step):
        return self.move_forward(ship, -step)

    def __call__(self, step=1):
        move_queue = Queue(self.ships)

        count = 0
        while move_queue:
            ship_to_move = move_queue.pop()
            if self.move_forward(ship_to_move, step):
                count = 0
            else:
                if self.move_backward(ship_to_move, step):
                    count = 0
                else:
                    move_queue.add(ship_to_move)
                    count += 1

            if count == len(move_queue):
                break


class ShipConstellator(GamePoleOwner):
    def __init__(self, gamepole: GamePole):
        super().__init__(gamepole)
        self.allowed_cells = list(range(self.size * self.size))

    def place_ship(self, ship):
        ship.orientation = random.choice([GameOptions.HORIZONTAL, GameOptions.VERTICAL])
        local_allowed_cells = self.allowed_cells.copy()
        while local_allowed_cells:
            position_absolute = random.choice(local_allowed_cells)
            start_point = CoordConverter.absolute_to_matrix(position_absolute, self.size)
            ship.start_point = start_point
            if self.gamepole.is_collision(ship) or ship.is_out_pole(self.size):
                ship.start_point = Point(None, None)
                local_allowed_cells.remove(position_absolute)
            else:
                break

        if ship.start_point.isEmpty():
            raise ValueError('Не удалось разместить корабль. Попробуйте снова')

        restricted_area = self.gamepole.get_restricted_ship_area(ship)
        for point in restricted_area:
            abs_cell = CoordConverter.matrix_to_absolute(point, self.size)
            if abs_cell in self.allowed_cells:
                self.allowed_cells.remove(abs_cell)

    def place_ships(self):
        for ship in self.ships:
            try:
                self.place_ship(ship)
            except ValueError:
                ship.reverse_orientation()
                self.place_ship(ship)


if __name__ == "__main__":
    gp = GamePole(10)
    for c in range(1000):
        try:
            gp.init()
        finally:
            print(c)
