import random

secret = random.randint(1, 10)
print("————————我爱鱼C工作室————————")
guess = 0
count = 3
print("不妨猜一下小甲鱼心里想的是哪个数字？", end=" ")
while guess != secret and count > 0:
    temp = input()
    if temp.isdigit():
        guess = int(temp)
        count -= 1
        if guess == secret:
            print("哎呀，你是小甲鱼肚里的蛔虫吗?")
            print("哼，猜中了也没有奖励!")
        else:
            if guess < secret:
                print("嘿，小了小了~~~")
            else:
                print("哥，大了大了~~~")
            if count > 0:
                print("再试一次吧", end=" ")
            else:
                print("次数用完了")
    else:
        print("❌️请重新输入整数", end=" ")

print("游戏结束，不玩啦")
