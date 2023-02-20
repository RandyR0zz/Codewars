def filter_list(l):
    res = []
    for i in l:
        if isinstance(i, int):
            res.append(i)
    return res 