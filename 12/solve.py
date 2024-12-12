import copy


def solve1(lines):
    map = []
    for line in lines:
        map.append(list(line))

    def check_surrounding(y, x, letter, chunk):
        if map[y][x] != letter:
            return
        if (y, x) in chunk:
            return

        chunk.append((y, x))
        map[y][x] = "."

        if y > 0 and map[y - 1][x] == letter:
            check_surrounding(y - 1, x, letter, chunk)
        if y < len(map) - 1 and map[y + 1][x] == letter:
            check_surrounding(y + 1, x, letter, chunk)
        if x > 0 and map[y][x - 1] == letter:
            check_surrounding(y, x - 1, letter, chunk)
        if x < len(map[y]) - 1 and map[y][x + 1] == letter:
            check_surrounding(y, x + 1, letter, chunk)

    chunks = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] != ".":
                chunk = []
                check_surrounding(y, x, map[y][x], chunk)
                chunk = list(set(chunk))
                chunks.append(chunk)

    result = 0
    for chunk in chunks:
        chunk_map = copy.deepcopy(map)
        # surround chunk with walls
        area = 0
        for y, x in chunk:
            chunk_map[y][x] = "#"
            area += 1

        walls = []
        for y, x in chunk:
            # check if there is a . in the surrounding
            if y == 0 or chunk_map[y - 1][x] == ".":
                walls.append((y - 1, x))
            if y == len(chunk_map) - 1 or chunk_map[y + 1][x] == ".":
                walls.append((y + 1, x))
            if x == 0 or chunk_map[y][x - 1] == ".":
                walls.append((y, x - 1))
            if x == len(chunk_map[y]) - 1 or chunk_map[y][x + 1] == ".":
                walls.append((y, x + 1))
            # if y == 0 or x == 0 or chunk_map[y - 1][x - 1] == ".":
            #     walls.append((y - 1, x - 1))
            # if y == 0 or x == len(chunk_map[y]) - 1 or chunk_map[y - 1][x + 1] == ".":
            #     walls.append((y - 1, x + 1))
            # if y == len(chunk_map) - 1 or x == 0 or chunk_map[y + 1][x - 1] == ".":
            #     walls.append((y + 1, x - 1))
            # if (
            #     y == len(chunk_map) - 1
            #     or x == len(chunk_map[y]) - 1
            #     or chunk_map[y + 1][x + 1] == "."
            # ):
            #     walls.append((y + 1, x + 1))

        # remove duplicates
        # walls = list(set(walls))

        result += area * len(walls)

    return result


def solve2(lines):
    # I tried really hard to solve this, but I couldn't.
    # Here have a useless quote:
    # Time is a flat circle.
    map = []
    for line in lines:
        map.append(list(line))

    def check_surrounding(y, x, letter, chunk):
        if map[y][x] != letter:
            return
        if (y, x) in chunk:
            return

        chunk.append((y, x))
        map[y][x] = "."

        if y > 0 and map[y - 1][x] == letter:
            check_surrounding(y - 1, x, letter, chunk)
        if y < len(map) - 1 and map[y + 1][x] == letter:
            check_surrounding(y + 1, x, letter, chunk)
        if x > 0 and map[y][x - 1] == letter:
            check_surrounding(y, x - 1, letter, chunk)
        if x < len(map[y]) - 1 and map[y][x + 1] == letter:
            check_surrounding(y, x + 1, letter, chunk)

    chunks = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] != ".":
                chunk = []
                check_surrounding(y, x, map[y][x], chunk)
                chunk = list(set(chunk))
                chunks.append(chunk)

    result = 0
    for chunk in chunks:
        chunk_map = copy.deepcopy(map)
        # surround chunk with walls
        area = 0
        for y, x in chunk:
            chunk_map[y][x] = "#"
            area += 1

        walls = []
        for y, x in chunk:
            # check if there is a . in the surrounding
            if y == 0 or chunk_map[y - 1][x] == ".":
                walls.append((y - 1, x))
            if y == len(chunk_map) - 1 or chunk_map[y + 1][x] == ".":
                walls.append((y + 1, x))
            if x == 0 or chunk_map[y][x - 1] == ".":
                walls.append((y, x - 1))
            if x == len(chunk_map[y]) - 1 or chunk_map[y][x + 1] == ".":
                walls.append((y, x + 1))

        # remove duplicates
        # walls = list(set(walls))

        def find_horizontal_walls(walls, wall, horizontal_wall):
            for wall2 in walls:
                if (
                    wall[0] == wall2[0]
                    and abs(wall[1] - wall2[1]) == 1
                    and wall2 not in horizontal_wall
                ):
                    horizontal_wall.append(wall2)
                    find_horizontal_walls(walls, wall2, horizontal_wall)
            return None

        def find_vertical_walls(walls, wall, vertical_wall):
            for wall2 in walls:
                if (
                    wall[1] == wall2[1]
                    and abs(wall[0] - wall2[0]) == 1
                    and wall2 not in vertical_wall
                ):
                    vertical_wall.append(wall2)
                    find_vertical_walls(walls, wall2, vertical_wall)
            return None

        # Group walls
        horizontal_walls = []
        for wall in walls:
            # find vertical & horizontal walls
            for horizontal_wall in horizontal_walls:
                if wall in horizontal_wall:
                    break
            else:
                horizontal_wall = []
                find_horizontal_walls(walls, wall, horizontal_wall)
                if horizontal_wall:
                    horizontal_walls.append(horizontal_wall)

        vertical_walls = []
        for wall in walls:
            for vertical_wall in vertical_walls:
                if wall in vertical_wall:
                    break
            else:
                vertical_wall = []
                find_vertical_walls(walls, wall, vertical_wall)
                if vertical_wall:
                    vertical_walls.append(vertical_wall)

        other_walls = []
        for wall in walls:
            for horizontal_wall in horizontal_walls:
                if wall in horizontal_wall:
                    break
            else:
                for vertical_wall in vertical_walls:
                    if wall in vertical_wall:
                        break
                else:
                    other_walls.append(wall)

        result += area * (
            len(horizontal_walls) + len(vertical_walls) + len(other_walls)
        )

    return result


if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 1930
    test2_solution = 1206

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
