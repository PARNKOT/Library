from typing import List


class GameOptions:
    ONE_DECKS = 4
    TWO_DECKS = 3
    THREE_DECKS = 2
    FOUR_DECKS = 1

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

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return (self._x, self._y)

    def move(self, go):
        if self._tp == GameOptions.HORIZONTAL:
            next_coord = self._x + go
            if next_coord


class GamePole:
    __slots__ = ('_size', '_ships')

    def __init__(self, size):
        self._size = size
        self._ships: List[Ship] = []

    def init(self):
        ships = [
            [Ship(1) for i in range(GameOptions.ONE_DECKS)],
            [Ship(2) for i in range(GameOptions.TWO_DECKS)],
            [Ship(3) for i in range(GameOptions.THREE_DECKS)],
            [Ship(4) for i in range(GameOptions.FOUR_DECKS)],
        ]
        for ship_type in ships:
            self._ships.extend(ship_type)


