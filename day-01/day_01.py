import operator

from stdlib import *

NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for i in range(1, 10):
    NUMBERS[f"{i}"] = i


def extract_digits_part1(line) -> list[str]:
    return re.findall(r"\d", line)


def extract_digits_part2(line) -> list[int]:
    pattern = "|".join(NUMBERS.keys())
    # https://stackoverflow.com/a/5616910
    return [NUMBERS[num] for num in re.findall(f"(?=({pattern}))", line)]


def part_1(lines):
    return sum(
        int(f"{digits[0]}{digits[-1]}")
        for line in lines
        if (digits := extract_digits_part1(line))
    )


def part_2(lines):
    temp = [
        (line, digits, 10 * digits[0] + digits[-1])
        for line in lines
        if (digits := extract_digits_part2(line))
    ]
    if DEBUG:
        pprint(temp)

    return sum(map(operator.itemgetter(2), temp))


if __name__ == "__main__":
    DEBUG.false()
    EXAMPLE.false()

    assert extract_digits_part2("onetwothreefourfivesixsevenoneightnine123456789") == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        1,
        8,
        9,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ]

    input_lines = read_input()
    print("Part 1:", part_1(input_lines) or "")
    print("Part 2:", part_2(input_lines) or "")
