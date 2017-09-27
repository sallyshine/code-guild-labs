"""

>>> shrink('1235')
2

>>> shrink('13')
4

>>> shrink('1123581321')
9

"""

def shrink(numbers):
    num_list = list(numbers)
    int_list = []

    for n in num_list:
        int_list.append(int(n))

    total = 0

    for num in int_list:
        total += num

    if total > 9:
        total = 0
        for x in int_list:
            return x
            x = int(x)
            total += x
    return total
