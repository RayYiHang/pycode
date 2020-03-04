

def calculate(*params):
    length = len(params)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in params[i]:
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == " ":
                space += 1
            else:
                others += 1
        print("第 %d 个字符串共有: ")