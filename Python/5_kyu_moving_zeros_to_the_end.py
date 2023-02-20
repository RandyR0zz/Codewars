def move_zeros(lst):
    count = 0
    while 0 in lst:
        lst.remove(0)
        count += 1
    while count != 0:
        lst.insert(len(lst), 0)
        count -= 1
    return lst