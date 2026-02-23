from typing import List, Dict

def create_adfgvx_square(square_2d: list) -> dict:

    adfgvx_square = {}

    top_row = square_2d[0]
    square_2d.remove(top_row)

    for row in range(6):
        for column in range(6):
            
            curr_letter = square_2d[row][column + 1]
            adfgvx_square[curr_letter] = square_2d[row][0] + top_row[column]

    return adfgvx_square


def adfgvx_encrypt(plaintext: str, key: str, square: dict) -> str:
    
    encrypt_line = ""
    result = ""

    for ch in plaintext:
        if ch not in square:
            continue
        encrypt_line += square[ch]

    cypher = [[x] for x in key]

    for index, ch in enumerate(encrypt_line):
        cypher[index % len(key)].append(ch)

    cypher = sorted(cypher, key=lambda x: x[0])

    for block in cypher:
        result += "".join(block[1:])

    return result


def adfgvx_decrypt(ciphertext: str, key: str, square: dict) -> str:
    
    reverse_square = {v: k for k, v in square.items()}
    
    n = len(key)
    total = len(ciphertext)
    long_cols = total % n 
    col_len = total // n
    
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    
    columns = {}
    pos = 0
    for rank, (orig_idx, letter) in enumerate(sorted_key):
        length = col_len + (1 if rank < long_cols else 0)
        columns[orig_idx] = list(ciphertext[pos:pos+length])
        pos += length
    
    encrypt_ch = ""
    max_len = max(len(v) for v in columns.values())
    for row in range(max_len):
        for col in range(n):
            if row < len(columns[col]):
                encrypt_ch += columns[col][row]

    result = ""
    for i in range(0, len(encrypt_ch), 2):
        result += reverse_square[encrypt_ch[i] + encrypt_ch[i+1]]
    
    return result

