from scripts.day11 import *

def test_blink():
    assert blink_once([0]) == [1]
    assert blink_once([12]) == [1, 2]
    assert blink_once([1000]) == [10, 0]
    assert blink_once([1]) == [2024]

def test_blink():
    stone_line = [125, 17]
    after_blinks = blink(stone_line, 1)
    assert after_blinks == [253000, 1, 7]

    after_blinks = blink(stone_line, 6)
    assert after_blinks == [
        2097446912, 14168, 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2
    ]

def test_fill_starting_with_zero():
    starting_with_zero = fill_starting_with_zero(4)
    assert starting_with_zero[4] == [2, 0, 2, 4]

    starting_with_zero = fill_starting_with_zero(35)
    assert len(starting_with_zero.keys()) == 35

def test_blink_stone():
    starting_with_zero = fill_starting_with_zero(36)
    line, blinks = blink_stone(0, 10)
    assert blinks == 0
    assert line == starting_with_zero[10]

    line, blinks = blink_stone(0, 40)
    assert blinks == 5
    assert line == starting_with_zero[35]

    line, blinks = blink_stone(11111111, 5)
    assert line == [1, 1, 1, 1, 1, 1, 1, 1]
    assert blinks == 2

    line, blinks = blink_stone(125, 5)
    assert line == [253, 0]
    assert blinks == 3

    line, blinks = blink_stone(11111111, 2)
    assert line == [11, 11, 11, 11]
    assert blinks == 0

def test_split_stones():
    stones = [1]
    line, blinks = split_stones(stones, 999)
    assert line == [1]
    assert blinks == 0

    stones = [11]
    line, blinks = split_stones(stones, 999)
    assert line == [1, 1]
    assert blinks == 1


    stones = [11111111]
    line, blinks = split_stones(stones, 999)
    assert line == [1, 1, 1, 1, 1, 1, 1, 1]
    assert blinks == 3

    stones = [11111111]
    line, blinks = split_stones(stones, 1)
    assert line == [1111, 1111]
    assert blinks == 1

    stones = [253000]
    line, blinks = split_stones(stones, 999)
    assert line == [253, 0]
    assert blinks == 1


def test_part_one():
    stone_line = [125, 17]
    assert part_one(stone_line) == 55312

def test_part_two():
    stone_line = [125, 17]
    assert part_two(stone_line) == 55312