from utils.parse_input import parse_input


def calculate(input):
    valid = [n for i, n in enumerate(input[1:]) if n > input[i]]
    return valid


if __name__ == '__main__':
    input = parse_input()
    input = [int(n) for n in input]
    result = len(calculate(input))
    print("Part 1 result", result)
    input2 = [n + input[i] + input[i + 1] for i, n in enumerate(input[2:])]
    result = len(calculate(input2))
    print("Part 2 result", result)
