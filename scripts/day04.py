

def parse_file_with_padding(filepath: str) -> list[list[str]]:
    puzzle = []
    with open(filepath, 'r') as f:
        line = f.readline()
        row_size = len(line) + 5
        puzzle.append(row_size * ".")
        puzzle.append(row_size * ".")
        puzzle.append(row_size * ".")

        while line:
            row = list(line)
            if row[-1] == "\n":
                row.pop(-1)
            padded_row = [".", ".", "."] + row + [".", ".", "."]
            puzzle.append(padded_row)
            line = f.readline()

        puzzle.append(row_size * ".")
        puzzle.append(row_size * ".")
        puzzle.append(row_size * ".")
    return puzzle


def parse_file(filepath: str) -> list[list[str]]:
    puzzle = []
    with open(filepath, 'r') as f:
        line = f.readline()
        while line:
            row = list(line)
            if row[-1] == "\n":
                row.pop(-1)
            puzzle.append(row)
            line = f.readline()
    return puzzle

def find_all_xmas(puzzle) -> int:
    result = 0
    for y in range(0, len(puzzle)):
        for x in range(0, len(puzzle[0])):
            result += check_xmas(puzzle, x, y)
    return result

def check_xmas(puzzle, x, y):
    result = 0
    xmax = len(puzzle[0])-3
    ymax = len(puzzle[0])-3
    if not puzzle[y][x] == "X":
        return result
    if x>2 and y>2 and puzzle[y-1][x-1] == "M" and puzzle[y-2][x-2] == "A" and puzzle[y-3][x-3] == "S":
        result += 1
        print(f"{y},{x}-linksboven")
    if x<xmax and y<ymax and puzzle[y+1][x+1] == "M" and puzzle[y+2][x+2] == "A" and puzzle[y+3][x+3] == "S":
        result += 1
        print(f"{y},{x}-rechtsonder")
    if x>2 and y<ymax and puzzle[y+1][x-1] == "M" and puzzle[y+2][x-2] == "A" and puzzle[y+3][x-3] == "S":
        result += 1
        print(f"{y},{x}-linksonder")
    if x<xmax and y>2 and puzzle[y-1][x+1] == "M" and puzzle[y-2][x+2] == "A" and puzzle[y-3][x+3] == "S":
        result += 1
        print(f"{y},{x}-rechtsboven")
    if x>2 and puzzle[y][x-1] == "M" and puzzle[y][x-2] == "A" and puzzle[y][x-3] == "S":
        result += 1
        print(f"{y},{x}-links")
    if x<xmax and puzzle[y][x+1] == "M" and puzzle[y][x+2] == "A" and puzzle[y][x+3] == "S":
        result += 1
        print(f"{y},{x}-rechts")
    if y<ymax and puzzle[y+1][x] == "M" and puzzle[y+2][x] == "A" and puzzle[y+3][x] == "S":
        result += 1
        print(f"{y},{x}-onder")
    if  y>2 and puzzle[y-1][x] == "M" and puzzle[y-2][x] == "A" and puzzle[y-3][x] == "S":
        result += 1
        print(f"{y},{x}-boven")
    return result


def part_one(filepath="./inputs/04.txt") -> int:
    puzzle = parse_file(filepath)
    xmas_count = find_all_xmas(puzzle)
    return xmas_count


def find_all_cross_mas(puzzle) -> int:
    result = 0
    for y in range(1, len(puzzle) -1):
        for x in range(1, len(puzzle[0])-1):
            if check_cross_mas(puzzle, x, y):
                #print(f"{y},{x}")
                result += 1
    return result


def check_cross_mas(puzzle, x, y) -> bool:
    if not puzzle[y][x] == "A":
        return False
    first = puzzle[y-1][x-1] + "A" + puzzle[y+1][x+1]
    if not first in ["MAS", "SAM"]:
        return False
    second = puzzle[y+1][x-1] + "A" + puzzle[y-1][x+1]
    return second in ["MAS", "SAM"]

def part_two(filepath="./inputs/04.txt") -> int:
    puzzle = parse_file(filepath)
    xmas_count = find_all_cross_mas(puzzle)
    return xmas_count

