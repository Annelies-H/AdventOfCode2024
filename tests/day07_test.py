from scripts.day07 import *

def test_parse_file():
    results = parse_file("./inputs/07_test.txt")

    assert len(results) == 9
    assert results[0].result == 190
    assert results[0].values == [10, 19]

def test_get_operator_combinations():
    combinations = list(get_operator_combinations(["ADD", "MULTIPLY"], 2))
    assert combinations == [("ADD",), ("MULTIPLY",)]

    combinations = list(get_operator_combinations(["ADD", "MULTIPLY"],4))
    assert len(combinations[0]) == 3

def test_evaluate():
    equation = Equation(292, [11, 6, 16, 20])
    assert evaluate(["ADD", "MULTIPLY"], equation) == 292

    equation = Equation(7290, [6, 8, 6, 15])
    assert evaluate(["ADD", "MULTIPLY"], equation) == 0


def test_part_one():
    assert part_one("./inputs/07_test.txt") == 3749

def test_part_two():
    assert part_two("./inputs/07_test.txt") == 11387