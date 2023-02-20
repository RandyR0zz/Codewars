def zero_fuel(distance_to_pump, mpg, fuel_left):
    n = fuel_left * mpg
    if n < distance_to_pump:
        return False
    if n >= distance_to_pump:
        return True
