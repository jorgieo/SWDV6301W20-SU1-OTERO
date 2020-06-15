from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Item(Base):
    """Items in the inventory."""

    def __init__(self, name, code, price, in_stock_qty):
        self.name = name
        self.code = code
        self.price = price
        self.in_stock_qty = in_stock_qty

    def __repr__(self):
        return f"Item Name: {self.name}\nItem Code: {self.code}\nItem Price: {self.price}\nItem Stock: {self.in_stock_qty}"

    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    price = Column(Numeric)
    in_stock_qty = Column(Numeric)


def main():

    engine =  create_engine("sqlite:///test_db.db", echo=False)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()  # Returns and Session class and creates a Session object in one line.

    items = [Item("apple", "F002", 0.95, 50),
            Item("orange", "F003", 0.95, 35),
            Item("strawberry", "F004", 2.50, 20),
            Item("watermelon", "F005", 4.25, 15),
            Item("lime", "F006", 0.75, 70)
            ]

    for item in items:
        session.add(item)

    itemsQuery = session.query(Item).all()
    
    for item in itemsQuery:
        print(item)

    session.commit()
    session.close()

if __name__ == '__main__': main()