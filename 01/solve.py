def solve1(text):
    left_list = []
    right_list = []
    for i in range(len(text)):
        text_split = text[i].split()
        if len(text_split) != 2:
            continue
        left_list.append(text_split[0])
        right_list.append(text_split[1])

    # sort
    left_list.sort()
    right_list.sort()

    result = 0
    for i in range(len(left_list)):
        result += abs(int(left_list[i]) - int(right_list[i]))
    return result


def solve2(text):

    left_list = []
    right_list = []
    for i in range(len(text)):
        text_split = text[i].split()
        if len(text_split) != 2:
            continue
        left_list.append(int(text_split[0]))
        right_list.append(int(text_split[1]))

    # value counts
    left_list_count = {}
    right_list_count = {}

    for i in range(len(left_list)):
        left_list_count[left_list[i]] = left_list_count.get(left_list[i], 0) + 1
        right_list_count[right_list[i]] = right_list_count.get(right_list[i], 0) + 1

    result = 0
    for i in range(len(left_list)):
        number = left_list[i]
        right_count = right_list_count[number] if number in right_list_count else 0

        result += right_count * number

    return result


if __name__ == "__main__":
    test1 = open("test1", "r").read().split("\n")
    test2 = open("test2", "r").read().split("\n")
    input = open("input", "r").read().split("\n")

    test1_solution = 11
    test2_solution = 31

    test1_result = solve1(test1)
    test2_result = solve2(test2)

    print("Test 1: " + str(test1_result))
    if test1_solution != test1_result:
        print("❌ Test 1 failed!")
        exit(1)
    else:
        print("✅ Test 1 passed!")

    print("Solution 1: " + str(solve1(input)))

    print("Test 2: " + str(test2_result))
    if test2_solution != test2_result:
        print("❌ Test 2 failed!")
        exit(1)
    else:
        print("✅ Test 2 passed!")

    print("Solution 2: " + str(solve2(input)))
