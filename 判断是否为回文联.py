

def dicts(String):
    list1 = list(String)
    list2 = reversed(list1)
    if list1 == list(list2):
        return "是回文联"
    else:
        return "不是回文联"


print(dicts("上海自来水来自海上"))
