# python saldo.py in.txt 5000 "wplata wlasna"

import sys

from lib import Program

program = Program()

program.wczytanie(sys.argv[1])
program.zmiana_salda(int(sys.argv[2]), str(sys.argv[3]))
print(program.saldo)
program.zapis(str(sys.argv[1]))
