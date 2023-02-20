def find_short(s):
    text = sorted(s.split(), key=len)
    return len(text[0])