

def parse_file(filepath: str) -> list[list[int]]:
    with open(filepath, 'r') as f:
        line = f.readline()
        reports = []
        while line:
            report = line.split()
            report = [int(value) for value in report]
            reports.append(report)
            line = f.readline()
    return reports

def count_safe_reports(reports: list[list[int]]) -> int:
    safe_reports = []
    for report in reports:
        if is_safe_report(report):
            safe_reports.append(report)
    return len(safe_reports)

def count_safe_reports_with_dampener(reports: list[list[int]]) -> int:
    safe_reports = []
    for report in reports:
        if is_safe_report_with_dampener(report):
            safe_reports.append(report)
    return len(safe_reports)

def is_safe_report_with_dampener(report):
    if is_safe_report(report):
        return True
    for index in range(0, len(report)):
        modified_report = report.copy()
        modified_report.pop(index)
        if is_safe_report(modified_report):
            return True,
    return False


def is_safe_report(report: list[int], dampener=True) -> bool:
    if report[0] > report[1] and is_safe_descending(report):
        return True
    elif report[0] < report[1] and is_safe_ascending(report):
        return True
    return False

def is_safe_descending(report: list[int]) -> bool:
    for index, value in enumerate(report):
        if index == 0:
            continue
        difference = report[index-1] - value
        if difference not in [1, 2, 3]:
            return False
    return True

def is_safe_ascending(report: list[int], dampener=0) -> bool:
    for index, value in enumerate(report):
        if index == 0:
            continue
        difference = value - report[index-1]
        if difference not in [1, 2, 3]:
            return False
    return True

def part_one(filepath="./inputs/02.txt") -> int:
    reports = parse_file(filepath)
    safe_reports_count = count_safe_reports(reports)
    return safe_reports_count

def part_two(filepath="./inputs/02.txt") -> int:
    reports = parse_file(filepath)
    safe_reports_count = count_safe_reports_with_dampener(reports)
    return safe_reports_count