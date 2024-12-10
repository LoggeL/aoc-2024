def solve1(lines):
    map = []
    for line in lines:
        map.append(list(line))

    # int parse
    for y in range(len(map)):
        for x in range(len(map[y])):
            map[y][x] = int(map[y][x])

    def move_path(idx, pos):
        y, x = pos

        if idx == 9:
            return [pos]

        result = []
        # check 4 directions
        if y > 0 and map[y - 1][x] == idx + 1:
            result += move_path(idx + 1, (y - 1, x))
        if y < len(map) - 1 and map[y + 1][x] == idx + 1:
            result += move_path(idx + 1, (y + 1, x))
        if x > 0 and map[y][x - 1] == idx + 1:
            result += move_path(idx + 1, (y, x - 1))
        if x < len(map[y]) - 1 and map[y][x + 1] == idx + 1:
            result += move_path(idx + 1, (y, x + 1))

        return result

    result = 0
    # find 0s
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                final_points = move_path(0, (y, x))
                # print(y, x, final_points)
                result += len(set(final_points))

    return result


def solve2(lines):
    map = []
    for line in lines:
        map.append(list(line))

    # int parse
    for y in range(len(map)):
        for x in range(len(map[y])):
            map[y][x] = int(map[y][x])

    def move_path(idx, pos):
        y, x = pos

        if idx == 9:
            return [pos]

        result = []
        # check 4 directions
        if y > 0 and map[y - 1][x] == idx + 1:
            result += move_path(idx + 1, (y - 1, x))
        if y < len(map) - 1 and map[y + 1][x] == idx + 1:
            result += move_path(idx + 1, (y + 1, x))
        if x > 0 and map[y][x - 1] == idx + 1:
            result += move_path(idx + 1, (y, x - 1))
        if x < len(map[y]) - 1 and map[y][x + 1] == idx + 1:
            result += move_path(idx + 1, (y, x + 1))

        return result

    result = 0
    # find 0s
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                final_points = move_path(0, (y, x))
                # print(y, x, final_points)
                result += len(final_points)

    return result


if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 36
    test2_solution = 81

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
