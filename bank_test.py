import unittest
import Bank
import numpy as np


class TestHello(unittest.TestCase):
    def test_withdraw(self):
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertEqual(beanBank.withdraw(100), 0)
        self.assertNotEqual(beanBank.withdraw(100), 8)


if __name__ == "__main__":
    unittest.main()
