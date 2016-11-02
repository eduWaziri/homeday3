def find_missing(list1, list2):

    if (len(list1) == 0) or (len(list2) == 0):
        return 0

    elif list1 == list2:
        return 0

    else:
        return list(set(list2).difference(list1))[0]

l1 = [1,2,3,4]
l2 = [1,2,3,4,5]
print find_missing(l1, l2)
