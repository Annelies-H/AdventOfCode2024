def parse_file(filepath: str) -> tuple[dict[str], list[str]]:
    rules = {}
    updates = []
    with open(filepath, 'r') as f:
        line = f.readline()
        while line:
            line = line.strip("\n")
            if "|" in line:
                first, next = line.split("|")
                after = rules.get(first, [])
                after.append(next)
                rules[first] = after
            elif line:
                updates.append(line.split(","))
            line = f.readline()
    return rules, updates


def sum_correct_middle_pages(rules: dict, updates: list) -> int:
    result = 0
    for pages in updates:
        if has_correct_order(rules, pages):
            middle_page_index = int(len(pages)/2)
            result += int(pages[middle_page_index])
    return result

def has_correct_order(rules, pages) -> bool:
    for index, page in enumerate(pages):
        page_rules = rules.get(page)
        if not page_rules:
            continue
        for previous_page in pages[:index]:
            if previous_page in page_rules:
                return False
    return True


def part_one(filepath="./inputs/05.txt") -> int:
    rules, updates= parse_file(filepath)
    result = sum_correct_middle_pages(rules, updates)

    return result

def part_two(filepath="./inputs/05.txt") -> int:
    rules, updates = parse_file(filepath)
    result = sum_corrected_middle_pages(rules, updates)

    return result

def sum_corrected_middle_pages(rules, updates) -> int:
    result = 0
    for update in updates:
        if has_correct_order(rules, update):
            continue #already correct
        print(update)
        corrected_update = correct_update(rules, update)
        middle_page_index = int(len(corrected_update) / 2)
        result += int(corrected_update[middle_page_index])
    return result

def correct_update(rules, update):
    latest_update = update
    while True:
        # use a trampoline to avoid recursion limit reached error
        if has_correct_order(rules, latest_update):
            return latest_update
        latest_update = _correct_update(rules, latest_update)



def _correct_update(rules, update):
    # very slow approach....
    # very very slow
    copy = update.copy()
    for index, page in enumerate(update):
        page_rules = rules.get(page, [])
        for previous_page in update[:index]:
            if previous_page in page_rules:
                copy.remove(previous_page)
                copy.insert(index, previous_page)
                return copy


def correct_update_only_small_test_data(rules, update) -> list[str]:
    if has_correct_order(rules, update):
        return update
    copy = update.copy()
    for index, page in enumerate(update):
        page_rules = rules.get(page, [])
        for previous_page in update[:index]:
            if previous_page in page_rules:
                copy.remove(previous_page)
                copy.insert(index, previous_page)
                return correct_update_only_small_test_data(rules, copy)


