from scripts.day08 import *

def test_get_antenna_locations():
    city_map = [
        [".","0", "."],
        [".", "A", "0"]
    ]
    locations = get_antenna_locations(city_map)
    assert "." not in locations.keys()
    assert locations["A"] == [Coordinate(1, 1)]
    assert locations["0"] == [Coordinate(1, 0), Coordinate(2, 1)]


def test_get_antinodes():
    one = Coordinate(4,3)
    two = Coordinate(5,5)
    node_1, node_2 = get_antinodes(one, two)
    assert node_1 == Coordinate(3, 1)
    assert node_2 == Coordinate(6, 7)

    two = Coordinate(4,3)
    one = Coordinate(5,5)
    node_1, node_2 = get_antinodes(one, two)
    assert node_2 == Coordinate(3, 1)
    assert node_1 == Coordinate(6, 7)

    one = Coordinate(8,1)
    two = Coordinate(5,2)
    node_1, node_2 = get_antinodes(one, two)
    assert node_1 == Coordinate(11, 0)
    assert node_2 == Coordinate(2, 3)

    two = Coordinate(8,1)
    one = Coordinate(5,2)
    node_1, node_2 = get_antinodes(one, two)
    assert node_2 == Coordinate(11, 0)
    assert node_1 == Coordinate(2, 3)

def test_part_one():
    assert part_one("./inputs/08_test.txt") == 14

def test_antinode_diagonals():
    antenna_locations = {
        "T": [Coordinate(0,0), Coordinate(3, 1), Coordinate(1, 2)]
    }
    diagonals = find_all_antinode_diagonals(antenna_locations)
    assert diagonals[Coordinate(0, 0)] == {(3, 1), (1, 2)}
    assert diagonals[Coordinate(3, 1)] == {(-2, 1)}

def test_find_all_nodes_on_diagonals():
    diagonals = {}
    diagonals[Coordinate(0, 0)] = {(3, 1), (1, 2)}
    diagonals[Coordinate(3, 1)] = {(-2, 1)}
    antinodes = find_all_antinodes_on_diagonals(diagonals=diagonals, x_max=11, y_max=10)
    assert antinodes == {
        # antennas:
        Coordinate(0, 0),
        Coordinate(3, 1),
        Coordinate(1, 2),
        # antinodies
        Coordinate(5, 0),
        Coordinate(6, 2),
        Coordinate(9, 3),
        Coordinate(2, 4),
        Coordinate(3, 6),
        Coordinate(4, 8)
    }

def test_part_two():
    assert part_two("./inputs/08_test_Tmap.txt") == 9
    assert part_two("./inputs/08_test.txt") == 34