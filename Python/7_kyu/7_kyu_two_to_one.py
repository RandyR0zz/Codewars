def longest(a1, a2):
    s1 = "".join(set(a1))
    s2 = "".join(set(a2))
    s3 = s1 + s2
    s3 = set(s3)
    res = sorted(s3, key=str)
    return "".join(res)