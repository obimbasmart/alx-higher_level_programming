#!/usr/bin/python3

def roman_to_int(roman_string):
    ''' converts a Roman numeral to an integer
        Args:
            @roman_string: roman representation
        Return:
            integer representation
    '''
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
                'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100,
                'D': 500, 'M': 1000}

    int_sum = 0
    if (len(roman_string) == 1):
        return (roman_numerals[roman_string])

    int_sum += roman_numerals[roman_string[-1]]
    # loop the roman_string in reverse order, starting from
    # the second to last numeral(-2). for each numeral we add the integer
    # equivalent, and also take note if the numeral behind it(right)
    # is greater or less, in any case we add or subtract
    for idx in range(-2, -1 * (len(roman_string) + 1), -1):
        roman_char = roman_string[idx]
        next_roman_char = roman_string[idx + 1]
        if (roman_numerals[roman_char] < roman_numerals[next_roman_char]):
            int_sum -= roman_numerals[roman_char]
        else:
            int_sum += roman_numerals[roman_char]
    return int_sum
