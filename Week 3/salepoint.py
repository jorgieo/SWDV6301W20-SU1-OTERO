# Point of sale (POS) module
# By Jorge Otero
# For SWDV630

from datetime import datetime
import secrets

ITEM_DATABASE = {'bananas': 0.60,
                 'apples': 0.90,
                 'kumquats': 3.50,
                 'carrots': 1.75,
                 'grapes': 2.98,
                 'corn': 1.75}

class Inventory:
    def __init__(self,inventory):
        self.inventory = inventory

    def getInventory(self):
        return self.inventory

class Transaction:
    """
    Super class for all transaction types.
    On instantiation system time is used to tag the object and a 32-character hexadecimal code
    is automatically generated.
    Attributes:
            timestamp: system date and time.
            transID: 32 random hex characters.
            description: dictionary of transaction object attributes.
                'timestamp': timestamp attribute
                'id': transID attribute
                'type': transaction type
                'items': items involved in the transaction
    """
    def __init__(self):
        self.timestamp = self._timetag()
        self.transID = self._generate_ID()
        self.description = {'timestamp': self.timestamp,
                            'id': self.transID,
                            'type': '',
                            'items': []}
        self.inventory = Inventory(ITEM_DATABASE)

    def _generate_ID(self):
        """
        Automatic ID generator.
        """
        return secrets.token_hex(16)

    def _timetag(self):
        """
        Autimatic time stamp.
        """
        return datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    def getDescription(self):
        """
        Returns a description of the transaction.
        """
        return self.description

    def getDate(self):
        """
        Returns the time stamp of the transaction.
        """
        return self.timestamp

    def getID(self):
        return self.transID

    def setType(self, type):
        self.description['type'] = type

class Sale(Transaction):
    """
    Sale transaction class.
    """
    def __init__(self):
        super().__init__()
        self.setType("SALE")

    def addItems(self, *args):
        for item in args:
            self.description['items'].append(item)

    def removeItems(self, item):
        if item in self.description['items']:
            self.description['items'].remove(item)
        else:
            print(f"Item '{item}' not found!")

    def getSoldItems(self):
        return self.getDescription()['items']

class Return(Transaction):
    """
    Return transaction class.
    """
    def __init__(self, sale_object):
        super().__init__()
        self.setType("RETURN")
        self.sale_object = sale_object
        self.returns = []

    def returnItems(self, *items):
        for item in items:
            if item in self.sale_object.description['items']:
                self.returns.append(item)
            else:
                print(f"Item '{item}' not found! Check the entry and try again.")
        return self.returns

    def storeCredit(self):
        credit = 0
        for item in self.returns:
            if item in self.inventory.getInventory().keys():
                credit += self.inventory.getInventory()[item]
        return credit

class Exchange(Transaction):

    def __init__(self, sale_object):
        super().__init__()
        self.setType("EXCHANGE")
        self.sale_object = sale_object
        self.sold_items = sale_object.getSoldItems()
        self.newSale = Sale()

    def getSoldItems(self):
        return self.sold_items

    def tradeItems(self, old_items, new_items):
        for item in old_items:
            if item in self.sold_items:
                self.sale_object.removeItems(item)
            else:
                print(f"Item '{item}' not found! Check the entry and try again.")

        for item in self.sale_object.description['items']:
            self.description['items'].append(item)
        for item in new_items:
            self.description['items'].append(item)


    def getNewSale(self):
        return self.newSale


if __name__ == '__main__':

    # Instance of Sale
    sale1 = Sale()

    print("\nSale object's date and ID:")
    print(sale1.getDate())
    print(sale1.getID())
    sale1.addItems('bananas','apples', 'kumquats', 'corn')

    print("\nSale object's oescription:")
    print(sale1.getDescription())

    print("\nSale object's list of sold items:")
    print(sale1.getSoldItems())
    sale1.removeItems('apples')

    print("\nRemoving an item that is not in the list:")
    sale1.removeItems('eggs')

    print("\nSale object after removing items:")
    print(sale1.getDescription())

    # Instance of Return
    return1 = Return(sale1)

    print("\nMessages from return object:")
    print(return1.returnItems('bananas', 'eggs', 'corn', 'apples'))

    print("\nDescription of return transaction:")
    print(return1.getDescription())

    print("\nValue of returned items' store credit:")
    print(return1.storeCredit())

    # Instance of Exchange
    exchange1 = Exchange(sale1)

    print("\nList of items brought to exchange:")
    print(exchange1.getSoldItems())
    exchange1.tradeItems(['apples', 'bananas'], ['grapes', 'carrots'])

    print("\nDescription of exchange transation after items were traded:")
    print(exchange1.getDescription())