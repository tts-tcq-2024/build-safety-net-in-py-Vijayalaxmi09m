def get_soundex_code(c): 
    # Uppercase the character for uniform mapping
    c = c.upper()
    # Define a static dictionary for character mapping
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for vowels or unlisted characters

def filter_name(name):
    # Filters out unwanted characters (vowels, h, w, y) after the first character
    return [char for char in name[1:].upper() if char not in "AEIOUYHW"]

def generate_soundex(name):
    if not name:
        return ""

    # Retain first letter
    soundex = name[0].upper()

    # Filter the name to remove unnecessary letters
    filtered_name = filter_name(name)
    prev_code = get_soundex_code(soundex)

    # Convert filtered characters to soundex code
    for char in filtered_name:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex += code
            prev_code = code
        if len(soundex) == 4:
            break

    # Pad to ensure the length is 4
    return soundex.ljust(4, '0')
