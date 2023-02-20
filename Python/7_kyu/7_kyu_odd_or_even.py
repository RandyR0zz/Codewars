def odd_or_even(arr):
    res = sum(i for i in arr)
    if res % 2 == 0:
        return "even"
    elif res % 2 != 0:
        return "odd"
    else:
        return "even"