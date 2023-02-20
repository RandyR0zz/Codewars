def to_jaden_case(string):
    text = string.split(" ")
    jaden_case = []
    for word in text:
        jaden_case.append(word.capitalize())
    return " ".join(jaden_case)