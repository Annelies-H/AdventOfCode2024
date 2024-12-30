from scripts.day05 import *


def test_parse_file():
    rules, pages = parse_file("./inputs/05_test.txt")

    assert len(pages) == 6
    assert pages[0] == ['75', '47', '61', '53', '29']

    assert set(rules.keys()) == set(['47', '97', '75', '61', '29', '53'])
    assert rules["53"] == ["29", "13"]

def test_has_correct_order():
    pages = ["75", "29", "13"]
    rules = {
        "75": ["29", "13", "43"],
        "29": ["13"],
    }

    assert has_correct_order(rules, pages)


def test_part_one():
    assert part_one("./inputs/05_test.txt") == 143


def test_correct_page_order_in_small_update():
    update = ["61", "13", "29"]
    rules = {
        "61": ["13"],
        "29": ["13"]
    }
    assert correct_update_only_small_test_data(rules, update) == ["61", "29", "13"]


def test_correct_page_order_in_update():
    update = ["61", "13", "29"]
    rules = {
        "61": ["13"],
        "29": ["13"]
    }
    assert correct_update(rules, update) == ["61", "29", "13"]

def test_part_two():
    assert part_two("./inputs/05_test.txt") == 123

