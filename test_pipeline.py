"""End-to-end checks for the greeting path exercised by the test pipeline.

These complement ``test_hello.py`` by asserting the shape of the rendered
result and the name handling that the issue-to-PR automation relies on.
Run the whole suite with:

    python3 -m unittest -v
"""

import unittest

import hello


class GreetingPipelineTests(unittest.TestCase):
    def test_non_ascii_name_is_preserved(self):
        self.assertEqual(hello.greet("张三"), "Hello, 张三!")

    def test_internal_whitespace_is_kept(self):
        self.assertEqual(hello.greet("  Ada Lovelace  "), "Hello, Ada Lovelace!")

    def test_greeting_is_plain_text(self):
        greeting = hello.greet("pipeline")
        self.assertIs(type(greeting), str)
        self.assertEqual(greeting, "Hello, pipeline!")

    def test_default_name_matches_constant(self):
        self.assertEqual(hello.greet(), hello.greet(hello.DEFAULT_NAME))


if __name__ == "__main__":
    unittest.main()
