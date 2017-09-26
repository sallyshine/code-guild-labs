def shrink(numbers):
    num_list = list(numbers)
    int_list = []

    for n in num_list:
        int_list.append(int(n))

    total = 0

    for num in int_list:
        total += num

    if total > 9:
        int_list = list(str(total))
        total = 0
        for x in int_list:
            total =+ x
    return total
