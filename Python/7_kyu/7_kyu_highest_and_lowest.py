def high_and_low(numbers):
    numbers = numbers.split(' ')
    numbers = sorted(numbers, key=int)
    return f'{numbers[-1]} {numbers[0]}'