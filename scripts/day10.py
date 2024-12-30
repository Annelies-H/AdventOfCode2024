from collections import namedtuple

from utils import parse_int_map

Coordinate = namedtuple("Coordinates", ["x", "y"])


def get_score(topography, coord):
    peaks = get_peaks(topography, coord, set())
    return len(peaks)

def get_peaks(topography, coord, coords):
    height = topography[coord.y][coord.x]
    if height == 9:
        return set([coord])
    # check up
    if coord.y > 0:
        up = Coordinate(coord.x, coord.y - 1)
        if topography[up.y][up.x] - height == 1:
            coords |= get_peaks(topography, up, coords)
    # check right
    if coord.x < (len(topography[0]) -1):
        right = Coordinate(coord.x + 1, coord.y)
        if topography[right.y][right.x] - height == 1:
            coords |= get_peaks(topography, right, coords)
    # check down
    if coord.y < (len(topography) -1):
        down = Coordinate(coord.x, coord.y + 1)
        if topography[down.y][down.x] - height == 1:
            coords |= get_peaks(topography, down, coords)
    # check left
    if coord.x > 0:
        left = Coordinate(coord.x -1, coord.y)
        if topography[left.y][left.x] - height == 1:
            coords |= get_peaks(topography, left, coords)
    return coords

def get_total_score(topography):
    total_score = 0
    for y in range(0, len(topography)):
        for x in range(0, len(topography[0])):
            if topography[y][x] == 0:
                total_score += get_score(topography, Coordinate(x, y))
    return total_score

def get_total_score_distinct_trails(topography):
    total_score = 0
    for y in range(0, len(topography)):
        for x in range(0, len(topography[0])):
            if topography[y][x] == 0:
                total_score += get_score_distinct_trails(topography, Coordinate(x, y))
    return total_score

def get_score_distinct_trails(topography, coord):
    height = topography[coord.y][coord.x]
    if height == 9:
        return 1
    score = 0
    # check up
    if coord.y > 0:
        up = Coordinate(coord.x, coord.y - 1)
        if topography[up.y][up.x] - height == 1:
            score += get_score_distinct_trails(topography, up)
    # check right
    if coord.x < (len(topography[0]) -1):
        right = Coordinate(coord.x + 1, coord.y)
        if topography[right.y][right.x] - height == 1:
            score += get_score_distinct_trails(topography, right)
    # check down
    if coord.y < (len(topography) -1):
        down = Coordinate(coord.x, coord.y + 1)
        if topography[down.y][down.x] - height == 1:
            score += get_score_distinct_trails(topography, down)
    # check left
    if coord.x > 0:
        left = Coordinate(coord.x -1, coord.y)
        if topography[left.y][left.x] - height == 1:
            score += get_score_distinct_trails(topography, left)
    return score


def part_one(filepath="./inputs/10.txt") -> int:
    topography = parse_int_map(filepath)
    total_score = get_total_score(topography)
    return total_score

def part_two(filepath="./inputs/10.txt") -> int:
    topography = parse_int_map(filepath)
    total_score = get_total_score_distinct_trails(topography)
    return total_score