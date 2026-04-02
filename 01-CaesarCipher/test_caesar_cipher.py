import unittest

from caesar_cipher import decrypt, encrypt


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_basic(self) -> None:
        self.assertEqual(encrypt("ABC", 3), "DEF")
        self.assertEqual(encrypt("xyz", 3), "abc")

    def test_decrypt_basic(self) -> None:
        self.assertEqual(decrypt("DEF", 3), "ABC")
        self.assertEqual(decrypt("abc", 3), "xyz")

    def test_negative_shift(self) -> None:
        # encrypt with negative shift == decrypt with positive shift
        self.assertEqual(encrypt("ABC", -3), decrypt("ABC", 3))

    def test_case_and_non_alpha(self) -> None:
        self.assertEqual(encrypt("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(decrypt("Khoor, Zruog!", 3), "Hello, World!")

    def test_shift_mod_26(self) -> None:
        self.assertEqual(encrypt("ABC", 26), "ABC")
        self.assertEqual(encrypt("ABC", 52), "ABC")


if __name__ == "__main__":
    unittest.main()

