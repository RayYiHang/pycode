temp = input("请输入一个整数：")
guess = int(temp)
count = 0
while guess != count:
    print(guess * " " + guess * "*")
    guess -= 1
