from scripts.day12 import *


def test_create_farm_plots():
    farm = [
        ["A", "A", "A", "A"],
        ["B", "B", "C", "E"],
        ["B", "B", "C", "C"],
        ["E", "E", "E", "C"]
    ]
    farm_plots = create_farm_plots(farm)

    expected_plots = [
        [Plot(0, 0, "A", 3), Plot(1, 0, 'A', 2), Plot(2, 0, 'A', 2), Plot(3, 0, 'A', 3)],
        [Plot(0, 1, 'B', 2), Plot(1, 1, 'B', 2), Plot(2, 1, 'C', 3), Plot(3, 1, 'E', 4)],
        [Plot(0, 2, 'B', 2), Plot(1, 2, 'B', 2), Plot(2, 2, 'C', 2), Plot(3, 2, 'C', 2)],
        [Plot(0, 3, 'E', 3), Plot(1, 3, 'E', 2), Plot(2, 3, 'E', 3), Plot(3, 3, 'C', 3)]
    ]
    assert farm_plots == expected_plots


def test_get_region():
    farm_plots = [
        [Plot(0, 0, "A", 3), Plot(1, 0, 'A', 2), Plot(2, 0, 'A', 2), Plot(3, 0, 'A', 3)],
        [Plot(0, 1, 'B', 2), Plot(1, 1, 'B', 2), Plot(2, 1, 'C', 3), Plot(3, 1, 'E', 4)],
        [Plot(0, 2, 'B', 2), Plot(1, 2, 'B', 2), Plot(2, 2, 'C', 2), Plot(3, 2, 'C', 2)],
        [Plot(0, 3, 'E', 3), Plot(1, 3, 'E', 2), Plot(2, 3, 'E', 3), Plot(3, 3, 'C', 3)]
    ]
    region_A = get_region(farm_plots, [Plot(0, 0, "A", 3)])
    assert set(region_A) == {Plot(0, 0, "A", 3), Plot(1, 0, 'A', 2), Plot(2, 0, 'A', 2), Plot(3, 0, 'A', 3)}

    region_C = get_region(farm_plots, [Plot(2, 1, 'C', 3)])
    assert set(region_C) == {Plot(2, 1, 'C', 3),Plot(2, 2, 'C', 2), Plot(3, 2, 'C', 2), Plot(3, 3, 'C', 3) }

def test_find_regions():
    farm_plots = [
        [Plot(0, 0, "A", 3), Plot(1, 0, 'A', 2), Plot(2, 0, 'A', 2), Plot(3, 0, 'A', 3)],
        [Plot(0, 1, 'B', 2), Plot(1, 1, 'B', 2), Plot(2, 1, 'C', 3), Plot(3, 1, 'E', 4)],
        [Plot(0, 2, 'B', 2), Plot(1, 2, 'B', 2), Plot(2, 2, 'C', 2), Plot(3, 2, 'C', 2)],
        [Plot(0, 3, 'E', 3), Plot(1, 3, 'E', 2), Plot(2, 3, 'E', 3), Plot(3, 3, 'C', 3)]
    ]
    regions = find_regions(farm_plots)
    assert len(regions) == 5

def test_calculate_price():
    region_A =  {Plot(0, 0, "A", 3), Plot(1, 0, 'A', 2), Plot(2, 0, 'A', 2), Plot(3, 0, 'A', 3)}
    price = calculate_price(region_A)
    assert price == 40

    region_C = {Plot(2, 1, 'C', 3),Plot(2, 2, 'C', 2), Plot(3, 2, 'C', 2)}
    price = calculate_price(region_C)
    assert price == 21

def test_part_one():
    assert part_one("./inputs/12_XO_test.txt") == 772
    assert part_one("./inputs/12_test.txt") == 1930
