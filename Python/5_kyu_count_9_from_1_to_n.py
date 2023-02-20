def count_nines(n):
    if n < 10: return (n==9)
    s = str(n)
    x, y, l = int(s[0]), int(s[1:]), len(s)
    return (x==9)*(y+1) + count_nines(y) + x*(l-1)*10**(l-2)