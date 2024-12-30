from collections import Counter

from scripts.day14 import *


def test_parse_robots():
    grid = Grid(3,4)
    robots = parse_robots("./inputs/14_test.txt", grid)
    assert len(robots) == 12
    first_robot = robots[0]
    assert first_robot.position == Coordinate(0,4)
    assert first_robot.velocity == Velocity(3, -3)


def test_move():
    grid = Grid(width=11, height=7)
    robot = Robot(Coordinate(2, 4), Velocity(2, -3), grid)

    robot.move()
    assert robot.position == Coordinate(4, 1)

    robot.move(3)
    assert robot.position == Coordinate(10, 6)

    robot = Robot(Coordinate(2, 4), Velocity(2, -3), grid)
    robot.move(5)
    assert robot.position == Coordinate(1, 3)

def test_move_robots():
    grid = Grid(11, 7)
    robots = parse_robots("./inputs/14_test.txt", grid)
    move_robots(robots, 100)
    positions = [robot.position for robot in robots]
    tiles_with_robots = Counter(positions)
    expected_tiles_with_robots = {
        Coordinate(6, 0): 2,
        Coordinate(9, 0): 1,
        Coordinate(0, 2): 1,
        Coordinate(1, 3): 1,
        Coordinate(2, 3): 1,
        Coordinate(5, 4): 1,
        Coordinate(3, 5): 1,
        Coordinate(4, 5): 2,
        Coordinate(1, 6): 1,
        Coordinate(6, 6): 1
    }
    assert tiles_with_robots == expected_tiles_with_robots



def test_get_quadrants():
    quadrants = get_quadrants(5, 5)
    assert quadrants == [
        (Coordinate(0, 0), Coordinate(1, 1)),
        (Coordinate(3, 0), Coordinate(4, 1)),
        (Coordinate(0, 3), Coordinate(1, 4)),
        (Coordinate(3, 3), Coordinate(4, 4)),
    ]

def test_part_one():
    assert part_one("./inputs/14_test.txt", 11, 7) == 12
