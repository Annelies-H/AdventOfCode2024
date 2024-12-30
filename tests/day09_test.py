from scripts.day09 import *


def test_get_file_blocks_from_file():
    file_blocks, file_id = file_blocks_from_map("12345")
    assert file_blocks == [
        0, '.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2
    ]


def test_move_file_blocks():
    file_blocks = [0, '.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]
    compacted_disk = move_file_blocks(file_blocks)
    assert compacted_disk == [0, 2, 2, 1, 1, 1, 2, 2, 2]

def test_check_sum():
    compacted_disk = [0, 2, 2, 1, 1, 1, 2, 2, 2]
    check_sum = calculate_check_sum(compacted_disk)
    assert check_sum == 60

def test_part_one():
    assert part_one("./inputs/09_test.txt") == 1928



def test_complete_file_blocks_from_disk_map():
    file_blocks, max_file_id = complete_file_blocks_from_map("12345")
    assert file_blocks == [[0], [".", "."], [1, 1, 1], [".",".",".","."], [2,2,2,2,2]]
    assert max_file_id == 2

def test_defragment_disk():
    file_blocks = [[0], [".", "."], [1, 1, 1], [".", ".", ".", "."], [2, 2, 2, 2, 2]]
    defragmented_disk = defragment_disk(file_blocks, 2)
    assert defragmented_disk == file_blocks

    file_blocks = [[0, 0], [".", ".", "."], [1], [".", ".", ".", "."], [2], ["."] ,[3, 3, 3,]]
    defragmented_disk = defragment_disk(file_blocks, 3)
    assert defragmented_disk ==  [
        [0, 0],
        [3, 3, 3],
        [1],
        [2],
        ['.', '.', ".", ".", ".", ".", ".", "."]
        ]

    file_blocks = [
        [0,0],
        ['.','.','.'],
        [1,1,1],
        ['.', '.', ".",],
        [2],
        ['.', '.', ".",],
        [3,3,3],
        ['.'],
        [4,4],
        ['.'],
        [5,5,5,5],
        ['.'],
        [6,6,6,6],
        ['.'],
        [7,7,7],
        ['.'],
        [8,8,8,8],
        [9,9]
    ]
    defragmented_disk = defragment_disk(file_blocks, 9)
    assert defragmented_disk == [
        [0,0],
        [9, 9],
        [2],
        [1, 1, 1],
        [7, 7, 7],
        ['.'],
        [4, 4],
        ['.'],
        [3, 3, 3],
        ['.', '.', ".", '.'],
        [5, 5, 5, 5],
        ['.'],
        [6, 6, 6, 6],
        ['.', '.', ".", '.','.'],
        [8, 8, 8, 8],
        ['.', '.',]
         ]

def test_get_empty_index():
    file_blocks = [[0, 0], [".", ".", "."], [1], [".", ".", ".", "."], [2], ["."], [3, 3, 3, ]]
    file_size = 3
    file_index = 6
    empty_index = get_empty_index(file_blocks, file_size, file_index)
    assert empty_index == 1

    file_blocks = [[0, 0], [".", "."], [1], [".", ".", ".", "."], [2], ["."], [3, 3, 3, ]]
    file_size = 3
    file_index = 6
    empty_index = get_empty_index(file_blocks, file_size, file_index)
    assert empty_index == 3

def test_file_index():
    file_blocks =  [[0, 0], [".", ".", "."], [1], [".", ".", ".", "."], [2], ["."] ,[3, 3, 3,]]
    file_id = 3
    previous_index = len(file_blocks) - 1

    index = get_file_index(file_blocks, file_id, previous_index)
    assert index == 6

    file_blocks = [[0, 0], [3, 3, 3], [1], ['.', '.', '.', '.'], [2], ['.', '.', '.', '.']]
    file_id = 2
    previous_index = len(file_blocks) - 1

    index = get_file_index(file_blocks, file_id, previous_index)
    assert index == 4

def test_insert_file():
    file_blocks = [[2], ["."] ,[3, 3, 3,]]
    file = [4]
    empty_index = 1
    blocks = insert_file(file_blocks, file, empty_index)
    assert blocks == [[2], [4] ,[3, 3, 3,]]

    file_blocks = [[2], [".", ".", "."] ,[3, 3, 3,]]
    file = [4]
    empty_index = 1
    blocks = insert_file(file_blocks, file, empty_index)
    assert blocks == [[2], [4,] , [".", "."], [3, 3, 3,]]


def test_remove_file():
    file_blocks = [[2], ["."] ,[3, 3, 3,]]
    index = 2
    required_space = 3
    blocks = remove_file(file_blocks, index, required_space)
    assert blocks == [[2], [".",".",".",".",]]

    file_blocks = [[0, 0], [".", "."], [1], [".", ".", ".", "."], [2], ["."] ,[3, 3, 3,]]
    index = 2
    required_space = 1
    blocks = remove_file(file_blocks, index, required_space)
    assert blocks == [[0, 0], [".", ".", ".", ".", ".", ".", "."], [2], ["."] ,[3, 3, 3,]]

    file_blocks = [[2], [1], [3, 3, 3, ]]
    index = 2
    required_space = 3
    blocks = remove_file(file_blocks, index, required_space)
    assert blocks == [[2], [1], [".", ".", ".", ]]

def test_part_two():
    assert part_two("./inputs/09_test.txt") == 2858