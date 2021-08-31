# python sprzedaz.py raspberry 25000 2

import sys
from accountant import manager

manager.process()
manager.process_action("sprzedaz", sys.argv[1:])
manager.save()

