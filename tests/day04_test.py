from scripts.day04 import *

def test_parse_file_padding():
    puzzle = parse_file_with_padding("./inputs/04_test.txt")
    assert len(puzzle) == 16
    assert len(puzzle[5]) == 16

def test_part_one():
    assert part_one("./inputs/04_test.txt") == 18

def test_part_two():
    assert part_two("./inputs/04_test.txt") == 9