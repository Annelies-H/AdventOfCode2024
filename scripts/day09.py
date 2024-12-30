from utils.fileparsers import parse_string

def file_blocks_from_map(disk_map: str) -> tuple[list[int, str], int]:
    file_blocks = []
    file_id = 0
    for i in range(0, len(disk_map), 2):
        for j in range(0, int(disk_map[i])):
            file_blocks.append(file_id)

        if i +1 == len(disk_map):
            break
        for j in range(0, int(disk_map[i+1])):
            file_blocks.append('.')
        file_id += 1
    return file_blocks, file_id


def move_file_blocks(file_blocks: list[int, str]) -> list[int]:
    first_empty = 0
    while True:
        last_value = file_blocks.pop()
        if last_value == ".":
            continue

        first_empty = first_empty_index(file_blocks, first_empty)
        if first_empty == -1:
            # no more empty spaces
            file_blocks.append(last_value)
            break

        file_blocks[first_empty] = last_value

    return file_blocks

def first_empty_index(file_blocks: list[int, str], start: int) -> int:
    for i in range (start, len(file_blocks)):
        if file_blocks[i] == ".":
            return i
    return -1

def calculate_check_sum(compacted_disk: list[int]) -> int:
    checksum = 0
    for index, file_id in enumerate(compacted_disk):
        if file_id == ".":
            continue
        checksum += index * int(file_id)
    return checksum


def complete_file_blocks_from_map(disk_map: str) -> tuple[str, int]:
    file_blocks = []
    file_id = -1
    for i in range(0, len(disk_map), 2):
        file_id += 1
        file_size = int(disk_map[i])
        new_block = []
        for j in range(0, file_size):
            new_block.append(file_id)
        file_blocks.append(new_block)
        if i +1 == len(disk_map):
            break

        empty_size = int(disk_map[i+1])
        empty_block = []
        for j in range(0, empty_size):
            empty_block.append('.')
        file_blocks.append(empty_block)

    return file_blocks, file_id

def defragment_disk(file_blocks: list[int, str], file_id) -> list[int, str]:
    index = len(file_blocks) -1

    while file_id > 0:
        file_blocks, file_id, index = _defragment_disk(file_blocks, file_id, index)

    return file_blocks


def _defragment_disk(file_blocks: list[int, str], file_id: int, previous_index: int) -> list[int, str]:
    if file_id < 0:
        return file_blocks
    file_index = get_file_index(file_blocks, file_id, previous_index)
    file = file_blocks[file_index]
    empty_index = get_empty_index(file_blocks, len(file), file_index)
    if empty_index:
        file_blocks = remove_file(file_blocks, file_index, len(file))
        file_blocks = insert_file(file_blocks, file, empty_index)
    index =  min(file_index, len(file_blocks) -1)
    return file_blocks, file_id-1, index


def insert_file(file_blocks, file, empty_index):
    empty_space = file_blocks[empty_index]
    file_blocks[empty_index] = file
    extra_space = len(empty_space) - len(file)
    if extra_space:
        empty_block = []
        for i in range(0, extra_space):
            empty_block.append('.')
        file_blocks.insert(empty_index + 1, empty_block)
    return file_blocks

def remove_file(file_blocks, file_index, size):
    previous_space = file_blocks[file_index - 1]
    if '.' in previous_space:
        size += len(previous_space)
        file_index += -1
        file_blocks.pop(file_index)

    if file_index < (len(file_blocks) -1) and '.' in (next_space := file_blocks[file_index + 1]):
        size += len(next_space)
        file_blocks.pop(file_index + 1)

    empty_block = []
    for i in range(0, size):
        empty_block.append('.')
    file_blocks[file_index] = empty_block
    return file_blocks

def get_file_index(file_blocks, file_id, previous_index):
    for i in range(previous_index, -1, -1):
        if file_id in file_blocks[i]:
            return i

def get_empty_index(file_blocks, required_space, file_index):
    for i in range(0, file_index):
        block = file_blocks[i]
        if not '.' in block:
            continue
        if len(block) >= required_space:
            return i
    return 0

def file_blocks_to_string(file_blocks) -> str:
    disk = ""
    for block in file_blocks:
        disk += block
    return disk


def part_one(filepath="./inputs/09.txt") -> int:
    disk_map = parse_string(filepath)
    file_blocks, _ = file_blocks_from_map(disk_map)
    compacted_disk = move_file_blocks(file_blocks)
    check_sum = calculate_check_sum(compacted_disk)
    return check_sum

def part_two(filepath="./inputs/09.txt") -> int:
    disk_map = parse_string(filepath)
    file_blocks, max_file_id = complete_file_blocks_from_map(disk_map)
    compacted_disk = defragment_disk(file_blocks, max_file_id)
    disk = []
    for block in compacted_disk:
        disk.extend(block)

    check_sum = calculate_check_sum(disk)
    return check_sum