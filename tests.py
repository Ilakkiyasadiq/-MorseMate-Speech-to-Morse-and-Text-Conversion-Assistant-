import unittest
from morse_converter import convert_morse

class TestMorseConverter(unittest.TestCase):
    def test_convert_morse(self):
        self.assertEqual(convert_morse("Hello"), ".... . .-.. .-.. ---")
        self.assertEqual(convert_morse("SOS"), "... --- ...")
        self.assertEqual(convert_morse("123"), ".---- ..--- ...--")
        self.assertEqual(convert_morse("Invalid"), ".. -. ...- .- .-.. .. -..")

if __name__ == "__main__":
    unittest.main()
