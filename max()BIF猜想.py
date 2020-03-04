list1 = [1, 2, 3, 4, 5, 0, -10]
temp = list1[0]
for i in list1:
    if i > temp:
        temp = i

print(temp)
