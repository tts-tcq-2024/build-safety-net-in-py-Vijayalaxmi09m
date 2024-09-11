def get_soundex_code(c):
    """Returns the Soundex digit for the given character."""
    return {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }.get(c.upper(), '0')  # '0' for vowels or non-mapped characters


def should_encode(c):
    """Returns True if the character should be encoded."""
    return c.upper() not in "AEIOUYHW"  # Only consonants are encoded


def filter_codes(name):
    """Filters name to return a list of codes for the valid characters."""
    return [get_soundex_code(c) for c in name[1:] if should_encode(c)]


def build_soundex(name):
    """Builds the Soundex code based on the first letter and filtered codes."""
    if not name:
        return ""
    
    # Get the first letter and initialize Soundex code with it
    soundex = [name[0].upper()]
    
    # Get filtered codes and track the previous code to avoid duplicates
    codes = filter_codes(name)
    prev_code = get_soundex_code(soundex[0])

    for code in codes:
        if code != prev_code and code != '0':  # Only add non-duplicate, valid codes
            soundex.append(code)
            prev_code = code
        if len(soundex) == 4:  # Stop once we have a letter and three digits
            break
    
    return ''.join(soundex)


def generate_soundex(name):
    """Generates and returns the final Soundex code."""
    return build_soundex(name).ljust(4, '0')  # Pad with zeros if needed
