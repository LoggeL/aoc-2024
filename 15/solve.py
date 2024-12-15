def solve1(lines):
    lines = "\n".join(lines)
    map, order = lines.split("\n\n")
    map = map.split("\n")
    map = [list(row) for row in map]
    order = "".join(order.split("\n"))

    # print(map)
    # print(order)

    robot_pos = (0, 0)
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "@":
                robot_pos = (y, x)
                break

    for i in range(len(order)):
        if order[i] == "^":
            direction = (-1, 0)
        elif order[i] == "v":
            direction = (1, 0)
        elif order[i] == ">":
            direction = (0, 1)
        elif order[i] == "<":
            direction = (0, -1)

        boxes_to_move = []
        new_pos = robot_pos
        while True:
            new_pos = (new_pos[0] + direction[0], new_pos[1] + direction[1])
            if map[new_pos[0]][new_pos[1]] == "O":
                boxes_to_move.append(new_pos)
            elif map[new_pos[0]][new_pos[1]] == "#":
                boxes_to_move = []
                break
            elif map[new_pos[0]][new_pos[1]] == ".":
                for box in boxes_to_move[::-1]:
                    # push box
                    map[box[0]][box[1]] = "."
                    map[box[0] + direction[0]][box[1] + direction[1]] = "O"
                # move robot
                map[robot_pos[0]][robot_pos[1]] = "."
                map[robot_pos[0] + direction[0]][robot_pos[1] + direction[1]] = "@"
                robot_pos = (robot_pos[0] + direction[0], robot_pos[1] + direction[1])
                break
            else:
                print("Unknown tile")
                print("Turn: ", i)
                print(map[new_pos[0]][new_pos[1]])
                exit(1)

        # print map
        # print("Turn: ", i)
        # print("Boxes: ", boxes_to_move)
        # print("Robot: ", robot_pos)
        # print("Order: ", order[i])
        # for row in map:
        #     print("".join(row))
        # print()

    result = 0
    # box coordinates
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "O":
                result += y * 100 + x

    return result


def solve2(lines):
    lines = "\n".join(lines)
    map, order = lines.split("\n\n")
    map = map.split("\n")
    map = [list(row) for row in map]
    order = "".join(order.split("\n"))

    new_map = []
    for row in map:
        new_row = []
        for i in range(len(row)):
            if row[i] == "@":
                new_row.append("@")
                new_row.append(".")
            elif row[i] == "#":
                new_row.append("#")
                new_row.append("#")
            elif row[i] == ".":
                new_row.append(".")
                new_row.append(".")
            elif row[i] == "O":
                new_row.append("[")
                new_row.append("]")
            else:
                print("Unknown tile")
                print(row[i])
                exit(1)
        new_map.append(new_row)

    map = new_map
    # print(map)
    # print(order)

    robot_pos = (0, 0)
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "@":
                robot_pos = (y, x)
                break

        for i in range(len(order)):
        if order[i] == "^":
            direction = (-1, 0)
        elif order[i] == "v":
            direction = (1, 0)
        elif order[i] == ">":
            direction = (0, 1)
        elif order[i] == "<":
            direction = (0, -1)

        boxes_to_move = []
        new_pos = robot_pos
        while True:
            new_pos = (new_pos[0] + direction[0], new_pos[1] + direction[1])
            if map[new_pos[0]][new_pos[1]] == "[" or map[new_pos[0]][new_pos[1]] == "]":
                # something something construct a tree
                # Too tired to do this
                pass
            elif map[new_pos[0]][new_pos[1]] == "#":
                boxes_to_move = []
                break
            elif map[new_pos[0]][new_pos[1]] == ".":
                for box in boxes_to_move[::-1]:
                    # push box
                    map[box[0]][box[1]] = "."
                    map[box[0] + direction[0]][box[1] + direction[1]] = "O"
                # move robot
                map[robot_pos[0]][robot_pos[1]] = "."
                map[robot_pos[0] + direction[0]][robot_pos[1] + direction[1]] = "@"
                robot_pos = (robot_pos[0] + direction[0], robot_pos[1] + direction[1])
                break
            else:
                print("Unknown tile")
                print("Turn: ", i)
                print(map[new_pos[0]][new_pos[1]])
                exit(1)

        # print map
        # print("Turn: ", i)
        # print("Boxes: ", boxes_to_move)
        # print("Robot: ", robot_pos)
        # print("Order: ", order[i])
        # for row in map:
        #     print("".join(row))
        # print()

    result = 0
    # box coordinates
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "O":
                result += y * 100 + x

    return result


if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 10092
    test2_solution = 0

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
