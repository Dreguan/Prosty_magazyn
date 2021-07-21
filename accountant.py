import sys
from lib import *

saldo = 0
log = []
magazyn = {}
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
            identyfikator = str(plik.readline())
            cena_jedn = int(plik.readline())
            ilosc_sztuk = int(plik.readline())
            program.sprzedaz(identyfikator, cena_jedn, ilosc_sztuk)

        if akcja == "zakup":
            identyfikator = str(plik.readline())
            cena_jedn = int(plik.readline())
            ilosc_sztuk = int(plik.readline())
            program.zakup(identyfikator, cena_jedn, ilosc_sztuk)

'''
    if sys.argv[1] == "sprzedaz":
        akcja = sys.argv[1]
        identifykator = str(sys.argv[2])
        cena_jedn = int(sys.argv[3])
        ilosc_sztuk = int(sys.argv[4])
        sprzedaz = cena_jedn * ilosc_sztuk
        saldo += sprzedaz
        if cena_jedn < 0 or ilosc_sztuk < 0:
            if cena_jedn < 0:
                bledne_pole = "cena jednostkowa"
            elif ilosc_sztuk < 0:
                bledne_pole = "ilość sztuk"
            print(
                "{} nie może wynosić mniej niż 0! "
                "Wprowadzone saldo -> kwota: {}, komentarz: {} "
                "<- zostaje pominięte!".format(bledne_pole, kwota, komentarz)
            )
            continue
        else:
            log.append([akcja, identifykator, cena_jedn, ilosc_sztuk])
            if identifykator not in magazyn:
                print("Nie ma takiego produktu w magazynie!")
            magazyn[identifykator] -= ilosc_sztuk
        for wpis in log:
            for element in wpis:
                print(element)
        continue

    if sys.argv[1] == "magazyn":
        for identifykator in sys.argv[2:]:
            if identifykator in magazyn:
                stan_magazynu = magazyn[identifykator]
            else:
                stan_magazynu = 0
            print("{}: {}".format(identifykator, stan_magazynu))
        break

    if sys.argv[1] == "przeglad":
        print("\nHistoria konta:")
        for wpis in log:
            for element in wpis:
                print(element)
        break

    if sys.argv[1] == "konto":
        print(saldo)
        break

    if akcja == "stop":
        for wpis in log:
            for element in wpis:
                print(element)

    else:
        print("Wprowadzono nieprawidłową komendę!")
'''