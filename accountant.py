from manager import Reader, Manager, NotEnoughDataException

reader = Reader("in.txt")
manager = Manager(reader)

@manager.action("saldo", 2)
def saldo(manager, rows):
    price = float(rows[0])
    manager.modify_account(price)
    return True

@manager.action("zakup", 3)
def zakup(manager, rows):
    name = rows[0]
    price = float(rows[1])
    qty = float(rows[2])
    manager.modify_account(-price*qty)
    manager.modify_stock(name, qty)
    return True

@manager.action("sprzedaz", 3)
def sprzedaz(manager, rows):
    name = rows[0]
    price = float(rows[1])
    qty = float(rows[2])
    manager.modify_account(price*qty)
    manager.modify_stock(name, -qty)
    return True

@manager.action("magazyn", 2)
def magazyn(manager, rows):
    for item in rows:
        if item not in manager.stock:
            manager.stock[item] = 0
        print(manager.stock)

@manager.action("przeglad", 2)
def przeglad(manager, rows):
    for row in manager.review(rows[0], rows[1]):
        print("\n".join(row))

try:
    manager.process()
except NotEnoughDataException as exc:
    print(exc)