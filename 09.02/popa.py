def custom_string_to_int(ch: str) -> int:
    try:
        return int(ch)
    except ValueError:
        raise


print(custom_string_to_int("123"))  # Вывод: 123
print(custom_string_to_int("-456"))  # Вывод: -456
print(custom_string_to_int("0"))  # Вывод: 0
print(custom_string_to_int("-0"))  # Вывод: 0
custom_string_to_int("12a3")  # Должно вызвать ValueError
custom_string_to_int("")  # Должно вызвать ValueError