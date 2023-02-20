def find_average(numbers):
    return sum(i if isinstance(i, int) else 0 for i in numbers) / len(numbers)