from scripts.day06 import *


def test_locate_guard():
    lab_map = [
        [".",".","#"],
        ["^", ".", "#"],
    ]
    guard = Guard(lab_map)
    assert guard.x == 0
    assert guard.y == 1

def test_walk():
    lab_map = [
        ["^",".",],
        [".", "."],
    ]
    guard = Guard(lab_map)

    guard.direction = "RIGHT"
    guard.walk()
    assert guard.x == 1
    assert guard.y == 0

    guard.direction = "DOWN"
    guard.walk()
    assert guard.x == 1
    assert guard.y == 1

    guard.direction = "LEFT"
    guard.walk()
    assert guard.x == 0
    assert guard.y == 1

    guard.direction = "UP"
    guard.walk()
    assert guard.x == 0
    assert guard.y == 0

def test_patrol():
    lab_map = [
        ["#", ".", "#"],
        [".", ".", "#"],
        ["^", ".", "#"],
    ]
    guard = Guard(lab_map)
    status = guard.patrol_map()
    assert status == "LEFT MAP!"
    assert guard.lab_map == [
        ["#", ".", "#"],
        ["X", "X", "#"],
        ["X", "X", "#"],
    ]
    assert guard.x == 1
    assert guard.y == 2

def test_total_visited_positions():
    lab_map = [
        ["#", ".", "#"],
        ["X", "X", "#"],
        ["X", "X", "#"],
    ]
    guard = Guard(lab_map)
    assert guard.total_visited_positions() == 4

def test_turn():
    guard = Guard([["."]])
    guard.direction = "DOWN"
    guard.turn()
    assert guard.direction == "LEFT"
    guard.turn()
    assert guard.direction == "UP"
    guard.turn()
    assert guard.direction == "RIGHT"
    guard.turn()
    assert guard.direction == "DOWN"



def test_part_one():
    assert part_one("./inputs/06_test.txt") == 41


def test_looped():
    lab_map = [
        [".", "#", ".","."],
        [".", ".", ".","#"],
        ["#", "^", ".","."],
        [".", ".", "#", "."],
    ]
    guard = Guard(lab_map)
    status = guard.patrol_map()
    assert status == "LOOPED!"
    assert guard.lab_map == [
        [".", "#", ".", "."],
        [".", "X", "X", "#"],
        ["#", "X", "X", "."],
        [".", ".", "#", "."],
    ]

def test_part_two():
    assert part_two("./inputs/06_test.txt") == 6