def in_array(array1, array2):
    lst = []
    for i in array1:
        for x in array2:
            if i in x and i not in lst:
                lst.append(i)
    return sorted(lst)