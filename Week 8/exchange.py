from sqlalchemy import Column, Integer, String, Numeric
from transaction import Transaction
from transactionbase import Base


class Exchange(Transaction, Base):

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

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    transID = Column(String)
    description = Column(String)
