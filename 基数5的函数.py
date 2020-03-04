

def baseFive(* params):
    count = 0
    if params[len(params) - 1] == 5:
        for i in params:
            count += i
        result = (count - 5) * 5
    else:
        for i in params:
            count += i
        result = count * 3
    return result


print(baseFive(1, 2, 3, 4, 5))
