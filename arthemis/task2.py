from itertools import cycle


def caesar_encrypt(plaintext: str, keyword: str) -> str:
    res = ''
    key_iter = cycle(keyword.lower())
    
    for char in plaintext:
        if char.isalpha():
            script = next(key_iter)
            curr_symbol = chr((ord(char.lower()) - 97 + ord(script) - 97) % 26 + 97)
            res += curr_symbol.upper() if char.isupper() else curr_symbol
        else:
            res += char  
    
    return res


def caesar_decrypt(ciphertext: str, keyword: str) -> str:

    res = ''
    key_iter = cycle(keyword.lower())
    
    for char in ciphertext:
        if char.isalpha():
            script = next(key_iter)
            curr_symbol = chr((ord(char.lower()) - ord(script)) % 26 + 97)
            res += curr_symbol.upper() if char.isupper() else curr_symbol
        else:
            res += char  
    
    return res

