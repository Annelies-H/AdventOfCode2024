from collections import Counter

from inputs.d11 import stone_line

def blink_once(stone_line):
    new_line = []
    for stone in stone_line:
        if stone == 0:
            new_line.append(1)
        elif len(string_stone := str(stone)) % 2 == 0:
            half = int(len(string_stone) / 2)
            new_line.append(int(string_stone[:half]))
            new_line.append(int(string_stone[half:]))
        else:
            new_line.append(stone * 2024)
    return new_line

def blink(stone_line, blinks):
    for i in range(0, blinks):
        print(i)
        stone_line = blink_once(stone_line)
    return stone_line

def _blink_stone(stone, blinks):
    if stone == 0:
        blinked = min(blinks, 35)
        stone_line = STARTING_WITH_ZERO[blinked]
        return stone_line, blinks - blinked
    if len(string_stone := str(stone)) % 2 == 0:
        stone_line = []
        half = int(len(string_stone) / 2)
        stone_line.append(int(string_stone[:half]))
        stone_line.append(int(string_stone[half:]))
        return stone_line, blinks - 1
    return blink_stone(stone * 2024, blinks - 1)


def blink_stone(stone, blinks):
    if stone == 0:
        blinked = min(blinks, 35)
        stone_line = STARTING_WITH_ZERO[blinked]
        return stone_line, blinks - blinked
    if len(str(stone)) % 2 == 0:
        stone_line, blinked = split_stones([stone], blinks)
        return stone_line, blinks - blinked
    return blink_stone(stone * 2024, blinks - 1)


def split_stones(stones, blinks, splits = 0):
    if blinks == 0 or len(str(stones[0])) % 2 != 0:
       return stones, splits

    stone_line = []
    for stone in stones:
        string_stone = str(stone)
        half = int(len(string_stone) / 2)
        stone_line.append(int(string_stone[:half]))
        stone_line.append(int(string_stone[half:]))
    return split_stones(stone_line, blinks - 1, splits + 1)

STARTING_WITH_ZERO = {}

def fill_starting_with_zero(blinks):
    stones = [0]
    for i in range(1, blinks + 1):
        stones = blink_once(stones)
        STARTING_WITH_ZERO[i] = stones
    return STARTING_WITH_ZERO


def blink_stone_once(stone):
    new_stone = []
    if stone == 0:
        new_stone.append(1)
    elif len(string_stone := str(stone)) % 2 == 0:
        half = int(len(string_stone) / 2)
        new_stone.append(int(string_stone[:half]))
        new_stone.append(int(string_stone[half:]))
    else:
        new_stone.append(stone * 2024)
    return new_stone


def blink_stones_once(stones: Counter):
    new_stones = Counter()
    for stone in stones.keys():
        blinked_stones = blink_stone_once(stone)
        for blinked_stone in blinked_stones:
            new_stones[blinked_stone] += stones[stone]
    return new_stones

def blink_stones(stones: list[int], blinks):
    stones = Counter(stones)
    for _ in range(blinks):
        stones = blink_stones_once(stones)
    return stones


def part_one(stone_line = stone_line):
    after_blinking = blink(stone_line, 25)
    return len(after_blinking)

def part_two(stone_line = stone_line):
    after_blinking = blink_stones(stone_line, 75)
    total_stones = sum(after_blinking.values())
    return total_stones


