from employee import Employee
from items import Item
from sale import Sale
from base import Base, engine, Session

Base.metadata.create_all(engine)

def init_config():
    """Create a supervisor and add stuff to the inventory"""

    supervisor = Employee('John Smith', 'Supervisor')
    session = Session()
    session.add(supervisor)
    print(session.query(Employee).first())

    item_list = [Item('T-Shirt', 25.00, 13),
                 Item('Shorts', 34.50, 20),
                 Item('Jeans', 40.00, 16)]

    for item in item_list:
        session.add(item)

    queried_items = session.query(Item).all()
    for item in queried_items:
        print(item)

    session.commit()
    session.close()


def execute_sale():
    """scan an item and sell it"""
    sale = Sale()

    session = Session()

    scanned_items = session.query(Item).all()
    for item in scanned_items:
        sale.addItems(item)

    print(sale.getSoldItems())
    print(f"\nTransaction Total: {sale.netTotal}\n")

    session.add(sale)
    session.commit()
    session.close()

def search_inventory():
    """take items from the a sale and return them"""
    session = Session()
    inventory = session.query(Item).all()
    for item in inventory:
        print(item)
        print()

# Tests:

# init_config()

# execute_sale()

search_inventory()