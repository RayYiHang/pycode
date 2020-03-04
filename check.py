symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

passwd = input('请输入需要检查的密码组合')

# 判断是否为空以及空格
while passwd.isspace() or len(passwd) == 0:
    print("错误,没有输入或者是使用了空格,请重新输入", end="")
    passwd = input()


# 判断长度
countLen = 0
length = len(passwd)
if length <= 8:
    countLen = 1
elif 16 > length > 8:
    countLen = 2
else:
    countLen = 3

# 判断由什么组成
compCount = 0

for i in passwd:
    if i in nums:
        compCount += 1
        break

for i in passwd:
    if i in chars:
        compCount += 1
        break

for i in passwd:
    if i in symbols:
        compCount += 1
        break

# 整合判断
while 1:
    print("您的密码安全级别评定为:", end="")
    if countLen == 1 or compCount == 1:
        print("低")
    elif countLen == 3 and compCount == 3 and (passwd[0] in chars):
        print("高\n请继续保持")
        break
    else:
        print("中")
    print("请按一下方式提升您的密码安全级别:\n\
          \t1.密码必须由数字、字母及特殊字符三种组合\n\
          \t2.密码只能由字母开头\n\
          \t3.密码长度不能低于16位")
    break
