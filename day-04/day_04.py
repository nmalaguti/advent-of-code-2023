from stdlib import *  # noqa


def card_points(winning_numbers, my_numbers):
    matches = len(set(winning_numbers).intersection(my_numbers))
    if matches > 0:
        return 2 ** (matches - 1)
    return 0


def part_1(lines: list[str]):
    total = 0
    for line in lines:
        card, numbers = line.split(":")
        winning_numbers, my_numbers = map(ints, numbers.split("|"))
        total += card_points(winning_numbers, my_numbers)

    return total


def part_2(lines: list[str]):
    card_stack = deque()
    card_dict = {}

    for line in lines:
        card, numbers = line.split(":")
        card_number = ints(card)[0]
        winning_numbers, my_numbers = map(ints, numbers.split("|"))
        matches = len(set(winning_numbers).intersection(my_numbers))
        card_stack.append((card_number, matches))
        card_dict[card_number] = (card_number, matches)

    total = 0

    while card_stack:
        total += 1
        card_number, matches = card_stack.popleft()
        for i in range(matches):
            card_stack.append(card_dict[card_number + i + 1])

    return total


if __name__ == "__main__":
    DEBUG.true()
    EXAMPLE.false()

    input_lines = read_input()
    print("Part 1:", part_1(input_lines) or "")
    print("Part 2:", part_2(input_lines) or "")
