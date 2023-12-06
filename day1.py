import os
import sys
import re


def parse(file_path):
    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    values = []
    with open(file_path) as f:
        for line in f.readlines():
            matches = re.findall(r"\d", line)
            values.append(int(matches[0] + matches[-1]))
    return values


def part1(data):
    return sum(data)


def part2(file_path):
    if not os.path.exists(file_path):
        sys.exit("File does not exist")
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    backward_numbers = {
        "eno": "1",
        "owt": "2",
        "eerht": "3",
        "ruof": "4",
        "evif": "5",
        "xis": "6",
        "neves": "7",
        "thgie": "8",
        "enin": "9",
    }
    values = []
    with open(file_path) as f:
        for line in f.readlines():
            result = ""
            forward_matches = re.findall(
                r"one|two|three|four|five|six|seven|eight|nine|\d",
                line,
            )
            if not forward_matches[0].isnumeric():
                result += numbers[forward_matches[0]]
            else:
                result += forward_matches[0]
            backward_matches = re.findall(
                r"eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d",
                line[::-1],
            )
            if not backward_matches[0].isnumeric():
                result += backward_numbers[backward_matches[0]]
            else:
                result += backward_matches[0]
            print(f"{line}\tResult: {result} ---- Length: {len(result)}")
            if len(result) != 2:
                break
            values.append(int(result))
    print(values)
    print(sum(values))


if __name__ == "__main__":
    # parse("sample.txt")
    # print(part1(parse("data.txt")))
    part2("data.txt")
