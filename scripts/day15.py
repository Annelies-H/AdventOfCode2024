from utils.fileparsers import parse_string, parse_arraygrid
from utils.grids import Direction, Coordinate

class Warehouse:

    def __init__(self, grid, moves):
        self.grid = grid
        self.moves = moves

        self.robot = self.grid.locate_values("@")[0]
        grid.set_cell(self.robot, '.')

    def move_direction(self, direction):
        next_location = self.grid.travel_in_direction(self.robot, direction)
        value_next_location = self.grid.get_cell(next_location)
        if value_next_location == "#":
            # can't move because wall
            return
        if value_next_location == ".":
            # safe to move, no boxes in the way
            self.robot = next_location
            return

        locations = [next_location]

        while value_next_location == "O":
            next_location = self.grid.travel_in_direction(next_location, direction)
            value_next_location = self.grid.get_cell(next_location)
            if value_next_location == "#":
                return
            locations.append(next_location)

        self.robot = locations[0]
        self.grid.set_cell(locations[0], ".")
        self.grid.set_cell(locations[-1], "O")

    def move_all(self):
        for direction in self.moves:
            self.move_direction(direction)

    def sum_gps_coordinates(self):
        boxes = self.grid.locate_values("O")
        gps_total = 0
        for box in boxes:
            gps_total += 100 * box.y + box.x
        return gps_total


    def print(self):
        self.grid.set_cell(self.robot, "@")
        self.grid.print()
        self.grid.set_cell(self.robot, ".")






def parse_movement(filepath):
    mapping = {
        "^": Direction.N,
        ">": Direction.E,
        "v": Direction.S,
        "<": Direction.W,
    }

    input = parse_string(filepath)
    moves = []
    for move in input:
        moves.append(mapping[move])
    return moves

def parse_warehouse(filepath_a, filepath_b):
    grid = parse_arraygrid(filepath_a)
    grid.print()

    moves = parse_movement(filepath_b)

    return Warehouse(grid, moves)


def part_one(filepath_a="./inputs/15a.txt", filepath_b="./inputs/15b.txt"):
    warehouse = parse_warehouse(filepath_a, filepath_b)
    warehouse.move_all()
    warehouse.print()
    gps_total = warehouse.sum_gps_coordinates()

    return gps_total


