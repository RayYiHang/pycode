

def bins(x):
    mylists = []
    results = ""
    while x >= 1:
        result = x % 2
        x = x // 2
        mylists.append(str(result))
        results += mylists.pop()
    return results


print(bins(255))
print(bin(255))
