class Bank:
    """Handles various accounts."""

    def __init__(self, name, accNum, balance):
        self.name = name
        self.accNum = accNum
        self.balance = balance
        """Initializes and checks if arguements are correct data type."""
        if isinstance(name, str):
            pass
        else:
            print("Sorry, name must be a string.")
        if isinstance(accNum, int):
            pass
        else:
            print("Sorry, account number must be an integer.")
        if isinstance(balance, float):
            pass
        elif isinstance(balance, int):
            pass
        else:
            print("Sorry, balance must be a number.")

    def withdraw(self, ammount):
        """Withdraws money from account."""
        balance = round(self.balance, 2)
        am = round(ammount, 2)
        if am > self.balance:
            print("Sorry! You cannot withdraw that much.")
            return False
        elif am <= 0:
            print("What are you even doing, try again >:(")
            return False
        else:
            self.balance = balance - am
            self.balance = round(self.balance, 2)
            print("Withdrawal made! New balance is $" + str(self.balance) + ".")
            return self.balance

    def deposit(self, ammount):
        """Deposits money to account."""
        balance = round(self.balance, 2)
        am = round(ammount, 2)
        if am <= 0:
            print("What are you even doing, try again >:(")
            return False
        self.balance = balance + am
        print("Deposit made! New balance is $" + str(self.balance) + ".")
        return self.balance

    def checkBalance(self):
        """Returns account balance."""
        print("Your current balance is $" + str(self.balance) + ".")
        return self.balance
