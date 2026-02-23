def rational_to_decimal(numerator: int, denominator: int, precision: int = None) -> str:

    sign = '' if (numerator * denominator > 0) else '-'

    integer_part = abs(numerator) // abs(denominator)
    remainder = abs(numerator) % abs(denominator)

    if remainder == 0:
        return sign + str(integer_part)
    
    decimal_part = []
    remainders= {}
    position = 0

    while remainder != 0 and remainder not in remainders:
        remainders[remainder] = position
        remainder *= 10
        decimal_part.append(str(remainder // denominator))
        remainder %= denominator
        position += 1

    if precision:
        if remainder == 0:
            decimal_part = decimal_part[:precision + 1]
            return f"{sign}{integer_part}.{''.join(decimal_part)}"
        
        else:
            repeat_start = remainders[remainder]
            if len(str(repeat_start)) > precision:
                non_repeating = ''.join(decimal_part[:precision])
                repeating = ''.join(decimal_part[repeat_start:])
            else:
                non_repeating = ''.join(decimal_part[:repeat_start])
                repeating = ''.join(decimal_part[repeat_start:precision + 1])
            
            if non_repeating:
                return f"{sign}{integer_part}.{non_repeating}({repeating})"
            else:
                return f"{sign}{integer_part}.({repeating})"
            
    else:
        if remainder == 0:
            return f"{sign}{integer_part}.{''.join(decimal_part)}"
        
        else:
            repeat_start = remainders[remainder]
        
            non_repeating = ''.join(decimal_part[:repeat_start])
            repeating = ''.join(decimal_part[repeat_start:])
            
            if non_repeating:
                return f"{sign}{integer_part}.{non_repeating}({repeating})"
            else:
                return f"{sign}{integer_part}.({repeating})"
            

print(rational_to_decimal(1, 2))  # Вывод: "0.5"
print(rational_to_decimal(1, 3))  # Вывод: "0.(3)"
print(rational_to_decimal(5, 6))  # Вывод: "0.8(3)"
print(rational_to_decimal(2, 7, 5))  # Вывод: "-0.25"
print(rational_to_decimal(1, 7, 18))  # Вывод: "0.(142857)..."

