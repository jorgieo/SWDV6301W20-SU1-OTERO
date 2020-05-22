# Point of sale (POS) module
# By Jorge Otero

from datetime import datetime
import secrets

class Transaction:
    """
    Super class for all transaction types.
    """
    def __init__(self):
        self.timestamp = ''
        self.transID = self._generate_ID()
        self.status = ''

    def _generate_ID(self):
        return secrets.token_hex(16)

    def timetag(self):
        return datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    def commit_to_ledger(self):
        pass

    def cancel(self):
        self.status = 'CANCELLED'

    def complete(self):
        self.status = 'COMPLETE'

    def getDate(self):
        pass

    def getID(self):
        pass

class Sale(Transaction):
    pass

class Return(Transaction):
    pass

class Pricecheck(Transaction):
    pass

if __name__ == '__main__':
    sale = Sale()
    print(sale.timetag())