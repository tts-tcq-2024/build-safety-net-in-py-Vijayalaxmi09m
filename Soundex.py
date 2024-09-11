def get_character_mapping():
    return {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }

def get_soundex_code(c):
    return get_character_mapping().get(c.upper(), '0')  # '0' for vowels or non-mapped characters


def should_ignore(c):
    return c.upper() in "AEIOUYHW"


def filter_and_map_name(name):
    return [get_soundex_code(c) for c in name[1:] if not should_ignore(c)]


def build_soundex_from_codes(soundex, codes):
    prev_code = get_soundex_code(soundex[0])
    
    for code in codes:
        if code != prev_code and code != '0':  # Skip duplicates and '0' codes
            soundex.append(code)
            prev_code = code
        if len(soundex) == 4:  # Stop when we have one letter and three digits
            break
    
    return soundex


def generate_soundex(name):
    if not name:
        return ""

    soundex = [name[0].upper()]  # Keep the first letter as is
    codes = filter_and_map_name(name)  # Filter valid characters and convert to Soundex digits
    soundex = build_soundex_from_codes(soundex, codes)  # Build the soundex

    return ''.join(soundex).ljust(4, '0')  # Ensure the result has a length of 4
