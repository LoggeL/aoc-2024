def line_valid(numbers):
    diffs = []
    for i in range(len(numbers) - 1):
        diffs.append(int(numbers[i + 1]) - int(numbers[i]))
    if max(diffs) < 0 and min(diffs) >= -3:
        return True
    elif min(diffs) > 0 and max(diffs) <= 3:
        return True
    return False

def solve1(lines):
    safe_lines = 0
    for line in lines:
        numbers = line.split(" ")
        numbers = [int(x) for x in numbers]
        if line_valid(numbers):
            safe_lines += 1

    return safe_lines        

def solve2(lines):
    safe_lines = 0

    for line in lines:
        numbers = line.split(" ")
        numbers = [int(x) for x in numbers]
        if line_valid(numbers):
            safe_lines += 1
        else:
            # remove one number and check if it is valid
            for i in range(len(numbers)):
                new_numbers = numbers[:i] + numbers[i + 1:]
                if line_valid(new_numbers):
                    safe_lines += 1
                    break

    return safe_lines


if __name__ == '__main__':
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if len(test2)  == 0:
        test2 = test1

    test1_solution = 2
    test2_solution = 4

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