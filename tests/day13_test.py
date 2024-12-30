from scripts.day13 import *


def test_minimum_tokens():
    button_a = Button(94, 34)
    button_b = Button(22, 67)
    prize = Prize(8400, 5400)

    tokens = minimum_tokens_for_machine(button_a, button_b, prize)
    assert tokens == 280

    button_a = Button(17, 86)
    button_b = Button(84, 37)
    prize = Prize(7870, 6450)

    tokens = minimum_tokens_for_machine(button_a, button_b, prize)
    assert tokens == 200

def test_minimum_tokens_no_solution():
    button_a = Button(26, 66)
    button_b = Button(67, 51)
    prize = Prize(12748, 12176)

    tokens = minimum_tokens_for_machine(button_a, button_b, prize)
    assert not tokens

    button_a = Button(69, 23)
    button_b = Button(27, 71)
    prize = Prize(18641, 10279)

    tokens = minimum_tokens_for_machine(button_a, button_b, prize)
    assert not tokens

def test_prize_button():
    line = "Button A: X+94, Y+34"
    button = parse_button(line)
    assert button.dx == 94
    assert button.dy == 34

def test_parse_button():
    line = "Prize: X=8400, Y=5400"
    button = parse_button(line)
    assert button.dx == 8400
    assert button.dy == 5400

def test_parse_machines():
    machines = parse_input("./inputs/13_test.txt")
    assert len(machines) == 4
    machine = machines[0]
    assert machine.a.dx == 94
    assert machine.b.dx == 22
    assert machine.prize.x == 8400


def test_part_one():
    assert part_one("./inputs/13_test.txt") == 480

def test_part_two():
    result = part_one("./inputs/13_test.txt")



#####
def test_diagonal():
    assert diagonal(3, 4) == 5
    assert diagonal(20, 50) == sqrt(2900)

def test_button_presses():
    button_a = Button(94, 34)
    button_b = Button(22, 67)
    prize = Prize(8400, 5400)

    button_presses = decimal_button_presses(button_a, button_b, prize)
    assert button_presses == 120

def test_decimal_minimum_tokens():
    button_a = Button(94, 34)
    button_b = Button(22, 67)
    prize = Prize(8400, 5400)

    tokens = decimal_minimum_tokens(button_a, button_b, prize)
    assert tokens == 280

