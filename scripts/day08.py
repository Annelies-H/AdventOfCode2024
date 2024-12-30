import itertools
from collections import defaultdict, namedtuple

from utils.fileparsers import parse_map

Coordinate = namedtuple("Coordinates", ["x", "y"])

def get_antenna_locations(city_map) -> dict:
    locations = defaultdict(list)
    for y, row in enumerate(city_map):
        for x, value in enumerate(row):
            if value == ".":
                continue
            locations[value].append(Coordinate(x, y))
    return locations


def get_antenna_pairs(coordinates: list[Coordinate]) -> list[tuple[Coordinate]]:
    pairs = itertools.combinations(coordinates, 2)
    return list(pairs)

def get_antinodes(one: Coordinate, two: Coordinate) -> tuple[Coordinate]:
    dx = two.x - one.x
    dy = two.y - one.y
    node_1 = Coordinate(one.x - dx, one.y - dy)
    node_2 = Coordinate(two.x + dx, two.y + dy)
    return node_1, node_2

def find_all_antinodes(antenna_locations: dict) -> set[Coordinate]:
    antinodes = set()
    for key in antenna_locations.keys():
        antennas = antenna_locations[key]
        antenna_pairs = get_antenna_pairs(antennas)
        for pair in antenna_pairs:
            node_1, node_2 = get_antinodes(pair[0], pair[1])

            antinodes.add(node_1)
            antinodes.add(node_2)
    return antinodes

def all_antinodes_on_map(city_map) -> list[Coordinate]:
    antenna_locations = get_antenna_locations(city_map)
    antinodes = find_all_antinodes(antenna_locations)
    x_max = len(city_map[0])
    y_max = len(city_map)
    antinodes_on_map = []
    for antinode in antinodes:
        if antinode.x < 0 or antinode.y < 0:
            continue
        if antinode.x >= x_max or antinode.y >= y_max:
            continue
        antinodes_on_map.append(antinode)
    return antinodes_on_map

def find_all_antinode_diagonals(antenna_locations: dict) -> dict:
    diagonals = defaultdict(set)
    for key in antenna_locations.keys():
        antennas = antenna_locations[key]
        antenna_pairs = get_antenna_pairs(antennas)
        for pair in antenna_pairs:
            dx = pair[1].x - pair[0].x
            dy = pair[1].y - pair[0].y
            diagonals[pair[0]].add((dx, dy))
    return diagonals

def find_all_antinodes_on_map_with_harmonics(city_map) -> list[Coordinate]:
    print("Finding all antennas...")
    antenna_locations = get_antenna_locations(city_map)
    print("Finding all diagonals...")
    diagonals = find_all_antinode_diagonals(antenna_locations)
    print("Finding all antinodes...")
    antinodes_on_map = find_all_antinodes_on_diagonals(diagonals, len(city_map[0]), len(city_map))
    return antinodes_on_map

def find_all_antinodes_on_diagonals(diagonals: dict, x_max: int, y_max: int) -> set[Coordinate]:
    antinodes = set()
    for antenna in diagonals.keys():
        antinodes.add(antenna)
        for dx, dy in diagonals[antenna]:
            within_bounds=True
            x = antenna.x
            y = antenna.y
            while within_bounds:
                x -= dx
                y -= dy
                if x < 0 or y < 0 or x >= x_max or y >= y_max:
                    within_bounds = False
                else:
                    antinodes.add(Coordinate(x, y))

            within_bounds=True
            x = antenna.x
            y = antenna.y
            while within_bounds:
                x += dx
                y += dy
                if x < 0 or y < 0 or x >= x_max or y >= y_max:
                    within_bounds = False
                else:
                    antinodes.add(Coordinate(x, y))
    return antinodes


def part_one(filepath="./inputs/08.txt") -> int:
    city_map = parse_map(filepath)
    antinodes = all_antinodes_on_map(city_map)
    return  len(antinodes)

def part_two(filepath="./inputs/08.txt") -> int:
    city_map = parse_map(filepath)
    antinodes = find_all_antinodes_on_map_with_harmonics(city_map)
    return  len(antinodes)