def is_valid_compressed_string(compressed_string: str) -> bool:
    
    if not compressed_string:
        return True
    
    if compressed_string[0] in '()' or '(03' in compressed_string or '()' in compressed_string:
        return False
    
    bracket = False 
    
    for i in range(1, len(compressed_string)):
        
        if compressed_string[i] == '(':
            if compressed_string[i - 1] in '()':
                return False
            bracket = True

        if bracket and compressed_string[i].isalpha():
            return False
        
        if (not bracket and compressed_string[i] == ')'):
            return False
        
        if compressed_string[i] == ')':
            bracket = False

    return not bracket



