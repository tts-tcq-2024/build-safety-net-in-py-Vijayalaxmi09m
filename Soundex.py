def get_soundex_code(c):
    """Returns the Soundex digit for the given character."""
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # '0' for vowels or non-mapped characters


def should_encode(char):
    """Returns True if the character should be encoded."""
    return char.upper() not in "AEIOUYHW"  # Only consonants are encoded


def get_filtered_codes(name):
    """Returns a list of soundex codes for the characters, skipping unwanted characters."""
    return [get_soundex_code(char) for char in name[1:] if should_encode(char)]


def build_soundex(name):
    """Builds the soundex code based on the first letter and filtered codes."""
    if not name:
        return ""

    # Start with the first letter capitalized
    soundex = name[0].upper()
    filtered_codes = get_filtered_codes(name)
    
    prev_code = get_soundex_code(soundex)
    
    for code in filtered_codes:
        if code != prev_code and code != '0':  # Skip duplicates and '0' codes
            soundex += code
            prev_code = code
        if len(soundex) == 4:  # Stop once we have a letter and three digits
            break
    
    return soundex


def generate_soundex(name):
    """Main function that generates the Soundex code for the given name."""
    soundex = build_soundex(name)
    return soundex.ljust(4, '0')  # Pad with zeros if less than 4 characters
