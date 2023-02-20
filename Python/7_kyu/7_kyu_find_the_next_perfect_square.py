from math import sqrt

def find_next_square(sq):
    if sqrt(sq) % int(sqrt(sq)) == 0:
        return (int(sqrt(sq)) + 1)**2
    else:
        return -1