def xo(s):
    x1 = sum(map(lambda x : 1 if 'x' in x else 0, s))
    o1 = sum(map(lambda x : 1 if 'o' in x else 0, s))
    x2 = sum(map(lambda x : 1 if 'X' in x else 0, s))
    o2 = sum(map(lambda x : 1 if 'O' in x else 0, s))
    x = x1 + x2
    o = o1 + o2
    if x == o:
        return True
    else:
        return False