def nb_year(p0, percent, aug, p):
    current = p0
    year = 0
    while current < p:
        current = int(current + (current * percent / 100) + aug)
        year += 1
    return year