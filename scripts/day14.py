from utils.grids import Coordinate, Velocity, Grid


class Robot:

    def __init__(self, position, velocity, grid):
        self.position = position
        self.velocity = velocity
        self.grid = grid

    def move(self, repeat=1):
        for i in range(repeat):
            next_position = self.grid.next_position(self.position, self.velocity, wrap=True)
            self.position = next_position

def parse_robot(line, grid):
    line = line.strip()
    p_part, v_part = line.split(' ')

    p = p_part.removeprefix("p=")
    x, y = p.split(',')
    position = Coordinate(int(x), int(y))

    v = v_part.removeprefix("v=")
    dx, dy = v.split(',')
    velocity = Velocity(int(dx), int(dy))

    return Robot(position, velocity, grid)


def parse_robots(filepath, grid):
    with open(filepath, 'r') as f:
        line = f.readline()
        robots = []
        while line:
            robots.append(parse_robot(line, grid))
            line = f.readline()
    return robots

def move_robots(robots, seconds):
    for robot in robots:
        robot.move(seconds)

def get_quadrants(width, height):
    NW_min = Coordinate(0,0)
    NW_max = Coordinate(width//2-1, height//2-1)

    NE_min = Coordinate(width//2+1, 0)
    NE_max =  Coordinate(width-1, height//2-1)

    SW_min =  Coordinate(0, height//2+1)
    SW_max =  Coordinate(width//2-1, height-1)

    SE_min = Coordinate(width//2+1, height//2+1)
    SE_max = Coordinate(width -1, height -1)
    return [(NW_min, NW_max), (NE_min, NE_max), (SW_min, SW_max), (SE_min, SE_max)]

def safety_factor(robots, width, height):
    NW, NE, SW, SE = get_quadrants(width, height)
    total_NW = 0
    total_NE = 0
    total_SW = 0
    total_SE = 0

    for robot in robots:
        if robot.position.within_bounds(*NW):
            total_NW += 1
        elif robot.position.within_bounds(*NE):
            total_NE += 1
        elif robot.position.within_bounds(*SW):
            total_SW += 1
        elif robot.position.within_bounds(*SE):
            total_SE += 1
    return total_NW * total_NE * total_SW * total_SE

def part_one(filepath="./inputs/14.txt", width=101, height=103):
    grid = Grid(width, height)
    robots = parse_robots(filepath, grid)
    move_robots(robots, 100)
    sf = safety_factor(robots, width, height)
    return sf
