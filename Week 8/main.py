from employee import Employee
from items import Item
from sale import Sale
from base import Base, engine, Session

Base.metadata.create_all(engine)

def init_config():
    """Create a supervisor and add stuff to the inventory."""

    supervisor = Employee('John Smith', 'Supervisor')
    session = Session()
    session.add(supervisor)
    print(session.query(Employee).first())

    item_list = [Item('T-Shirt', 25.00, 13),
                 Item('Shorts', 34.50, 20),
                 Item('Jeans', 40.00, 16)]

    for item in item_list:
        session.add(item)

    print("Items added to inventory:")
    queried_items = session.query(Item).all()
    for item in queried_items:
        print(item)

    session.commit()
    session.close()


def execute_sale():
    """Scan an item (from inventory) and sell it."""
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
    """Use a keyword to search for an inventory item."""
    session = Session()
    inventory = session.query(Item).all()

    # print("Inventory:")
    # for item in inventory:
    #     print(item)
    #     print()

    search_query = session.query(Item).first().name
    search_result = session.query(Item).filter(Item.name == search_query).all()
    print(f"Search for '{search_query} resulted in:")
    print(search_result)
    print()

def balance_register():
    session = Session()
    sales = session.query(Sale).all()
    num_sales = session.query(Sale).count()

    grand_total = 0
    for sale in sales:
        grand_total += sale.netTotal

    print(f"Number of Sales: {num_sales}\nSales Total = ${grand_total:.2f}")


# Functionality Tests:

init_config()

execute_sale()

search_inventory()

balance_register()
