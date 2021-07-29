# python konto.py in.txt

import sys

from lib import Program

program = Program()

print(sys.argv[1])

program.wczytanie(sys.argv[1])
program.konto()