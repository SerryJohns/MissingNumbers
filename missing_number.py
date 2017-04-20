def find_missing(list1, list2):
    if len(list1) < 1 and len(list2) < 1:
        return 0
    if len(list1) > len(list2):
        large = list1
        small = list2
    else:
        large = list2
        small = list1

    for x in large:
        if x not in small:
            return x
    return 0

print(find_missing([4, 6], [4, 6]))