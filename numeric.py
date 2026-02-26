def roman_to_int(s):
    """
    Convert a Roman numeral string to an integer with validation.
    
    Args:
        s (str): Roman numeral string (e.g., 'IV', 'IX', 'MCMXC')
        
    Returns:
        int: The integer value of the Roman numeral
        
    Raises:
        ValueError: If the input contains invalid Roman numeral patterns
    """
    if not s:
        return 0
        
    # Validate the Roman numeral format
    def validate_roman_numeral(roman):
        import re
        
        # Check for invalid characters
        if not re.match(r'^[IVXLCDM]+$', roman.upper()):
            raise ValueError(f"Invalid Roman numeral character in: {roman}")
        
        # Check for invalid repetitions
        # I, X, C can repeat up to 3 times
        if re.search(r'I{4,}|X{4,}|C{4,}', roman.upper()):
            raise ValueError(f"Invalid repetition in Roman numeral: {roman}")
        
        # V, L, D should never repeat
        if re.search(r'V{2,}|L{2,}|D{2,}', roman.upper()):
            raise ValueError(f"Invalid repetition in Roman numeral: {roman}")
        
        # Check for invalid subtractive combinations
        # Valid subtractive: IV, IX, XL, XC, CD, CM
        # Invalid: IL, IC, ID, IM, VL, VC, VD, VM, etc.
        invalid_patterns = [
            r'IL', r'IC', r'ID', r'IM',  # I can only subtract from V and X
            r'VL', r'VC', r'VD', r'VM',  # V cannot be subtractive
            r'XD', r'XM',                # X can only subtract from L and C
            r'LC', r'LD', r'LM',         # L cannot be subtractive
            r'DM'                        # D cannot be subtractive
        ]
        
        for pattern in invalid_patterns:
            if re.search(pattern, roman.upper()):
                raise ValueError(f"Invalid subtractive combination in Roman numeral: {roman}")
    
    # Validate the input
    validate_roman_numeral(s)
    
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(s.upper()):
        curr_value = roman_numerals[char]
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value
        prev_value = curr_value
    return total

def written_number_to_int(s):
    written_numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }
    return written_numbers.get(s, None)

# Test the functions
if __name__ == "__main__":
    # Test Roman numeral conversion
    print("Roman numeral tests:")
    print(f"IV = {roman_to_int('IV')}")
    print(f"IX = {roman_to_int('IX')}")
    print(f"LVIII = {roman_to_int('LVIII')}")
    print(f"MCMXC = {roman_to_int('MCMXC')}")
    
    # Test invalid Roman numerals
    print("\nTesting invalid Roman numerals:")
    invalid_cases = ["IIII", "VV", "LLLL", "IC", "VL"]
    for case in invalid_cases:
        try:
            result = roman_to_int(case)
            print(f"{case} = {result} (unexpected - should be invalid)")
        except ValueError as e:
            print(f"{case} -> Error: {e}")
    
    # Test written number conversion
    print("\nWritten number tests:")
    print(f"one = {written_number_to_int('one')}")
    print(f"five = {written_number_to_int('five')}")
    print(f"ten = {written_number_to_int('ten')}")
    print(f"invalid = {written_number_to_int('invalid')}")
    print(f"negative one = {written_number_to_int('negative one')}")
