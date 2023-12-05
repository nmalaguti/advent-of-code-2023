from stdlib import *  # noqa


def border(start, end):
    y1, x1 = start
    y2, x2 = end

    assert y1 == y2
    for x in range(x1 - 1, x2 + 2):
        yield y1 - 1, x
    yield y1, x1 - 1
    yield y1, x2 + 1
    for x in range(x1 - 1, x2 + 2):
        yield y1 + 1, x


def get_number(schematic, coord):
    y, x = coord
    while schematic[(y, x - 1)] is not None and schematic[(y, x - 1)] in "0123456789":
        x -= 1

    start = x

    digits = []
    while schematic[(y, x)] is not None and schematic[(y, x)] in "0123456789":
        digits.append(schematic[(y, x)])
        x += 1

    end = x

    return start, end, int("".join(digits))


def find_adjacent_symbol(schematic, start, end):
    """start and end are inclusive"""
    for coord in border(start, end):
        sym = schematic[coord]
        if sym is not None and sym not in "0123456789.":
            return coord

    return None


def make_schematic(lines):
    schematic = defaultdict(lambda: None)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            schematic[(y, x)] = char
    return schematic


def part_1(lines: list[str]):
    schematic = make_schematic(lines)
    part_numbers = []
    for y, line in enumerate(lines):
        line_numbers = []
        x = -1
        for number in positive_ints(line):
            str_num = str(number)
            x = line.index(str_num, x + 1)
            coord = find_adjacent_symbol(schematic, (y, x), (y, x + len(str_num) - 1))
            if coord is not None:
                line_numbers.append(number)
            x += len(str(number))
        part_numbers.append(line_numbers)

    return sum(flatten(part_numbers))


def part_2(lines: list[str]):
    schematic = make_schematic(lines)
    gears = defaultdict(list)
    for y, line in enumerate(lines):
        x = -1
        for number in positive_ints(line):
            str_num = str(number)
            x = line.index(str_num, x + 1)
            coord = find_adjacent_symbol(schematic, (y, x), (y, x + len(str_num) - 1))
            if schematic[coord] == "*":
                gears[coord].append(number)
            x += len(str(number))

    total = 0
    for coord, part_numbers in gears.items():
        if len(part_numbers) == 2:
            a, b = part_numbers
            total += a * b

    return total


def part_2_alt(lines: list[str]):
    schematic = make_schematic(lines)
    potential_gears = []
    for coord, sym in schematic.items():
        if sym == "*":
            potential_gears.append(coord)

    seen = set()
    gears = []
    for coord in potential_gears:
        numbers = []
        for b in border(coord, coord):
            if schematic[b] in "0123456789" and b not in seen:
                start, end, number = get_number(schematic, b)
                numbers.append(number)
                for x in range(start, end):
                    seen.add((b[0], x))
        if len(numbers) == 2:
            gears.append(numbers)

    debug(sorted([sorted(coord) for coord in gears]))
    debug(len(gears))
    return sum(a * b for a, b in gears)


if __name__ == "__main__":
    DEBUG.false()
    EXAMPLE.false()

    input_lines = read_input()
    print("Part 1:", part_1(input_lines) or "")
    print("Part 2:", part_2(input_lines) or "")
    print("Part 2:", part_2_alt(input_lines) or "")
