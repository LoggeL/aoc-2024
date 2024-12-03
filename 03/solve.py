import re


def solve1(lines):
    result = 0
    for line in lines:
        # mul(8,5)
        mul_RE = re.compile(r"mul\((\d+),(\d+)\)")
        for match in mul_RE.finditer(line):
            a = int(match.group(1))
            b = int(match.group(2))
            result += a * b

    return result


def solve2(lines):
    result = 0
    lines = ["".join(lines)]  # hehe
    for line in lines:
        positive_parts = line.split("do()")
        for positive_part in positive_parts:
            positive_part = positive_part.split("don't()")[0]

            # mul(8,5)
            mul_RE = re.compile(r"mul\((\d+),(\d+)\)")
            for match in mul_RE.finditer(positive_part):
                a = int(match.group(1))
                b = int(match.group(2))
                result += a * b

    return result

    pass


if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if len(test2) == 0:
        test2 = test1

    test1_solution = 161
    test2_solution = 48

    test1_result = solve1(test1)
    test2_result = solve2(test2)

    print("Test 1: " + str(test1_result))
    if test1_solution != test1_result:
        print("Test 1 failed!")
        exit(1)

    print("Solution 1: " + str(solve1(input)))

    print("Test 2: " + str(test2_result))
    if test2_solution != test2_result:
        print("Test 2 failed!")
        exit(1)

    print("Solution 2: " + str(solve2(input)))
