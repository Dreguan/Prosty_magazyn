# python magazyn.py in.txt raspberry jason

import sys

from lib import Program

program = Program()

program.wczytanie(sys.argv[1])
program.magazyn_log(sys.argv[2:])
