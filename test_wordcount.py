import unittest

from wordcount import count_words


class CountWordsTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_words("a b a"), {"a": 2, "b": 1})

    def test_case_insensitive(self):
        self.assertEqual(count_words("Hello hello"), {"hello": 2})

    def test_empty(self):
        self.assertEqual(count_words(""), {})


if __name__ == "__main__":
    unittest.main()
