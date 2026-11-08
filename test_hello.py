"""Tests for hello.py.

Run them with:

    python3 -m unittest -v
"""

import unittest

import hello


class GreetTests(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(hello.greet(), "Hello, alen-bot001!")

    def test_custom_name(self):
        self.assertEqual(hello.greet("World"), "Hello, World!")

    def test_surrounding_whitespace_is_trimmed(self):
        self.assertEqual(hello.greet("  alen  "), "Hello, alen!")

    def test_empty_name_is_rejected(self):
        for value in ("", "   "):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    hello.greet(value)

    def test_non_string_name_is_rejected(self):
        with self.assertRaises(TypeError):
            hello.greet(42)


if __name__ == "__main__":
    unittest.main()
