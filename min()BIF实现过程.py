list1 = [1, 2, 3, 4, 5, 6, 7, -10]


def mis(x):
    temp = x[0]
    for i in x:
        if i < temp:
            temp = i
    return temp


print(mis(list1))