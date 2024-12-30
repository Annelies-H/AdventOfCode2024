from enum import Enum
from typing import Any
from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


    def __str__(self):
        return f"(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def within_bounds(self, topleft: "Coordinate", bottomright: "Coordinate") -> bool:
        return self.x >= topleft.x and self.x <= bottomright.x and self.y >= topleft.y and self.y <= bottomright.y


@dataclass(frozen=True)
class Velocity:
    dx: int
    dy: int

    def __str__(self):
        return f"(dx={self.dx}, dy={self.dy})"

    def __eq__(self, other):
        return self.dx == other.dx and self.dy == other.dy


class Direction(Enum):
    N = ("North", Velocity(dx=0, dy=-1))
    NE = ("NorthEast", Velocity(dx=1, dy=-1))
    E = ("East", Velocity(dx=1, dy=0))
    SE = ("SouthEast", Velocity(dx=1, dy=1))
    S = ("South", Velocity(dx=0, dy=1))
    SW = ("SouthWest", Velocity(dx=-1, dy=1))
    W = ("West", Velocity(dx=-1, dy=0))
    NW = ("NorthWest", Velocity(dx=-1, dy=-1))

    def __init__(self, label, velocity):
        self.velocity = velocity
        self.label = label

    @classmethod
    def all(cls) -> list[Velocity]:
        return [direction for direction in Direction]

    @classmethod
    def orthogonal(cls)  -> list[Velocity]:
        return [cls.N, cls.E, cls.S, cls.W]

    @classmethod
    def diagonal(cls) -> list[Velocity]:
        return [cls.NE, cls.SE, cls.SW, cls.NW]

class Grid:
    """
    Abstract grid class for 2d grids.
    The origin of the grid (0,0) is at the topleft corner.
    positive x moves right, negative moves left
    positive y moves down, negative y moves up

    """
    def __init__(self, width: int, height: int, initial_grid: Any = None, default_cell: Any=None):
        x_min = 0
        y_min = 0
        x_max = x_min + width - 1
        y_max = y_min + height - 1

        # set boundaries
        self.width = width
        self.height = height
        self.min = Coordinate(x=x_min, y=y_min)
        self.max = Coordinate(x=x_max, y=y_max)

        # set grid
        self.grid = initial_grid
        self.default = default_cell

    def set_cell(self, coord: Coordinate, value: Any):
        raise NotImplemented

    def get_cell(self, coord: Coordinate):
        raise NotImplemented

    def locate_values(self, value: Any) -> list[Coordinate]:
        raise NotImplemented

    def next_position(self, coord: Coordinate, velocity: Velocity, wrap=False):
        """
        Find the next position (coordinate) based on the current coordinate and the velocity.
        Returns an out of bound error when wrap = False and the new position is outside the grid.
        When wrap is True the new position will be wrapped around the grid.
        """
        new_x = coord.x + velocity.dx
        new_y = coord.y + velocity.dy
        new_coord = Coordinate(x=new_x, y=new_y)
        if not self.out_of_bounds(new_coord):
            return new_coord
        if not wrap:
            self.raise_out_of_bounds(new_coord)

        wrapped_x = new_x % self.width
        wrapped_y = new_y % self.height

        return Coordinate(wrapped_x, wrapped_y)


    def travel_in_direction(self, coord: Coordinate, direction: Direction) -> Coordinate:
        """
        Find the next position based on a direction
        does not wrap around the grid
        """
        return self.next_position(coord, direction.velocity)

    def find_neighbours(self, coord: Coordinate, orthogonal: bool = True, diagonal: bool = True) -> list[Coordinate]:
        if orthogonal and diagonal:
            directions = Direction.all()
        elif orthogonal:
            directions = Direction.orthogonal()
        elif diagonal:
            directions = Direction.diagonal()
        else:
            directions = []

        neighbours = []
        for direction in directions:
            try:
                neighbours.append(self.travel_in_direction(coord, direction))
            except OutOfBoundsException:
                pass

        return neighbours

    def out_of_bounds(self, coord: Coordinate) -> bool:
        return not coord.within_bounds(self.min, self.max)
        #return coord.x < self.min.x or coord.y < self.min.y or coord.x > self.max.x or coord.y > self.max.y

    def raise_out_of_bounds(self, coord: Coordinate):
        message = f"Coordinate {coord} if out of bounds for grid: Topleft: {self.min}, Bottomright: {self.max}"
        raise OutOfBoundsException(message)


class ArrayGrid(Grid):
    """"
    2D array grid which always has the origin (top left) at 0,0
    Requires an initial grid containing an array of arrays
    """
    def __init__(self, initial_grid: list[list[Any]], *args, **kwargs):
        x_min = 0
        y_min = 0
        x_max = len(initial_grid[0]) - 1
        y_max = len(initial_grid) - 1

        # set boundaries
        self.min = Coordinate(x=0, y=0)
        self.max = Coordinate(x=x_max, y=y_max)

        # set grid
        self.grid = initial_grid

    def set_cell(self, coord: Coordinate, value: Any):
        if self.out_of_bounds(coord):
            raise OutOfBoundsException
        self.grid[coord.y][coord.x] = value

    def get_cell(self, coord: Coordinate):
        if self.out_of_bounds(coord):
            self.raise_out_of_bounds(coord)
        return self.grid[coord.y][coord.x]

    def print(self):
        print()
        for row in self.grid:
            print(row)
        print()

    def locate_values(self, value: Any) -> list[Coordinate]:
        coordinates = []
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == value:
                    coordinates.append(Coordinate(x, y))
        return coordinates

class DictionaryGrid(Grid):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.grid:
            self.grid = {}
    def set_cell(self, coord: Coordinate, value: Any):
        if self.out_of_bounds(coord):
            raise OutOfBoundsException
        self.grid[coord] = value

    def get_cell(self, coord: Coordinate):
        if self.out_of_bounds(coord):
            self.raise_out_of_bounds(coord)
        return self.grid.get(coord, self.default)

    def locate_values(self, value: Any) -> list[Coordinate]:
        coordinates = []
        for key in self.grid.keys():
            if self.grid[key] == value:
                coordinates.append(key)
        return coordinates


class OutOfBoundsException(Exception):
    """"Coordinate falls outside the grid"""
