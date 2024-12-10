def solve1(lines):
    line = lines[0]

    # Convert string into alternating list of file/space lengths
    lengths = [int(x) for x in line]

    # Create list of (file_id, length) pairs
    files = []
    for i in range(0, len(lengths), 2):
        if lengths[i] > 0:
            files.append({"id": i // 2, "length": lengths[i]})
        if i + 1 < len(lengths) and lengths[i + 1] > 0:
            files.append({"id": None, "length": lengths[i + 1]})

    # print(files, "\n")
    for left_index in range(len(files)):
        if files[left_index]["id"] is None:
            # find last item with numbers
            for right_index in range(len(files) - 1, left_index, -1):
                if files[right_index]["id"] is not None:

                    left_length = files[left_index]["length"]
                    right_length = files[right_index]["length"]

                    # 3 cases
                    if left_length == right_length:
                        # swap
                        files[right_index]["id"], files[left_index]["id"] = (
                            files[left_index]["id"],
                            files[right_index]["id"],
                        )
                        break
                    elif left_length > right_length:
                        # fill right with numbers and keep remaining in left
                        files[right_index]["length"] = right_length
                        files[left_index]["length"] = right_length
                        files[left_index]["id"] = files[right_index]["id"]
                        files[right_index]["id"] = None
                        # inject new empty file
                        files.insert(
                            left_index + 1,
                            {"id": None, "length": left_length - right_length},
                        )
                        break
                    elif left_length < right_length:
                        # fill left with numbers and keep remaining in right
                        files[left_index]["length"] = left_length
                        files[right_index]["length"] = right_length - left_length
                        files[left_index]["id"] = files[right_index]["id"]
                        files[right_index]["length"] = right_length - left_length
                        break
                    else:
                        raise Exception("Invalid case")

        # output_str = ""
        # for file in files:
        #     output_str += (
        #         "." * file["length"]
        #         if file["id"] is None
        #         else str(file["id"]) * file["length"]
        #     )
        # print(output_str)

    checksum = 0
    idx = 0
    for file in files:
        if file["id"] is not None:
            for i in range(file["length"]):
                checksum += (file["id"]) * (idx + i)
            idx += file["length"]
    return checksum


def solve2(lines):
    line = lines[0]

    # Convert string into alternating list of file/space lengths
    lengths = [int(x) for x in line]

    # Create list of (file_id, length) pairs
    files = []
    for i in range(0, len(lengths), 2):
        if lengths[i] > 0:
            files.append({"id": i // 2, "length": lengths[i]})
        if i + 1 < len(lengths) and lengths[i + 1] > 0:
            files.append({"id": None, "length": lengths[i + 1]})

        # print(files, "\n")
    for left_index in range(len(files)):
        if files[left_index]["id"] is None:
            # find last item with numbers
            jump_to = None
            for right_index in range(len(files) - 1, left_index, -1):
                if files[right_index]["id"] is not None:

                    left_length = files[left_index]["length"]
                    right_length = files[right_index]["length"]

                    # 3 cases
                    if left_length == right_length:
                        # swap
                        files[right_index]["id"], files[left_index]["id"] = (
                            files[left_index]["id"],
                            files[right_index]["id"],
                        )
                        if jump_to is not None:
                            right_index = jump_to
                            jump_to = None
                        break
                    elif left_length > right_length:
                        # fill right with numbers and keep remaining in left
                        files[right_index]["length"] = right_length
                        files[left_index]["length"] = right_length
                        files[left_index]["id"] = files[right_index]["id"]
                        files[right_index]["id"] = None
                        # inject new empty file
                        files.insert(
                            left_index + 1,
                            {"id": None, "length": left_length - right_length},
                        )
                        if jump_to is not None:
                            right_index = jump_to
                            jump_to = None
                        break
                    elif left_length < right_length:
                        # small gap -> check other values
                        if jump_to is None:
                            jump_to = right_index
                    else:
                        raise Exception("Invalid case")

    output_str = ""
    for file in files:
        output_str += (
            "." * file["length"]
            if file["id"] is None
            else str(file["id"]) * file["length"]
        )
    print(output_str)

    checksum = 0
    idx = 0
    for file in files:
        if file["id"] is not None:
            for i in range(file["length"]):
                checksum += (file["id"]) * (idx + i)
            idx += file["length"]
        else:
            idx += file["length"]
    return checksum


if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 1928
    test2_solution = 2858

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
