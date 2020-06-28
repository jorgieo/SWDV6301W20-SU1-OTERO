from sqlalchemy import Column, Integer, String, Numeric
from transaction import Transaction
from base import Base


class Sale(Transaction, Base):
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

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    transID = Column(String)
    description = Column(String)
