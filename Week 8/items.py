from sqlalchemy import Column, Integer, String, Numeric
from inventorybase import Base
import secrets


class Item(Base):
    """Items in the inventory."""

    def __init__(self, name, price, in_stock_qty):
        self.name = name
        self.code = self._genCode()
        self.price = price
        self.in_stock_qty = in_stock_qty

    def __repr__(self):
        return f"Item Name: {self.name}\nItem Code: {self.code}\nItem Price: {self.price}\nItem Stock: {self.in_stock_qty}"

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def _genCode(self):
        return secrets.token_hex(12)

    def getCode(self):
        return self.code

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    price = Column(Numeric)
    in_stock_qty = Column(Numeric)
