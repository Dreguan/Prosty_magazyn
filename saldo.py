# python saldo.py 5000 "wplata wlasna"

import sys
from app import manager

manager.process()
manager.process_action("saldo", sys.argv[1:])
print(manager.account)
manager.save()
