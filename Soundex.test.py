import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        """Test that an empty string returns an empty Soundex code."""
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        """Test that a single character returns the character padded with zeros."""
        self.assertEqual(generate_soundex("A"), "A000")

    def test_similar_consonants(self):
        """Test that similar consonants return the correct code."""
        self.assertEqual(generate_soundex("BFPV"), "B100")
        self.assertEqual(generate_soundex("CGJKQSXZ"), "C200")
        self.assertEqual(generate_soundex("DT"), "D300")
        self.assertEqual(generate_soundex("L"), "L400")
        self.assertEqual(generate_soundex("MN"), "M500")
        self.assertEqual(generate_soundex("R"), "R600")

    def test_vowels_and_ignored_characters(self):
        """Test that vowels and ignored characters are correctly excluded."""
        self.assertEqual(generate_soundex("AEIOUYHW"), "A000")
        self.assertEqual(generate_soundex("BOAT"), "B300")

    def test_repeating_characters(self):
        """Test that repeating characters with the same code are treated as one."""
        self.assertEqual(generate_soundex("BB"), "B000")
        self.assertEqual(generate_soundex("SS"), "S000")
        self.assertEqual(generate_soundex("FF"), "F000")

    def test_name_padding(self):
        """Test that names shorter than 4 characters are padded with zeros."""
        self.assertEqual(generate_soundex("Bo"), "B000")
        self.assertEqual(generate_soundex("Ga"), "G000")
        self.assertEqual(generate_soundex("Li"), "L000")

    def test_full_soundex_generation(self):
        """Test that full Soundex codes are generated correctly."""
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Tymczak"), "T522")
    

if __name__ == '__main__':
    unittest.main()
