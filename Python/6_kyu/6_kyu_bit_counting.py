def to_binary(number):
    sum = 0
    res = bin(number).replace("0b", "")
    for i in res:
        sum += int(i)
    return sum