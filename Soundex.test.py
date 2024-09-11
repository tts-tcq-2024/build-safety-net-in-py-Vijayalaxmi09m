import unittest
from soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_vowels_removed(self):
        self.assertEqual(generate_soundex("AeIoU"), "A000")

    def test_h_w_y_ignored(self):
        self.assertEqual(generate_soundex("AhWsy"), "A200")

    def test_duplicate_encodings(self):
        self.assertEqual(generate_soundex("Abbot"), "A130")

    def test_special_characters(self):
        self.assertEqual(generate_soundex("Bcd@#E"), "B230")

    def test_names_with_h_w_vowels_between_same_digit_letters(self):
        self.assertEqual(generate_soundex("Ashcroft"), "A261")

    def test_padding_zeros(self):
        self.assertEqual(generate_soundex("G"), "G000")
        self.assertEqual(generate_soundex("Pfister"), "P236")
    
if __name__ == '__main__':
    unittest.main()
