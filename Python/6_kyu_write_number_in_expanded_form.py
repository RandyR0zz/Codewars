def expanded_form(num):
    res = []
    for index, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            res.append(digit + ('0' * index))
    return ' + '.join(res[::-1])