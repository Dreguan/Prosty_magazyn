# python magazyn.py in.txt raspberry jetson

import sys

from lib import Program

program = Program()

program.wczytanie(sys.argv[1])
for identyfikator in sys.argv[2:]:
    program.magazyn_log(identyfikator)
