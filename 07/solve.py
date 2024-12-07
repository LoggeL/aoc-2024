def solve1(lines):
    result = 0
    for line in lines:
        parts = line.split(": ")
        value = int(parts[0])
        numbers = parts[1].split(" ")
        orders = []
        for number in numbers:
            if len(orders) == 0:
                orders.append(number)
            else:
                new_orders = []
                for order in orders:
                    if type(order) == str:
                        order = [order]
                    new_orders.append([*order, "+", number])
                    new_orders.append([*order, "*", number])
                orders = new_orders

        # check if one order is valid
        for order in orders:
            order_result = int(order[0])
            for i in range(1, len(order), 2):
                if order[i] == "+":
                    order_result += int(order[i + 1])
                elif order[i] == "*":
                    order_result = order_result * int(order[i + 1])

                if order_result > value: 
                    break

            if order_result == value:
                result += value
                break


    return result


def solve2(lines):
    result = 0
    for line in lines:
        parts = line.split(": ")
        value = int(parts[0])
        numbers = parts[1].split(" ")
        orders = []
        for number in numbers:
            if len(orders) == 0:
                orders.append(number)
            else:
                new_orders = []
                for order in orders:
                    if type(order) == str:
                        order = [order]
                    new_orders.append([*order, "+", number])
                    new_orders.append([*order, "*", number])
                    new_orders.append([*order, "||", number])
                orders = new_orders

        # check if one order is valid
        for order in orders:
            order_result = int(order[0])
            for i in range(1, len(order), 2):
                if order[i] == "+":
                    order_result += int(order[i + 1])
                elif order[i] == "*":
                    order_result = order_result * int(order[i + 1])
                elif order[i] == "||":
                    order_result = int(str(order_result) + str(order[i + 1]))

                if order_result > value:
                    break

            if order_result == value:
                result += value
                break

    return result


if __name__ == "__main__":
    test1 = open("test1", "r").read().strip().split("\n")
    test2 = open("test2", "r").read().strip().split("\n")
    input = open("input", "r").read().strip().split("\n")

    if test2 == [""]:
        test2 = test1

    test1_solution = 3749
    test2_solution = 11387

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
