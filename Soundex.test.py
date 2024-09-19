import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def assert_soundex(self, name, expected):
        """Helper method to simplify assertions."""
        self.assertEqual(generate_soundex(name), expected)

    def test_empty_string(self):
        """Test that an empty string returns an empty Soundex code."""
        self.assert_soundex("", "")

    def test_single_character(self):
        """Test that a single character returns the character padded with zeros."""
        cases = [("A", "A000"), ("B", "B000"), ("C", "C000")]
        for name, expected in cases:
            self.assert_soundex(name, expected)

    def test_similar_consonants(self):
        """Test that similar consonants return the correct code."""
        cases = [
            ("BFPV", "B100"),
            ("CGJKQSXZ", "C200"),
            ("DT", "D300"),
            ("L", "L400"),
            ("MN", "M500"),
            ("R", "R600"),
        ]
        for name, expected in cases:
            self.assert_soundex(name, expected)

    def test_vowels_and_ignored_characters(self):
        """Test that vowels and ignored characters are correctly excluded."""
        cases = [("AEIOUYHW", "A000"), ("BOAT", "B300")]
        for name, expected in cases:
            self.assert_soundex(name, expected)

    def test_repeating_characters(self):
        """Test that repeating characters with the same code are treated as one."""
        cases = [("BB", "B000"), ("SS", "S000"), ("FF", "F000")]
        for name, expected in cases:
            self.assert_soundex(name, expected)

    def test_name_padding(self):
        """Test that names shorter than 4 characters are padded with zeros."""
        cases = [("Bo", "B000"), ("Ga", "G000"), ("Li", "L000")]
        for name, expected in cases:
            self.assert_soundex(name, expected)

    def test_full_soundex_generation(self):
        """Test that full Soundex codes are generated correctly."""
        cases = [
            ("Robert", "R163"),
            ("Rupert", "R163"),
            ("Ashcraft", "A261"),
            ("Tymczak", "T522"),
        ]
        for name, expected in cases:
            self.assert_soundex(name, expected)

if __name__ == '__main__':
    unittest.main()
