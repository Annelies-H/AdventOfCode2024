from collections import namedtuple
import re

from sympy import symbols, Eq, solve, Integer
from math import sqrt, pow

Button = namedtuple("Button", ["dx", "dy"])
Prize = namedtuple("Prize", ["x", "y"])
ClawMachine = namedtuple("ClawMachine", ["a", "b", "prize"])
N, M = symbols('N M')


def parse_input(filepath):
    with open(filepath, 'r') as f:
        line = f.readline()
        machines = []
        while line:
            button_a = parse_button(line)
            line = f.readline()
            button_b = parse_button(line)
            line = f.readline()
            prize = parse_prize(line)
            machine = ClawMachine(button_a, button_b, prize)
            machines.append(machine)
            line = f.readline()
            line = f.readline()
    return machines


def parse_button(line):
    pattern = r"[0-9]+"
    distances = re.findall(pattern, line)
    return Button(int(distances[0]), int(distances[1]))

def parse_prize(line):
    pattern = r"[0-9]+"
    distances = re.findall(pattern, line)
    return Prize(int(distances[0]), int(distances[1]))


def minimum_tokens_for_machine(button_a, button_b, prize):
    equation_x = Eq(N * button_a.dx + M * button_b.dx, prize.x)
    equation_y = Eq(N * button_a.dy + M * button_b.dy, prize.y)
    button_presses = solve((equation_x, equation_y), (N, M))

    if not isinstance(button_presses[N], Integer):
        return 0
    tokens = button_presses[N]*3 + button_presses[M]
    return tokens

def minimum_tokens(machines):
    tokens = 0
    for machine in machines:
        tokens += minimum_tokens_for_machine(machine.a, machine.b, machine.prize)
    return tokens


def minimum_tokens_for_machine_with_conversion(button_a, button_b, prize):
    equation_x = Eq(N * button_a.dx + M * button_b.dx, prize.x + 10000000000000)
    equation_y = Eq(N * button_a.dy + M * button_b.dy, prize.y + 10000000000000)
    button_presses = solve((equation_x, equation_y), (N, M))

    if not isinstance(button_presses[N], Integer):
        return 0
    if not isinstance(button_presses[M], Integer):
        return 0
    tokens = button_presses[N]*3 + button_presses[M]
    return tokens

def minimum_tokens_with_conversion(machines):
    tokens = 0
    for machine in machines:
        tokens += minimum_tokens_for_machine_with_conversion(machine.a, machine.b, machine.prize)
    return tokens

def part_one(filepath="./inputs/13.txt"):
    machines = parse_input(filepath)
    tokens = minimum_tokens(machines)
    return tokens

def part_two(filepath="./inputs/13.txt"):
    machines = parse_input(filepath)
    tokens = minimum_tokens_with_conversion(machines)
    return tokens


# don't need all below, was misguided trying to be smart and use diagonals
def diagonal(x, y):
    return sqrt(pow(x, 2) + pow(y, 2))


def decimal_button_presses(button_a, button_b, prize):
    # of course this doesn't work because button presess need to be whole numbers...
    distance_a = diagonal(button_a.dx, button_a.dy)
    distance_b = diagonal(button_b.dx, button_b.dy)
    distance_prize = diagonal(prize.x, prize.y)

    equation_1 = Eq(N * distance_a + M * distance_b, distance_prize)
    equation_2 = Eq(2 *N * distance_a + 2* M * distance_b, 2* distance_prize)
    solution = solve((equation_1, equation_2), (N, M))

    button_presses = solution[N] + solution[M]
    return button_presses

def decimal_minimum_tokens(button_a, button_b, prize):
    """"
    n*distance_a + m*distance_b = distance_prize
    n*distance_a = distance_prize - m*distance_b
    n = (distance_prize - m*distance_b) / distance_a
    """
    # no no no this gives non integer diagonals so does not work
    distance_a = diagonal(button_a.dx, button_a.dy)
    distance_b = diagonal(button_b.dx, button_b.dy)
    distance_prize = diagonal(prize.x, prize.y)

    min_tokens = 401
    # max 100 button presses
    for m in range(0, 100):
        if m == 40:
            h = 4
        divide_this = distance_prize - m * distance_b
        if divide_this % distance_a != 0:
            # n is not an integer
            continue
        n = int(divide_this / distance_a)
        tokens = 3*m + n
        min_tokens = min(min_tokens, tokens)

    return min_tokens





