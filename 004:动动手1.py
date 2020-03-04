temp = input("请输入一个整数：")
guess = int(temp)
count = 0
while guess != count:
    if count != guess:
        count += 1
        print(count)
