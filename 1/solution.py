from utils.parse_input import parse_input


def check_condition(num, prev_num):
    if int(num) > int(prev_num):
        return True
    return False


if __name__ == '__main__':
    input = parse_input()
    valid = [n for i, n in enumerate(input[1:]) if check_condition(n, input[i])]
    print(len(valid))