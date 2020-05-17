import random
import time

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
        self._overdrawnflag = False

    def _generateAccountnum(self):
        stringAccNo = ''
        for digit in range(9):
            stringAccNo += str(random.randint(0, 9))
        return stringAccNo

    def _is_overdrawn(self):
        if self.getBanlance() < 0:
            self._overdrawnflag = True
            return True
        else:
            self._overdrawnflag = False
            return False

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._is_overdrawn():
            print("Declined: Insufficient Funds")
        else:
            self._balance -= amount


    def getBanlance(self):
        return self._balance

    def setAddress(self, street="", city="", state="", zipcode=""):
        self.address = {'street': street, 'city': city, 'state': state, 'zipcode': zipcode}

    def getAddress(self):
        return self.address

    def getAccountnum(self):
        return self.accountNum


if __name__ == '__main__':
    # Driver program functions:
    def printAccountno(object):
        print(f"Account Number: {object.getAccountnum()}")

    def printBalance(object):
        print(f"Your balance is: ${object.getBanlance():.2f}")

    def printAddrLabel(object):
        custAddress = object.getAddress()
        print("Customer Address:")
        print(f"{custAddress['street']}\n{custAddress['city']}, {custAddress['state']} {custAddress['zipcode']}")

    # Instance of Checking Account
    myChecking = CheckingAccount("John Smith")
    myChecking.setAddress(street="123 Main St", city="Springfield", state="FR", zipcode="99999")

    # Print basic account information
    printAccountno(myChecking)
    printAddrLabel(myChecking)
    printBalance(myChecking)

    # Make transaction
    myChecking.deposit(525.50)
    printBalance(myChecking)
    myChecking.withdraw(35.25)
    printBalance(myChecking)
