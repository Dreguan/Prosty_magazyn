# python zakup.py in.txt raspberry 15000 4

import sys

from lib import Program

program = Program()

program.wczytanie(sys.argv[1])
program.zakup(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
program.zapis(sys.argv[1])
