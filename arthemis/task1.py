from typing import List


def compress_string(input_string: str) -> str:

    if not input_string:
        return ""

    res = []
    count = 1
    i = 1 

    while i < len(input_string):
        
        if input_string[i - 1] == input_string[i]:
            
            count += 1
            if count == 2:
                res.append(input_string[i])
                res.append('(')

        elif count > 1 and input_string[i - 1] != input_string[i]:
            res.append(f"{count}")
            res.append(')')
            count = 1
        
        else:
            res.append(input_string[i - 1])
        
        i += 1

    if count > 1:
        res.append(f"{count}")
        res.append(')')
    else:
        res.append(input_string[-1])

    return ''.join(res)




def decompress_string(compressed_string: str) -> str:
    if not compressed_string:
        return ""

    res = []
    i = 0

    while i < len(compressed_string):
        char = compressed_string[i]

        if i + 1 < len(compressed_string) and compressed_string[i + 1] == '(':
            j = i + 2
            num_str = ""
            while j < len(compressed_string) and compressed_string[j] != ')':
                num_str += compressed_string[j]
                j += 1
            count = int(num_str)
            res.append(char * count)
            i = j + 1 
        else:
            res.append(char)
            i += 1

    return "".join(res)
        

        