def solve1(lines):
    # split the lines at the empty line
    groups = "\n".join(lines).split("\n\n")
    orders = groups[0].split("\n")
    updates = groups[1].split("\n")

    orders_dict = {}
    for order in orders:
        order = order.split("|")
        if order[0] not in orders_dict:
            orders_dict[order[0]] = []
        orders_dict[order[0]].append(order[1])

    result = 0
    for update in updates:
        update = update.split(",")
        invalid = False
        for i in range(len(update)):
            if invalid:
                break
            item = update[i]
            if item not in orders_dict:
                continue
            looking_for_items = orders_dict[item]
            for looking_for in looking_for_items:
                if looking_for in update and update.index(looking_for) < i:
                    print("Invalid line", update, "Found " + looking_for + " after " + item)
                    invalid = True
                    break
            else:
                continue
        else:
            if not invalid:
                print("Valid Line", update, "adding " + update[int(len(update) / 2)])
                result += int(update[int(len(update) / 2)])

    return result

def solve2(lines):
    # split the lines at the empty line
    groups = "\n".join(lines).split("\n\n")
    orders = groups[0].split("\n")
    updates = groups[1].split("\n")

    orders_dict = {}
    for order in orders:
        order = order.split("|")
        if order[0] not in orders_dict:
            orders_dict[order[0]] = []
        orders_dict[order[0]].append(order[1])

    result = 0
    invalid_lines = []
    for update in updates:
        update = update.split(",")
        invalid = False
        for i in range(len(update)):
            if invalid:
                break
            item = update[i]
            if item not in orders_dict:
                continue
            looking_for_items = orders_dict[item]
            for looking_for in looking_for_items:
                if looking_for in update and update.index(looking_for) < i:
                    # print("Invalid line", update, "Found " + looking_for + " after " + item)
                    invalid = True
                    invalid_lines.append(update)
                    break
            else:
                continue
        else:
            pass
    # sort invalid lines by the order
    for line in invalid_lines:
        invalid = True
        while invalid:
            for i in range(len(line)):
                if line[i] not in orders_dict:
                    continue
                looking_for_items = orders_dict[line[i]]
                for looking_for in looking_for_items:
                    if looking_for in line and line.index(looking_for) < i:
                        print("Invalid line", line, "Found " + looking_for + " after " + line[i])
                        # swap the two items
                        line[i], line[line.index(looking_for)] = line[line.index(looking_for)], line[i]
                        break
                else:
                    continue
                break
            else:
                invalid = False
                print("Valid Line", line, "adding " + line[int(len(line) / 2)])
                result += int(line[int(len(line) / 2)])


    return result

if __name__ == '__main__':
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == ['']:
        test2 = test1

    test1_solution = 143
    test2_solution = 123

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