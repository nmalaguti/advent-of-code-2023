from stdlib import *  # noqa

RED = "red"
GREEN = "green"
BLUE = "blue"

CUBE_COLORS = [RED, GREEN, BLUE]


def parse_handful(handful):
    colors = handful.split(",")
    result = {}
    for color in colors:
        for cube_color in CUBE_COLORS:
            if cube_color in color:
                result[cube_color] = ints(color)[0]
    return result


def part_1(lines):
    max_cubes = {RED: 12, GREEN: 13, BLUE: 14}

    total = 0
    for line in lines:
        game, results = line.split(":")
        game_id = ints(game)[0]
        handfuls = [parse_handful(handful) for handful in results.split(";")]
        impossible = False
        for handful in handfuls:
            for cube_color in CUBE_COLORS:
                if handful.get(cube_color, 0) > max_cubes[cube_color]:
                    impossible = True

        if not impossible:
            total += game_id

    return total


def part_2(lines):
    total = 0
    for line in lines:
        game, results = line.split(":")
        handfuls = [parse_handful(handful) for handful in results.split(";")]
        maxes = defaultdict(lambda: 0)
        for handful in handfuls:
            for cube_color in CUBE_COLORS:
                maxes[cube_color] = max(maxes[cube_color], handful.get(cube_color, 0))

        power = 1
        for cube_color in CUBE_COLORS:
            power *= maxes[cube_color]

        total += power

    return total


if __name__ == "__main__":
    DEBUG.true()
    EXAMPLE.false()

    input_lines = read_input()
    print("Part 1:", part_1(input_lines) or "")
    print("Part 2:", part_2(input_lines) or "")
