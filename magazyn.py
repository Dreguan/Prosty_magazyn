# python magazyn.py raspberry jetson

import sys
from accountant import manager

manager.process()
manager.process_action("magazyn", sys.argv[1:])
