def permutation(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        return True
    return False
