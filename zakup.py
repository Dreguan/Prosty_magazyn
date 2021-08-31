# python zakup.py raspberry 15000 4

import sys
from app import manager

manager.process()
manager.process_action("zakup", sys.argv[1:])
manager.save()
