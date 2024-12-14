def solve1(lines):

    # max x, max y
    max_x = 0
    max_y = 0
    robots = []
    for robot in lines:
        # p=0,4 v=3,-3
        # p=x,y v=vx,vy
        pos = robot.split(" ")[0].split("=")[1].split(",")
        vel = robot.split(" ")[1].split("=")[1].split(",")
        robots.append([int(pos[0]), int(pos[1]), int(vel[0]), int(vel[1])])
        max_x = max(max_x, int(pos[0]))
        max_y = max(max_y, int(pos[1]))

    max_x += 1
    max_y += 1

    turns = 100
    for robot in robots:
        robot[0] += robot[2] * turns
        robot[1] += robot[3] * turns
        robot[0] %= max_x
        robot[1] %= max_y

    # count robots in each quadrant
    quadrant_counts = [0, 0, 0, 0]
    # 11 => first 5, ignore middle, last 5
    half_x = max_x // 2
    half_y = max_y // 2
    for robot in robots:
        # ignore middle
        if robot[0] == half_x and robot[1] == half_y:
            continue
        if robot[0] > half_x and robot[1] > half_y:
            quadrant_counts[0] += 1
        elif robot[0] > half_x and robot[1] < half_y:
            quadrant_counts[1] += 1
        elif robot[0] < half_x and robot[1] > half_y:
            quadrant_counts[2] += 1
        elif robot[0] < half_x and robot[1] < half_y:
            quadrant_counts[3] += 1

    print(quadrant_counts)

    return (
        quadrant_counts[0]
        * quadrant_counts[1]
        * quadrant_counts[2]
        * quadrant_counts[3]
    )


def solve2(lines):

    # max x, max y
    max_x = 0
    max_y = 0
    robots = []
    for robot in lines:
        # p=0,4 v=3,-3
        # p=x,y v=vx,vy
        pos = robot.split(" ")[0].split("=")[1].split(",")
        vel = robot.split(" ")[1].split("=")[1].split(",")
        robots.append([int(pos[0]), int(pos[1]), int(vel[0]), int(vel[1])])
        max_x = max(max_x, int(pos[0]))
        max_y = max(max_y, int(pos[1]))

    max_x += 1
    max_y += 1

    half_x = max_x // 2
    half_y = max_y // 2

    top_variance = 100_000
    top_turn = 0

    turns = 10_000
    for i in range(1, turns):
        for robot in robots:
            robot[0] += robot[2]
            robot[1] += robot[3]
            robot[0] %= max_x
            robot[1] %= max_y

        # get variance
        distances = []
        for robot in robots:
            distances.append((robot[0] - half_x) ** 2 + (robot[1] - half_y) ** 2)

        variance = sum(distances) / len(distances)
        # print(i, variance)
        if variance < top_variance:
            top_variance = variance
            top_turn = i

    return top_turn


if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 12
    test2_solution = 0

    test1_result = solve1(test1)
    # test2_result = solve2(test2)

    print("Test 1: " + str(test1_result))
    if test1_solution != test1_result:
        print("Test 1 failed!")
        exit(1)

    print("Solution 1: " + str(solve1(input)))

    # print("Test 2: " + str(test2_result))
    # if test2_solution != test2_result:
    #     print("Test 2 failed!")
    #     exit(1)

    print("Solution 2: " + str(solve2(input)))
