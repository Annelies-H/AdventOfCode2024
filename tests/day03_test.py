from scripts.day03 import *

def test_parse_memory():
    input = "23487mul(45,3)sfd"
    assert find_mul_instructions(input) == ["mul(45,3)"]

    input = "23487mul(123,456)sfd"
    assert find_mul_instructions(input) == ["mul(123,456)"]

    # too many digits
    input = "23487mul(4554,3)sfd"
    assert find_mul_instructions(input) == []

    # no closing bracket
    input = "23487mul(4554,3sfd"
    assert find_mul_instructions(input) == []

    # special characters
    input = "23487mul(4$5,3)sfd"
    assert find_mul_instructions(input) == []

def test_execute_mul_instruction():
    instruction = "mul(3,4)"
    assert execute_mul_instruction(instruction) == 12
    assert  instruction == "mul(3,4)"

def test_find_all_instructions():
    input = "23487mul(45,3)sfddon'tlasdjfdo()don't()"
    assert find_all_instructions(input) == ["mul(45,3)", "do()", "don't()"]

def test_part_one():
    assert part_one("./inputs/03_test.txt") == 161

def test_part_two():
    assert part_two("./inputs/03_test.txt") == 161
    assert part_two("./inputs/03p2_test.txt") == 48