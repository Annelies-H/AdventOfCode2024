def parse_file(filepath: str) ->list[list[str]]:
    lab_map = []
    with open(filepath, 'r') as f:
        line = f.readline()
        while line:
            row = list(line)
            if row[-1] == "\n":
                row.pop(-1)
            lab_map.append(row)
            line = f.readline()
    return lab_map


class Guard():

    def __init__(self, lab_map):
        self.lab_map = lab_map
        self.x_max = len(lab_map[0])
        self.y_max = len(lab_map)
        self.x = None
        self.y = None
        self.direction = None
        self.locate()
        self.visited_locations = []
        self.initial_x = self.x
        self.initial_y = self.y



    def locate(self):
        for y, row in enumerate(self.lab_map):
            for x, location in enumerate(row):
                if location == "^":
                    self.x = x
                    self.y = y
                    self.direction = "UP"

    def location_ahead(self):
        if self.direction == "UP":
            return self.x, self.y - 1
        if self.direction == "RIGHT":
            return self.x + 1, self.y
        if self.direction == "DOWN":
            return self.x, self.y + 1
        if self.direction == "LEFT":
            return self.x - 1, self.y

    def check_ahead(self):
        x, y = self.location_ahead()
        if x in [-1, self.x_max] or y in [-1, self.y_max]:
            return "EDGE"
        location_ahead = self.lab_map[y][x]
        if location_ahead == "#":
            return "OBSTACLE"
        return "EMPTY"

    def turn(self):
        if self.direction == "UP":
            self.direction = "RIGHT"
        elif self.direction == "RIGHT":
            self.direction = "DOWN"
        elif self.direction == "DOWN":
            self.direction = "LEFT"
        elif self.direction == "LEFT":
            self.direction = "UP"

    def walk(self):
        if self.direction == "UP":
            self.y += -1
        elif self.direction == "RIGHT":
            self.x += 1
        elif self.direction == "DOWN":
            self.y += 1
        elif self.direction == "LEFT":
            self.x += -1

    def patrol_map(self):
        on_map = True
        while on_map:
            self.lab_map[self.y][self.x] = "X"
            current = self.x, self.y, self.direction
            if current in self.visited_locations:
                return "LOOPED!"
            self.visited_locations.append(current)
            ahead = self.check_ahead()
            if ahead == "EMPTY":
                self.walk()
            elif ahead == "OBSTACLE":
                self.turn()
            elif ahead == "EDGE":
                on_map = False
            else:
                raise Exception("Guard has no idea what to do")
        return "LEFT MAP!"

    def total_visited_positions(self) -> int:
        total = 0
        for row in self.lab_map:
            total += len(["X" for location in row if location == "X"])
        return total

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.direction = "UP"
        self.visited_locations = []

def part_one(filepath="./inputs/06.txt") -> int:
    original_map = parse_file(filepath)
    guard = Guard(original_map)
    guard.patrol_map()
    return guard.total_visited_positions()


def part_two(filepath="./inputs/06.txt") -> int:
    lab_map = parse_file(filepath)
    guard = Guard(lab_map)

    # find all location the guard passes on his route
    # it takes way to long to check all spots on the map
    guard.patrol_map()
    visited_locations = guard.visited_locations
    on_route = set()
    for location in visited_locations:
        on_route.add((location[0], location[1])) # (x, y)
    on_route = list(on_route)
    guard.reset()

    # for each location the guard passes place an obstacle and check if it loops
    total = 0
    for coordinate in on_route:
        y = coordinate[1]
        x = coordinate[0]
        lab_map[y][x] = "#"
        guard.map = lab_map
        status = guard.patrol_map()
        print(f"{y},{x}{status}")
        if status == "LOOPED!":
            total += 1
        lab_map[y][x] = "."
        guard.reset()

    return total
