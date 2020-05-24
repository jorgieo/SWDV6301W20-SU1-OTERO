# Point of sale (POS) module
# By Jorge Otero
# For SWDV630

from datetime import datetime
import secrets

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
        self.description['items'].remove(item)

    def getSoldItems(self):
        return self.sale_object.getDescription()['items']

class Return(Transaction):
    """
    Return transaction class.
    """
    def __init__(self, sale_object):
        super().__init__()
        self.setType("RETURN")
        self.sale_object = sale_object

    def returnItems(self, items=[]):
        for item in items:
            self.sale_object.removeItems(item)

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
                print("Item not found! Check the entry and try again.")

        self.newSale.addItems(new_items)

    def getNewSale(self):
        return self.newSale


if __name__ == '__main__':

    ITEM_DATABASE = {"bananas": 0.50,
                       "apples": 0.88,
                       "oranges": 0.90,
                       "milk": 3.10,
                       }

    sale1 = Sale()
    print(sale1.getDate())
    print(sale1.getID())
    sale1.addItems("bananas", "apples", "milk")
    print(sale1.getDescription())
    sale1.removeItems("apples")
    print(sale1.getDescription())

    refund1 = Return(sale1)
    print(refund1.getItems())