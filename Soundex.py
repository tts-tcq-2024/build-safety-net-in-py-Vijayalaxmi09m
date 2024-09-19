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
    return get_character_mapping().get(c.upper(), '0')


def is_consonant(c):
    return get_soundex_code(c) != '0'


def is_valid_for_mapping(c):
    return not should_ignore(c)


def should_ignore(c):
    return c.upper() in "AEIOUYHW"


def get_filtered_codes(name):
    return [get_soundex_code(c) for c in name[1:] if is_valid_for_mapping(c)]


def append_code_if_needed(soundex, code, prev_code):
    if code != prev_code and code != '0':
        soundex.append(code)
    return soundex


def build_soundex_from_codes(soundex, codes):
    prev_code = get_soundex_code(soundex[0])
    for code in codes:
        soundex = append_code_if_needed(soundex, code, prev_code)
        prev_code = code
        if len(soundex) == 4:
            break
    return soundex


def generate_soundex(name):
    if not name:
        return ""

    soundex = [name[0].upper()]
    codes = get_filtered_codes(name)
    soundex = build_soundex_from_codes(soundex, codes)

    return ''.join(soundex).ljust(4, '0')
