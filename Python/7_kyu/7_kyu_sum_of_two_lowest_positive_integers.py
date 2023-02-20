def sum_two_smallest_numbers(numbers):
    lowest = sorted(numbers, key=int)
    return lowest[0]+lowest[1] 