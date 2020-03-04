list1 = [1, 2, 3, 4, "1", '2', 4]


def sums(x):
    count = 0
    for i in x:
        if isinstance(i, str):
            continue
        else:
            count += i
    return count


print(sums(list1))

