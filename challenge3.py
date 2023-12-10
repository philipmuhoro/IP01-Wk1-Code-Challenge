def solve(s):
    vowels = 'aeiou'
    # Create a dictionary
    consonant_values = {letter: i + 1 for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz')}
    
    max_consonant_value = 0
    current_consonant_value = 0
    
    for char in s:
        if char not in vowels:
            current_consonant_value += consonant_values[char]
        else:
            max_consonant_value = max(max_consonant_value, current_consonant_value)
            current_consonant_value = 0

    # Double checks if the string ends with a consonant sub-string
    max_consonant_value = max(max_consonant_value, current_consonant_value)

    return max_consonant_value

# Examples
print(solve("zodiacs"))    # Output: 26
print(solve("strength"))   # Output: 57
