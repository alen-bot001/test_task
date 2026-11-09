"""Additional edge-case checks for the greeting test pathway.

Added by worker ``worker-97b066efba89e36d584e4cd86d8b0f1f``
(ticket ``add-more-test-code-97b066efba89``) on 2026-11-09, following the
request on issue #4.

Run the whole suite with:

    python3 -m unittest -v
"""

import unittest

import hello


class GreetingEdgeCaseTests(unittest.TestCase):
    def test_newlines_and_tabs_are_trimmed(self):
        self.assertEqual(hello.greet("\n\t Ada \t\n"), "Hello, Ada!")

    def test_ideographic_space_is_rejected(self):
        with self.assertRaises(ValueError):
            hello.greet("\u3000")

    def test_emoji_name_is_preserved(self):
        self.assertEqual(hello.greet("🤖"), "Hello, 🤖!")

    def test_default_name_is_non_empty_text(self):
        self.assertIs(type(hello.DEFAULT_NAME), str)
        self.assertTrue(hello.DEFAULT_NAME.strip())


if __name__ == "__main__":
    unittest.main()
