import unittest

from hello import hello


class HelloTest(unittest.TestCase):
    def test_default(self):
        self.assertEqual(hello(), "Hello, World!")

    def test_name(self):
        self.assertEqual(hello("Yuki"), "Hello, Yuki!")


if __name__ == "__main__":
    unittest.main()
