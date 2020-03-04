score = int(input("请输入一个分数"))
# 这种情况下cpu占用率相比第一种提高了400%
# 有一种情况成立，后面不会进行判断
if 100 >= score > 90:
    print("A")
else:
    if 90 >= score > 80:
        print("B")
    else:
        if 80 >= score > 60:
            print("C")
        else:
            if 60 >= score > 0:
                print("D")
            else:
                print("输入错误")
