#!/usr/bin/python3

def roman_to_int(roman_string):
    ''' converts a Roman numeral to an integer

        Args:
            @roman_string: roman representation
        Return:
            integer representation
    '''
    if roman_string is None or type(roman_string) != str:
        return 0

    int_sum = 0
    roman_numerals = {
                'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100,
                'D': 500, 'M': 1000}

    for idx in range(-1, -1 * (len(roman_string) + 1), -1):
        roman_char = roman_string[idx]

        if idx != -1:
            _roman_char = roman_string[idx + 1]
            if roman_numerals[roman_char] < roman_numerals[_roman_char]:
                int_sum -= roman_numerals[roman_char]
            else:
                int_sum += roman_numerals[roman_char]
        else:
            int_sum += roman_numerals[roman_char]

    return int_sum
