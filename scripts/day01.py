

def parse_file(filepath: str) -> tuple[list[str]]:
    with open(filepath, 'r') as f:
        line = f.readline()
        lefts = []
        rights = []
        while line:
            left, right = line.split()
            lefts.append(int(left))
            rights.append(int(right))
            line = f.readline()
    return lefts, rights


def total_distance(lefts: list[str], rights: list[str]) -> int:
    lefts.sort()
    rights.sort()
    total_distance = 0
    for index, right in enumerate(rights):
        left = lefts[index]
        total_distance += abs(left - right)
    return total_distance


def similarity_score(lefts: list[str], rights: list[str]) -> int:
    similarity_score = 0
    for left in lefts:
        score = rights.count(left)
        similarity_score += score * int(left)
    return similarity_score


def part_one(filepath="./inputs/01.txt") -> int:
    lefts, rights = parse_file(filepath)
    distance = total_distance(lefts, rights)
    return distance

def part_two(filepath="./inputs/01.txt") -> int:
    lefts, rights = parse_file(filepath)
    score = similarity_score(lefts, rights)
    return score