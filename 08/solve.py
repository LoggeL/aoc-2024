def solve1(lines):
    map_grid = [
        list(line) for line in lines
    ]  # Renamed to avoid shadowing built-in `map`
    unique_chars = set()
    for line in map_grid:
        unique_chars.update(line)

    # Remove '.' if it exists
    unique_chars.discard(".")  # Using discard to avoid KeyError if '.' isn't present

    # Sort the characters to ensure deterministic processing order
    sorted_unique_chars = sorted(unique_chars)

    max_x = len(map_grid[0])
    max_y = len(map_grid)

    pos = []
    for char in sorted_unique_chars:
        # Get positions of char
        for y in range(max_y):
            for x in range(max_x):
                if map_grid[y][x] == char:
                    pos.append((char, x, y))

    # Calculate and set antinode positions
    for char1, x1, y1 in pos:
        for char2, x2, y2 in pos:
            if x1 == x2 and y1 == y2 or char1 != char2:
                continue

            # Calculate first antinode
            antinode1_x = 2 * x1 - x2
            antinode1_y = 2 * y1 - y2

            if 0 <= antinode1_x < max_x and 0 <= antinode1_y < max_y:
                map_grid[antinode1_y][antinode1_x] = "#"

            # Calculate second antinode
            antinode2_x = 2 * x2 - x1
            antinode2_y = 2 * y2 - y1

            if 0 <= antinode2_x < max_x and 0 <= antinode2_y < max_y:
                map_grid[antinode2_y][antinode2_x] = "#"

    # Print map (optional, can be removed if not needed)
    for line in map_grid:
        print("".join(line))

    # Count '#'
    result = sum(line.count("#") for line in map_grid)

    return result


def solve2(lines):
    map_grid = [
        list(line) for line in lines
    ]  # Renamed to avoid shadowing built-in `map`
    unique_chars = set()
    for line in map_grid:
        unique_chars.update(line)

    # Remove '.' if it exists
    unique_chars.discard(".")  # Using discard to avoid KeyError if '.' isn't present

    # Sort the characters to ensure deterministic processing order
    sorted_unique_chars = sorted(unique_chars)

    max_x = len(map_grid[0])
    max_y = len(map_grid)

    pos = []
    for char in sorted_unique_chars:
        # Get positions of char
        for y in range(max_y):
            for x in range(max_x):
                if map_grid[y][x] == char:
                    pos.append((char, x, y))

    # Calculate and set antinode positions
    for char1, x1, y1 in pos:
        for char2, x2, y2 in pos:
            if x1 == x2 and y1 == y2 or char1 != char2:
                continue

            for i in range(-50, 50):

                if i == 0:
                    continue

                # Calculate antinode
                antinode_x = (x1 - x2) * i + x1
                antinode_y = (y1 - y2) * i + y1

                if 0 <= antinode_x < max_x and 0 <= antinode_y < max_y:
                    map_grid[antinode_y][antinode_x] = "#"

    # Print map (optional, can be removed if not needed)
    for line in map_grid:
        print("".join(line))

    # Count '#'
    result = sum(line.count("#") for line in map_grid)

    return result


if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 14
    test2_solution = 34

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
