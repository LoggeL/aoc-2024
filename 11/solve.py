def solve1(lines):
    line = lines[0]

    stones = {}
    for stone in line.split(" "):
        stone_number = int(stone)
        if stone_number not in stones:
            stones[stone_number] = 1
        else:
            stones[stone_number] += 1 
            
    num_loops = 25
    for i in range(1, num_loops + 1):
        new_stones = {}
        for stone_num, stone_count in stones.items():
            # 0 -> 1
            # even digits -> split
            # odd digits -> *= 2024
            if stone_num == 0:
                if 1 not in new_stones:
                    new_stones[1] = stone_count
                else:
                    new_stones[1] += stone_count

            elif len(str(stone_num)) % 2 == 0:
                left_number = int(str(stone_num)[:len(str(stone_num)) // 2])
                right_number = int(str(stone_num)[len(str(stone_num)) // 2:])
                if left_number not in new_stones:
                    new_stones[left_number] = stone_count
                else:
                    new_stones[left_number] += stone_count

                if right_number not in new_stones:
                    new_stones[right_number] = stone_count
                else:
                    new_stones[right_number] += stone_count
            else:
                new_stones[stone_num * 2024] = stone_count

        stones = new_stones

    return sum([stone_count for stone_count in stones.values()])
            

def solve2(lines):
    line = lines[0]

    stones = {}
    for stone in line.split(" "):
        stone_number = int(stone)
        if stone_number not in stones:
            stones[stone_number] = 1
        else:
            stones[stone_number] += 1 
            
    num_loops = 75
    for i in range(1, num_loops + 1):
        new_stones = {}
        for stone_num, stone_count in stones.items():
            # 0 -> 1
            # even digits -> split
            # odd digits -> *= 2024
            if stone_num == 0:
                if 1 not in new_stones:
                    new_stones[1] = stone_count
                else:
                    new_stones[1] += stone_count

            elif len(str(stone_num)) % 2 == 0:
                left_number = int(str(stone_num)[:len(str(stone_num)) // 2])
                right_number = int(str(stone_num)[len(str(stone_num)) // 2:])
                if left_number not in new_stones:
                    new_stones[left_number] = stone_count
                else:
                    new_stones[left_number] += stone_count

                if right_number not in new_stones:
                    new_stones[right_number] = stone_count
                else:
                    new_stones[right_number] += stone_count
            else:
                new_stones[stone_num * 2024] = stone_count

        stones = new_stones

    return sum([stone_count for stone_count in stones.values()])
            

if __name__ == '__main__':
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == ['']:
        test2 = test1

    test1_solution = 55312
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