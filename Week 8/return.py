from sqlalchemy import Column, Integer, String, Numeric
from transaction import Transaction
from base import Base


class Return(Transaction, Base):
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

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    transID = Column(String)
    description = Column(String)
