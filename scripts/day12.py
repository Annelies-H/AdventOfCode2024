from collections import namedtuple
from utils.fileparsers import parse_map

Plot = namedtuple("Plot", ["x", "y", "plant_type", "perimeter"])

def create_farm_plots(farm):
    farm_plots = []
    for y, row in enumerate(farm):
        plot_row = []
        for x, area in enumerate(row):
            plot = create_plot(farm, x, y)
            plot_row.append(plot)
        farm_plots.append(plot_row)
    return farm_plots

def create_plot(farm, x, y):
    plant_type = farm[y][x]
    perimeter = 0
    # up
    if y == 0:
        perimeter += 1
    elif farm[y-1][x] != plant_type:
        perimeter += 1
    # right
    if x == len(farm[0]) - 1:
        perimeter += 1
    elif farm[y][x+1] != plant_type:
        perimeter += 1
    #down
    if y == len(farm) -1:
        perimeter += 1
    elif farm[y+1][x] != plant_type:
        perimeter += 1
    # left
    if x == 0:
        perimeter += 1
    elif farm[y][x-1] != plant_type:
        perimeter += 1
    return Plot(x, y, plant_type, perimeter)

def find_regions(farm_plots):
    regions = []
    checked_plots = []
    for y, row in enumerate(farm_plots):
        for x, plot in enumerate(row):
            if plot in checked_plots:
                continue
            region = get_region(farm_plots, [plot])
            regions.append(region)
            checked_plots.extend(region)

    return regions

def get_region(farm_plots, plots, region=None):
    check_next = []
    if not region:
        region = []
    x_max = len(farm_plots[0]) - 1
    y_max = len(farm_plots) - 1

    for plot in plots:
        if plot in region:
            continue
        x = plot.x
        y = plot.y
        plant_type = plot.plant_type

        if y > 0 and (up := farm_plots[y-1][x]).plant_type == plant_type:
            check_next.append(up)
        if x < x_max and (right := farm_plots[y][x+1]).plant_type == plant_type:
            check_next.append(right)
        if y < y_max and (down := farm_plots[y+1][x]).plant_type == plant_type:
            check_next.append(down)
        if x > 0 and (left := farm_plots[y][x-1]).plant_type == plant_type:
            check_next.append(left)
        region.append(plot)

    if check_next:
        return get_region(farm_plots, check_next, region)
    else:
        return region

def calculate_price(region):
    area = len(region)
    perimeter = 0
    for plot in region:
        perimeter += plot.perimeter
    return area * perimeter

def total_fence_price(regions):
    total = 0
    for region in regions:
        total += calculate_price(region)
    return total

def part_one(filepath="./inputs/d12.txt"):
    farm = parse_map(filepath)
    farm_plots = create_farm_plots(farm)
    regions = find_regions(farm_plots)
    total = total_fence_price(regions)
    return total
