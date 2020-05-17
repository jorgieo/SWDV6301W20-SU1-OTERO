import random
from datetime import datetime

class CheckingAccount:
    """
    Build and use a checking account.

    Args:
            uname(String) - Account owner name.
            [initialbalance(Float)] - Optional initial balance. Default = 50.0 dollars.

    Public Methods:
            deposit() - Adds to the account balance.
            withdraw() - Subtracts from the account balance.
    """

    def __init__(self, uname, initialbalance=50.0):
        self.uname = uname
        self.address = {}
        self.accountNum = self._generateAccountnum()
        self._balance = initialbalance
        self._ledger = []

    def _generateAccountnum(self):
        stringAccNo = ''
        for digit in range(9):
            stringAccNo += str(random.randint(0, 9))
        return stringAccNo

    def _is_overdrawn(self, amount):
        if self.getBanlance() - amount < 0:
            return True
        else:
            return False

    def _updateLedger(self, transactype, amount, status, balance):
        timestamp = datetime.now().strftime("%m/%d/%Y--%H:%M:%S")
        transaction = (timestamp, transactype, amount, status, balance)
        self._ledger.append(transaction)

    def deposit(self, amount):
        self._balance += amount
        self._updateLedger("DEPOSIT", amount, "SUCCESS", self.getBanlance())

    def withdraw(self, amount):
        if self._is_overdrawn(amount):
            print(f"Debit ${amount} declined: Insufficient Funds.")
            self._updateLedger("DEBIT", amount, "FAILED", self.getBanlance())
        else:
            self._balance -= amount
            self._updateLedger("DEBIT", amount, "SUCCESS", self.getBanlance())

    def getName(self):
        return self.uname

    def getBanlance(self):
        return self._balance

    def setAddress(self, street="", city="", state="", zipcode=""):
        self.address = {'street': street, 'city': city, 'state': state, 'zipcode': zipcode}

    def getAddress(self):
        return self.address

    def getAccountnum(self):
        return self.accountNum

    def getLedger(self):
        return self._ledger


if __name__ == '__main__':
    # Driver program functions:
    def printAccountowner(object):
        print(f"Account Owner: {object.getName()}")

    def printAccountno(object):
        print(f"Account Number: {object.getAccountnum()}")

    def printBalance(object):
        print(f"Your balance is: ${object.getBanlance():.2f}")

    def printAddrLabel(object):
        custAddress = object.getAddress()
        print("Customer Address:")
        print(f"{custAddress['street']}\n{custAddress['city']}, {custAddress['state']} {custAddress['zipcode']}")

    def printLedger(object):
        ledger = object.getLedger()
        print("Account Ledger:")
        print(f"{'Timestamp':24}{'Type':12}Amount\tStatus\tBalance")
        for transaction in ledger:
            print(f"{transaction[0]}\t{transaction[1]}\t\t{transaction[2]:.2f}\t{transaction[3]}\t{transaction[4]:.2f}")

    # Instance of Checking Account
    myChecking = CheckingAccount("John Smith")
    myChecking.setAddress(street="123 Main St", city="Springfield", state="FR", zipcode="99999")

    # Print basic account information
    print("Basic Account Information:")
    printAccountowner(myChecking)
    printAccountno(myChecking)
    printAddrLabel(myChecking)
    printBalance(myChecking)
    print()

    # Make transaction

    myChecking.deposit(525.50)
    printBalance(myChecking)
    myChecking.withdraw(35.25)
    printBalance(myChecking)
    myChecking.withdraw(650.75)
    printBalance(myChecking)
    myChecking.deposit(2000)
    printBalance(myChecking)
    myChecking.withdraw(3500.00)
    printBalance(myChecking)
    print()

    # Print the account ledger
    printLedger(myChecking)
