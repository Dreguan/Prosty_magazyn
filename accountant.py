import sys
from lib import *

program = Program()

with open ("in.txt") as plik:

    while True:
        akcja = plik.readline().rstrip()

        if not akcja:
            break

        if akcja == "saldo":
            kwota = int(plik.readline())
            komentarz = str(plik.readline())
            program.zmiana_salda(kwota, komentarz)

        if akcja == "sprzedaz":
            identyfikator = str(plik.readline().rstrip())
            cena_jedn = int(plik.readline())
            ilosc_sztuk = int(plik.readline())
            program.sprzedaz(identyfikator, cena_jedn, ilosc_sztuk)

        if akcja == "zakup":
            identyfikator = str(plik.readline().rstrip())
            cena_jedn = int(plik.readline())
            ilosc_sztuk = int(plik.readline())
            program.zakup(identyfikator, cena_jedn, ilosc_sztuk)

        if akcja == "stop":
            break

if sys.argv[1] == "sprzedaz":
    identyfikator = str(sys.argv[2])
    cena_jedn = int(sys.argv[3])
    ilosc_sztuk = int(sys.argv[4])
    program.sprzedaz(identyfikator, cena_jedn, ilosc_sztuk)

if sys.argv[1] == "zakup":
    identyfikator = str(sys.argv[2])
    cena_jedn = int(sys.argv[3])
    ilosc_sztuk = int(sys.argv[4])
    program.zakup(identyfikator, cena_jedn, ilosc_sztuk)

if sys.argv[1] == "magazyn":
    for identyfikator in sys.argv[2:]:
        program.magazyn_log(identyfikator)

if sys.argv[1] == "przeglad":
    program.przeglad()

if sys.argv[1] == "konto":
    program.konto()

