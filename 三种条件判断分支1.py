score = int(input("请输入一个分数"))
# 这种情况下，效率底，每种情况都会检查
if 100 >= score > 90:
    print("A")
if 90 >= score > 80:
    print("B")
if 80 >= score > 60:
    print("C")
if 60 >= score > 0:
    print("D")
if score > 100 or score < 0:
    print("输入错误")
