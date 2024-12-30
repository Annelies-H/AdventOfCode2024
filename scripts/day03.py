import re


def find_mul_instructions(memory: str) -> list[str]:
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    instructions = re.findall(pattern, memory)
    return instructions

def execute_mul_instruction(instruction: str) -> int:
    instruction = instruction.removeprefix("mul(")
    instruction = instruction.removesuffix(")")
    x, y = instruction.split(",")
    return int(x) * int(y)

def add_instrutions(instructions: list[str]) -> int:
    result = 0
    for instruction in instructions:
        result += execute_mul_instruction(instruction)
    return result

def parse_file(filepath: str) -> str:
    memory = ""
    with open(filepath, 'r') as f:
        line = f.readline()
        while line:
            memory += line
            line = f.readline()
    return memory

def remove_dont_parts(memory: str) -> str:
    do_dont_pattern = r"do\(\)|don't\(\)"
    split_memory = re.split(do_dont_pattern, memory)
    # todo add all non do/dont parts that follow a do part in a string
    # then use the cleanup string to get all mul parts and the susual we do in part one

def find_all_instructions(memory: str) -> list[str]:
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
    instructions = re.findall(pattern, memory)
    return instructions

def execute_all_instructions(instructions: list[str]) -> int:
    execute_mul = True
    result = 0
    for instruction in instructions:
        if instruction == "don't()":
            execute_mul = False
        elif instruction == "do()":
            execute_mul = True
        elif execute_mul:
            result += execute_mul_instruction(instruction)
    return result

def part_one(filepath="./inputs/03.txt") -> int:
    memory = parse_file(filepath)
    instructions = find_mul_instructions(memory)
    result = add_instrutions(instructions)
    return result

def part_two(filepath="./inputs/03.txt") -> int:
    memory = parse_file(filepath)
    instructions = find_all_instructions(memory)
    result = execute_all_instructions(instructions)
    return result