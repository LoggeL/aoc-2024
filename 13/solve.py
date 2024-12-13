def solve1(lines):
    # Parse input
    # Button A: X+94, Y+34
    # Button B: X+22, Y+67
    # Prize: X=8400, Y=5400
    # \n

    blocks = []
    for i in range(0, len(lines), 4):
        A = lines[i].split(": ")[1].split(", ")
        B = lines[i + 1].split(": ")[1].split(", ")
        Prize = lines[i + 2].split(": ")[1].split(", ")

        A[0] = int(A[0].replace("X+", ""))
        A[1] = int(A[1].replace("Y+", ""))
        B[0] = int(B[0].replace("X+", ""))
        B[1] = int(B[1].replace("Y+", ""))
        Prize[0] = int(Prize[0].replace("X=", ""))
        Prize[1] = int(Prize[1].replace("Y=", ""))

        blocks.append((A, B, Prize))

    # Linear equation
    # Px = Ax * n1 + Bx * n2
    # Py = Ay * n1 + By * n2

    # (Px - Ax * n1) / Bx = n2
    # (Py - Ay * n1) / By = n2

    # (Px - Ax * n1) / Bx = (Py - Ay * n1) / By
    # Px * By - Ax * n1 * By = Py * Bx - Ay * n1 * Bx
    # Px * By - Py * Bx = Ax * n1 * By - Ay * n1 * Bx
    # Px * By - Py * Bx = n1 * (Ax * By - Ay * Bx)
    # n1 = (Px * By - Py * Bx) / (Ax * By - Ay * Bx)

    # n2 = (Px - Ax * n1) / Bx

    result = 0
    for block in blocks:
        A, B, Prize = block

        n1 = (Prize[0] * B[1] - Prize[1] * B[0]) / (A[0] * B[1] - A[1] * B[0])
        n2 = (Prize[0] - A[0] * n1) / B[0]

        # if not int continue
        if n1 != int(n1) or n2 != int(n2):
            continue

        print(n1, n2)
        result += n1 * 3 + n2

    return int(result)


def solve2(lines):
    # Parse input
    # Button A: X+94, Y+34
    # Button B: X+22, Y+67
    # Prize: X=8400, Y=5400
    # \n

    blocks = []
    for i in range(0, len(lines), 4):
        A = lines[i].split(": ")[1].split(", ")
        B = lines[i + 1].split(": ")[1].split(", ")
        Prize = lines[i + 2].split(": ")[1].split(", ")

        A[0] = int(A[0].replace("X+", ""))
        A[1] = int(A[1].replace("Y+", ""))
        B[0] = int(B[0].replace("X+", ""))
        B[1] = int(B[1].replace("Y+", ""))
        Prize[0] = int(Prize[0].replace("X=", "")) + 10000000000000
        Prize[1] = int(Prize[1].replace("Y=", "")) + 10000000000000

        blocks.append((A, B, Prize))

    # Linear equation
    # Px = Ax * n1 + Bx * n2
    # Py = Ay * n1 + By * n2

    # (Px - Ax * n1) / Bx = n2
    # (Py - Ay * n1) / By = n2

    # (Px - Ax * n1) / Bx = (Py - Ay * n1) / By
    # Px * By - Ax * n1 * By = Py * Bx - Ay * n1 * Bx
    # Px * By - Py * Bx = Ax * n1 * By - Ay * n1 * Bx
    # Px * By - Py * Bx = n1 * (Ax * By - Ay * Bx)
    # n1 = (Px * By - Py * Bx) / (Ax * By - Ay * Bx)

    # n2 = (Px - Ax * n1) / Bx

    result = 0
    for block in blocks:
        A, B, Prize = block

        n1 = (Prize[0] * B[1] - Prize[1] * B[0]) / (A[0] * B[1] - A[1] * B[0])
        n2 = (Prize[0] - A[0] * n1) / B[0]

        # if not int continue
        if n1 != int(n1) or n2 != int(n2):
            continue

        print(n1, n2)
        result += n1 * 3 + n2

    return int(result)


if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 480
    test2_solution = 0

    test1_result = solve1(test1)
    test2_result = solve2(test2)

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
