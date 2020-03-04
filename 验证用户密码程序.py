
count = 3
print("请输入密码", end="")
while True:
    temp = input()
    if "*" in temp:
        print("密码中不能含有'*'号！您还有" + str(count) + "次机会！请输入密码:", end="")
        continue
    elif count < 0:
        print("次数用完了，退出")
        break
    elif temp == "FishC.com":
        print("密码正确，进入程序...")
        break
    else:
        count -= 1
        print("密码输入错误！您还有" + str(count) + "次机会，请输入密码", end="")
        continue


