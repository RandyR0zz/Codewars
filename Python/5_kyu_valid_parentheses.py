def valid_parentheses(string):
    counter = 0
    
    for character in string:
        if character == '(':
            counter += 1
            
        if character == ')':
            counter -= 1
            
        if counter < 0:
            return False
        
    return counter == 0