import unittest
import hello
import numpy as np


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "Bye, world!")

    def test_sin(self):
        randomFloat = np.random.uniform(low=-4 * 3.1416, high=4 * 3.1416)
        self.assertEqual(hello.sin(randomFloat), np.sin(randomFloat))

    def test_cos(self):
        randomFloat = np.random.uniform(low=-4 * 3.1416, high=4 * 3.1416)
        self.assertEqual(hello.cos(randomFloat), np.cos(randomFloat))

    def test_tan(self):
        randomFloat = np.random.uniform(low=-4 * 3.1416, high=4 * 3.1416)
        self.assertEqual(hello.tan(randomFloat), np.tan(randomFloat))

    def test_cot(self):
        randomFloat = np.random.uniform(low=-4 * 3.1416, high=4 * 3.1416)
        self.assertEqual(hello.cot(randomFloat), 1 / np.tan(randomFloat))


if __name__ == "__main__":
    unittest.main()
