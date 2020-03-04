# 求最大公约数


def gcd(x, y):
    rest = 0
    while y != 0:
        rest = y
        y = x % y
        x = rest
    return rest


print(gcd(1071, 462))
