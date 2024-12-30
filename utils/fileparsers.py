from utils.grids import ArrayGrid


def parse_map(filepath: str) -> list[list[str]]:
    with open(filepath, 'r') as f:
        line = f.readline()
        rows = []
        while line:
            row = line.strip()
            rows.append(list(row))
            line = f.readline()
    return rows


def parse_arraygrid(filepath: str) -> ArrayGrid:
    map = parse_map(filepath)
    return ArrayGrid(map)


def parse_int_map(filepath: str) -> list[list[int]]:
    with open(filepath, 'r') as f:
        line = f.readline()
        rows = []
        while line:
            row = line.strip()
            row = [int(value) for value in list(row)]
            rows.append(row)
            line = f.readline()
    return rows


def parse_int_arraygrid(filepath: str) -> ArrayGrid:
    map = parse_int_map(filepath)
    return ArrayGrid(map)

def parse_string(filepath: str) -> str:
    with open(filepath, 'r') as f:
        line = f.readline()
        result = ""
        while line:
            result += line.strip('\n')
            line = f.readline()
    return result
