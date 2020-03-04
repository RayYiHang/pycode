score = int(input("请输入一个分数"))
# 这种情况下比第一种和第二种好，不管是效率还是可读性
if 100 >= score > 90:
    print("A")
elif 90 >= score > 80:
    print("B")
elif 80 >= score > 60:
    print("C")
elif 60 >= score > 0:
    print("D")
else:
    print("输入错误")
