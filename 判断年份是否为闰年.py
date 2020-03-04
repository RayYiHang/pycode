
print("输入年份:", end=" ")
while True:
    temp = input()
    if temp.isdigit():
        num = int(temp)
        if num % 400 == 0:
            print(temp + "是闰年")
            break
        else:
            if num % 4 == 0 and num % 100 != 0:
                print(temp + "是闰年")
            else:
                print(temp + "不是闰年")
                print("请重新输入", end=" ")
    else:
        print("请重新输入数字", end=" ")
