# python konto.py in.txt

import sys

from lib import Program

program = Program()
program.wczytanie(sys.argv[1])
program.konto()