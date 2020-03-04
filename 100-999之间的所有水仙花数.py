temp = 0
for i in range(100, 1000):
    temp = 0
    for each in str(i):
        temp += int(each) ** 3
        if temp == i:
            print(i)
