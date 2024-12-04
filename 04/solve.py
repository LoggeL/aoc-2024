def solve1(lines):
    grid = []
    for line in lines:
        grid.append(list(line.strip()))

    search = ["X", "M", "A", "S"]

    def check_spot(y, x, idx, direction):

        if grid[y][x] != search[idx]:
            return 0

        if idx == len(search) - 1 and grid[y][x] == search[idx]:
            return 1

        sum = 0
        y2 = direction[0]
        x2 = direction[1]
        if y + y2 < len(grid) and y + y2 >= 0 and x + x2 < len(grid[y]) and x + x2 >= 0:
            if grid[y + y2][x + x2] == search[idx + 1]:
                sum += check_spot(y + y2, x + x2, idx + 1, direction)
            else:
                sum += 0

        return sum

    result = 0
    for y2, x2 in [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1],
    ]:

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                result += check_spot(y, x, 0, (y2, x2))

    return result


def solve2(lines):
    grid = []
    for line in lines:
        grid.append(list(line.strip()))

    result = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if (
                grid[y][x] == "A"
                and (
                    (grid[y - 1][x - 1] == "M" and grid[y + 1][x + 1] == "S")
                    or (grid[y + 1][x + 1] == "M" and grid[y - 1][x - 1] == "S")
                )
                and (
                    (grid[y - 1][x + 1] == "M" and grid[y + 1][x - 1] == "S")
                    or (grid[y + 1][x - 1] == "M" and grid[y - 1][x + 1] == "S")
                )
            ):
                result += 1

    return result


if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if len(test2) == 0:
        test2 = test1

    test1_solution = 18
    test2_solution = 9

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
