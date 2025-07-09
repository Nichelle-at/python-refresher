import unittest
import Bank
import numpy as np


class TestHello(unittest.TestCase):
    def test_withdraw(self):
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertEqual(beanBank.withdraw(100), 0)
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertNotEqual(beanBank.withdraw(100), 8)
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertNotEqual(beanBank.withdraw(-100), 200)
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertEqual(beanBank.withdraw(101), False)
        beanBank = Bank.Bank("Test_Acc", 1, 100.722976785)
        self.assertEqual(beanBank.withdraw(18.93262626), 81.79)
        beanBank = Bank.Bank("Test_Acc", 1, 100.722976785)
        self.assertEqual(beanBank.withdraw(0), False)

    def test_deposit(self):
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertEqual(beanBank.deposit(100), 200)
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertNotEqual(beanBank.deposit(100), 8)
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertNotEqual(beanBank.deposit(-95), 5)
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertEqual(beanBank.deposit(-101), False)
        beanBank = Bank.Bank("Test_Acc", 1, 100.722976785)
        self.assertEqual(beanBank.deposit(18.93262626), 119.65)
        beanBank = Bank.Bank("Test_Acc", 1, 100.722976785)
        self.assertEqual(beanBank.deposit(0), False)


if __name__ == "__main__":
    unittest.main()
