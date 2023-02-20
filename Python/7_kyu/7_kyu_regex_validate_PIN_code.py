def validate_pin(pin):
    if len(pin) == 4:
        if pin.isdigit():
            return True
        else:
            return False
    elif len(pin) == 6:
        if pin.isdigit():
            return True
        else:
            return False
    else:
        return False