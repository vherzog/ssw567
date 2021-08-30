import unittest


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertTrue(sum([45, 45, 2]) == 92, "Should be 92")


if __name__ == '__main__':
    unittest.main()
