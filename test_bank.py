import unittest
import Bank
import numpy as np
import random


class TestHello(unittest.TestCase):
    def test_withdraw(self):  # Testing withdraw method
        beanBank = Bank.Bank("Test_Acc", 1, 100)  # Bean Bank :D (for testing purposes)
        self.assertEqual(
            beanBank.name, "Test_Acc"
        )  # making sure the account name is what it's supposed to be
        self.assertEqual(beanBank.accNum, 1)  # same for the account number
        self.assertEqual(beanBank.balance, 100)  # and the account balance
        self.assertEqual(beanBank.withdraw(100), 0)  # tests withdrawing valid ammount
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertNotEqual(
            beanBank.withdraw(100), 8
        )  # and makes sure the balance isn't what it shouldn't be
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertNotEqual(
            beanBank.withdraw(-100), 200
        )  # making sure you can't withdraw negative ammounts
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertEqual(
            beanBank.withdraw(101), False
        )  # making sure you can't withdraw more than the balance
        beanBank = Bank.Bank("Test_Acc", 1, 100.722976785)
        self.assertEqual(
            beanBank.withdraw(18.93262626), 81.79
        )  # testing rounding to cents
        beanBank = Bank.Bank("Test_Acc", 1, 100.722976785)
        self.assertEqual(
            beanBank.withdraw(0), False
        )  # making sure you can't withdraw 0

    def test_deposit(self):  # testing depositing
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertEqual(beanBank.deposit(100), 200)  # normal deposit test
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertNotEqual(beanBank.deposit(100), 8)  # balance isn't what it's not
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertNotEqual(
            beanBank.deposit(-95), 5
        )  # can't deposit negative #s (making sure it doesn't adjust balance)
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        self.assertEqual(
            beanBank.deposit(-101), False
        )  # making sure neg. deposit returns false
        beanBank = Bank.Bank("Test_Acc", 1, 100.722976785)
        self.assertEqual(beanBank.deposit(18.93262626), 119.65)
        beanBank = Bank.Bank("Test_Acc", 1, 100.722976785)  # rounding
        self.assertEqual(beanBank.deposit(0), False)  # no depositing 0

    n = 1

    def test_checkBalance(self):  # testing depositing
        beanBank = Bank.Bank("Test_Acc", 1, 100)
        while n < 7:
            x = random.randint(
                -1000000000, 1000000000
            )  # tests checkbalance with random integers
            beanBank = Bank.Bank("Test_Acc", 1, x)
            if x < 0:
                self.assertEqual(beanBank.checkBalance(), False)
                self.assertNotEqual(beanBank.checkBalance(), x)
            else:
                self.assertEqual(beanBank.checkBalance(), x)
                self.assertNotEqual(
                    beanBank.checkBalance(), x + random.randint(268, 975)
                )
            n += 1


if __name__ == "__main__":
    unittest.main()
