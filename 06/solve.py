def solve1(lines):
    map = []
    for line in lines:
        map.append(list(line))

    # Guard ^
    # Obstacle #
    # Empty .

    guard_pos = (0, 0)
    direction = (0, -1)
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == "^":
                guard_pos = (x, y)
                break

    # idle counter
    idle = 0
    x, y = guard_pos
    dx, dy = direction
    while True:
        # guard moves straight until it hits a wall, then turns right
        # bounds check 
        if y + dy < 0 or y + dy >= len(map) or x + dx < 0 or x + dx >= len(map[y]):
            # turn left (since flipped)
            dx, dy = -dy, dx
            break
        # wall check
        elif map[y + dy][x + dx] == "#":
            # turn "left"
            dx, dy = -dy, dx
        else:
            x += dx
            y += dy
            # if empty, mark
            if map[y][x] == ".":
                map[y][x] = "X"
                # reset idle
                idle = 0
            elif map[y][x] == "X":
                idle += 1

        if idle == 100:
            break

    # print map
    for row in map:
        print("".join(row))

    # sum all X
    return sum([row.count("X") for row in map]) + 1




def solve2(lines):
    map = []
    for line in lines:
        map.append(list(line))

    guard_pos = (0, 0)
    direction = (0, -1)
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == "^":
                guard_pos = (x, y)
                break

    # idle counter

    count = 0
    # Place new obstacle
    for i in range(len(map)):
        for j in range(len(map[i])):
            idle = 0
            x, y = guard_pos
            dx, dy = direction

            if map[i][j] != ".":
                continue

            modded_map = [row.copy() for row in map]
            modded_map[i][j] = "#"

            while True:
                # guard moves straight until it hits a wall, then turns right
                # bounds check 
                if y + dy < 0 or y + dy >= len(modded_map) or x + dx < 0 or x + dx >= len(modded_map[y]):
                    # turn left (since flipped)
                    dx, dy = -dy, dx
                    break
                # wall check
                elif modded_map[y + dy][x + dx] == "#":
                    # turn "left"
                    dx, dy = -dy, dx
                else:
                    x += dx
                    y += dy
                    # if empty, mark
                    if modded_map[y][x] == ".":
                        modded_map[y][x] = "X"
                        # reset idle
                        idle = 0
                    elif modded_map[y][x] == "X":
                        idle += 1

                if idle == 200:
                    count += 1
                    print("Loop found at " + str(i) + ", " + str(j))
                    break

    # sum all X
    return count

if __name__ == '__main__':
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == ['']:
        test2 = test1

    test1_solution = 41
    test2_solution = 6

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