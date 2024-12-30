from unittest import TestCase

from utils.grids import *


class TestCoordinate():

    def test_to_string(self):
        coord = Coordinate(x=4, y=777)
        assert str(coord) == "(x=4, y=777)"

    def test_equal(self):
        coord_1 = Coordinate(x=4, y=777)
        coord_2 = Coordinate(x=4, y=777)

        assert coord_1 == coord_2

    def test_not_equal(self):
        coord_1 = Coordinate(x=4, y=777)
        coord_2 = Coordinate(x=5, y=5)
        assert not coord_1 == coord_2


class TestVelocity():

    def test_equal(self):
        dxy_1 = Velocity(1, 2)
        dxy_2 = Velocity(1, 2)

        assert dxy_1 == dxy_2

    def test_not_equal(self):
        dxy_1 = Velocity(1, 2)
        dxy_2 = Velocity(2, 2)

        assert not dxy_1 == dxy_2


class TestDirection():
    def test_orthogonal(self):
        orthogonal = Direction.orthogonal()
        assert orthogonal == [
            Direction.N,
            Direction.E,
            Direction.S,
            Direction.W
        ]

    def test_diagonal(self):
        diagonal = Direction.diagonal()
        assert diagonal == [
            Direction.NE,
            Direction.SE,
            Direction.SW,
            Direction.NW
        ]


class TestGrid(TestCase):
    def test_out_of_bounds(self):
        grid = Grid(width=5, height=7)

        assert not grid.out_of_bounds(Coordinate(0,0))
        assert not grid.out_of_bounds(Coordinate(4, 6))
        assert grid.out_of_bounds(Coordinate(-1, 0))
        assert grid.out_of_bounds(Coordinate(0, -1))
        assert grid.out_of_bounds(Coordinate(5, 6))
        assert grid.out_of_bounds(Coordinate(4, 7))

    def test_next_position_no_wrap(self):
        grid = Grid(width=5, height=5)
        start = Coordinate(2, 2)

        dxy = Velocity(2, 1)
        assert grid.next_position(start, dxy) == Coordinate(4, 3)
        dxy = Velocity(-2, -1)
        assert grid.next_position(start, dxy) == Coordinate(0, 1)

        with self.assertRaises(OutOfBoundsException):
            dxy = Velocity(-5, 5)
            grid.next_position(start, dxy)

    def test_next_position_with_orthogonal_wrap(self):
        grid = Grid(width=3, height=3)
        start = Coordinate(0,0)

        dxy = Velocity(5, 0)
        assert grid.next_position(start, dxy, wrap=True) == Coordinate(2,0)
        dxy = Velocity(0, 5)
        assert grid.next_position(start, dxy, wrap=True) == Coordinate(0,2)
        dxy = Velocity(-1, 0)
        assert grid.next_position(start, dxy, wrap=True) == Coordinate(2,0)
        dxy = Velocity(0, -1)
        assert grid.next_position(start, dxy, wrap=True) == Coordinate(0,2)

    def test_next_position_with_diagonal_wrap(self):
        grid = Grid(width=11, height=7)
        start = Coordinate(2, 4)
        dxy = Velocity(4, -6)

        next = grid.next_position(start, dxy, wrap=True)
        assert next == Coordinate(6, 5)

        next = grid.next_position(next, dxy, wrap=True)
        assert next == Coordinate(10, 6)

        # rotate the grid to test for negative x
        grid = Grid(width=7, height=11)
        start = Coordinate(4, 2)
        dxy = Velocity(-6, 4)

        next = grid.next_position(start, dxy, wrap=True)
        assert next == Coordinate(5, 6)

        next = grid.next_position(next, dxy, wrap=True)
        assert next == Coordinate(6, 10)

    def test_next_position_topleft_corner(self):
        grid = Grid(width=11, height=7)
        start = Coordinate(0, 0)

        dxy = Velocity(2, -3)
        next = grid.next_position(start, dxy, wrap=True)
        assert next == Coordinate(2, 4)

        dxy = Velocity(-2, 3)
        next = grid.next_position(start, dxy, wrap=True)
        assert next == Coordinate(9, 3)

    def test_next_position_bottom_right_corner(self):
        grid = Grid(width=11, height=7)
        start = Coordinate(10, 6)
        dxy = Velocity(2, -3)
        next = grid.next_position(start, dxy, wrap=True)
        assert next == Coordinate(1, 3)

        start = Coordinate(10, 6)
        dxy = Velocity(-2, 3)
        next = grid.next_position(start, dxy, wrap=True)
        assert next == Coordinate(8, 2)

    def test_next_position_top_right_corner(self):
        grid = Grid(width=11, height=7)
        start = Coordinate(10, 0)

        dxy = Velocity(2, -3)
        next = grid.next_position(start, dxy, wrap=True)
        assert next == Coordinate(1, 4)

        dxy = Velocity(-2, 3)
        next = grid.next_position(start, dxy, wrap=True)
        assert next == Coordinate(8, 3)

    def test_next_position_bottom_left_corner(self):
        grid = Grid(width=11, height=7)
        start = Coordinate(0, 6)

        dxy = Velocity(2, -3)
        next = grid.next_position(start, dxy, wrap=True)
        assert next == Coordinate(2, 3)

        dxy = Velocity(-2, 3)
        next = grid.next_position(start, dxy, wrap=True)
        assert next == Coordinate(9, 2)

    def test_travel_in_direction(self):
        grid = Grid(width=3, height=3)
        start = Coordinate(0,0)
        next_position = grid.travel_in_direction(start, Direction.SE)
        assert next_position == Coordinate(1, 1)

    def test_neighbours(self):
        grid = Grid(width=3, height=3)

        orthogonal_neighbours = grid.find_neighbours(Coordinate(1, 1), diagonal=False)
        assert orthogonal_neighbours == [
            Coordinate(1, 0),
            Coordinate(2, 1),
            Coordinate(1, 2),
            Coordinate(0, 1)
        ]

        diagonal_neighbours = grid.find_neighbours(Coordinate(1, 1), orthogonal=False)
        assert diagonal_neighbours == [
            Coordinate(2, 0),
            Coordinate(2, 2),
            Coordinate(0, 2),
            Coordinate(0, 0)
        ]

        neighbours_on_edge = grid.find_neighbours(Coordinate(0,0))
        assert neighbours_on_edge == [
            Coordinate(1, 0),
            Coordinate(1, 1),
            Coordinate(0, 1)
        ]


class TestDictionaryGrid(TestCase):
    def test_get_cell(self):
        initial_grid = {Coordinate(0,0): "my value"}
        grid = DictionaryGrid(width=3, height=5, initial_grid=initial_grid)
        assert grid.get_cell(Coordinate(0,0)) == "my value"

        # test default
        grid = DictionaryGrid(width=3, height=5, default_cell='.')
        assert grid.get_cell(Coordinate(0,0)) == '.'

        # test out of bounds
        grid = DictionaryGrid(width=3, height=5, default_cell='.')
        with self.assertRaises(OutOfBoundsException):
            grid.get_cell(Coordinate(-1,0))

    def test_set_cell(self):
        grid = DictionaryGrid(width=3, height=5)
        grid.set_cell(Coordinate(0,0), "I set this")
        assert grid.grid[Coordinate(0,0)] == "I set this"

        # test out of bounds
        grid = DictionaryGrid(width=3, height=5, default_cell='.')
        with self.assertRaises(OutOfBoundsException):
            grid.set_cell(Coordinate(-1,0), "my value")

    def test_locate_values(self):
        grid = DictionaryGrid(width=3, height=5)
        grid.set_cell(Coordinate(1, 0), 1)
        grid.set_cell(Coordinate(2, 1), 1)
        grid.set_cell(Coordinate(0,0), 9)

        coords = grid.locate_values(1)
        assert coords == [Coordinate(1, 0), Coordinate(2, 1)]


class TestArrayGrid(TestCase):
    def test_get_cell(self):
        initial_grid = [["my value", "."]]
        grid = ArrayGrid(initial_grid=initial_grid)
        assert grid.get_cell(Coordinate(0,0)) == "my value"

        with self.assertRaises(OutOfBoundsException):
            grid.get_cell(Coordinate(-1,0))

    def test_set_cell(self):
        initial_grid = [["my value", "."]]
        grid = ArrayGrid(initial_grid=initial_grid)
        grid.set_cell(Coordinate(0,0), "I set this")
        assert grid.grid[0][0] == "I set this"

        # test out of bounds
        with self.assertRaises(OutOfBoundsException):
            grid.set_cell(Coordinate(-1,0), "my value")

    def test_locate_values(self):
        initial_grid = [
            [0, 1, 0],
            [0, 0, 1],
            [0, 0, 0],
        ]
        grid = ArrayGrid(initial_grid=initial_grid)
        coords = grid.locate_values(1)
        assert coords == [Coordinate(1, 0), Coordinate(2, 1)]