def roman_to_int(roman):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman (str): the Roman numeral to convert

    Returns:
        The integer value of the Roman numeral, or None if the input is invalid.
    """
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    prev_value = 0
    total = 0

    for letter in roman:
        value = values.get(letter, None)
        if value is None:
            return None

        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value

        prev_value = value

    return total

# Example usage
roman_numerals = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']

for roman in roman_numerals:
    result = roman_to_int(roman)
    if result is not None:
        print(f"{roman} is {result}")
    else:
        print(f"{roman} is not a valid Roman numeral")
