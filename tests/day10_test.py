from scripts.day10 import *


def test_get_score():
    topography = [
        [4, 5],
        [9, 6],
        [8, 7],
    ]
    score = get_score(topography, Coordinate(0, 0))
    assert score == 1

    topography = [
        [4, 6, 5],
        [8, 7, 8],
        [9, 6, 9],
    ]
    score = get_score(topography, Coordinate(1, 0))
    assert score == 2

def test_get_score_two_path_same_peak():
    topography = [
        [7, 8],
        [8, 9]
    ]
    score = get_score(topography, Coordinate(0, 0))
    assert score == 1

def test_get_score_b_map():
    topography = [
        [-1,-1, 9, 0,-1,-1, 9],
        [-1,-1,-1, 1,-1, 9, 8],
        [-1,-1,-1, 2,-1,-1, 7],
        [ 6, 5, 4, 3, 4, 5, 6],
        [ 7, 6, 5,-1, 9, 8, 7],
        [ 8, 7, 6,-1,-1,-1,-1],
        [9,8,7,1,1,1,1],
    ]
def test_part_one():
    assert part_one("./inputs/10a_test.txt") == 2
    assert part_one("./inputs/10b_test.txt") == 4
    assert part_one("./inputs/10_test.txt") == 36

def test_part_two():
    assert part_two("./inputs/10_test.txt") == 81
