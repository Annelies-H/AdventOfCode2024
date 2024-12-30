import itertools
from collections import namedtuple




Equation = namedtuple("Equation", ["result", "values"])
combinations_cache = {}

def parse_file(filepath: str) ->list[Equation]:
    equations = []
    with open(filepath, 'r') as f:
        line = f.readline()
        while line:
            result, input = line.split(":")
            split_input = input.split(" ")
            values = [int(value.strip()) for value in split_input if value]
            equations.append(Equation(int(result), values))
            line = f.readline()
    return equations

combinations = {}

def get_operator_combinations(operators: list[str], length: int) -> list[list[str]]:
    if combinations_cache.get(length):
        return combinations_cache.get(length)
    combinations = list(itertools.product(operators, repeat=length-1))
    combinations_cache[length] = combinations
    return list(combinations)


def evaluate(operators: list[str], equation: Equation) -> int:
    values = equation.values
    combinations = get_operator_combinations(operators, len(values))
    expected_result = equation.result

    for combination in combinations:
        result = values[0]
        for index, operator in enumerate(combination, 1):
            if operator == "ADD":
                result += values[index]
            elif operator == "MULTIPLY":
                result *= values[index]
            elif operator == "CONCATENATE":
                result = int(str(result) + str(values[index]))
            if result > expected_result:
                break
        if result == expected_result:
            return expected_result

    return 0


def part_one(filepath="./inputs/07.txt") -> int:
    equations = parse_file(filepath)
    result = 0
    for equation in equations:
        result += evaluate(["ADD", "MULTIPLY"], equation)
    return result


def part_two(filepath="./inputs/07.txt") -> int:
    equations = parse_file(filepath)
    result = 0
    for equation in equations:
        result += evaluate(["ADD", "MULTIPLY", "CONCATENATE"], equation)
    return result
