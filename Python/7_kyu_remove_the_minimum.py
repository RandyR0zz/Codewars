def remove_smallest(numbers):
    arr = numbers.copy()
    if len(arr) < 1:
        return arr
    else:
        arr.remove(min(arr))
    return arr