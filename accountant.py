import sys

saldo = 0
log = []
magazyn = {}

while True:
    akcja = input()
    if not akcja:
        break
    if akcja == "saldo":
        kwota = int(input())
        saldo += kwota
        komentarz = str(input())
        if saldo < 0:
            print(
                "Saldo nie może wynosić mniej niż 0! "
                "Wprowadzone saldo -> kwota: {}, komentarz: {} "
                "<- zostaje pominięte!".format(kwota, komentarz)
            )
            continue
        else:
            log.append([akcja, kwota, komentarz])
            print(
                "Potwierdzam wprowadzenie salda -> kwota: {}, komentarz: {}."
                .format(kwota, komentarz)
            )
        continue
    if akcja == "zakup":
        identifykator = str(input())
        cena_jedn = int(input())
        ilosc_sztuk = int(input())
        zakup = cena_jedn * ilosc_sztuk
        saldo -= zakup
        if saldo < 0:
            print(
                "Saldo nie może wynosić mniej niż 0! "
                "Wprowadzone saldo -> kwota: {}, komentarz: {} "
                "<- zostaje pominięte!".format(kwota, komentarz)
            )
            continue
        elif cena_jedn < 0 or ilosc_sztuk < 0:
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
            print(
                "Potwierdzam wprowadzenie zakupu -> identyfikator: {}, "
                "cena jednostki: {}, sztuk: {}."
                    .format(identifykator, cena_jedn, ilosc_sztuk)
            )
            if identifykator not in magazyn:
                magazyn[identifykator] = 0
            magazyn[identifykator] += ilosc_sztuk
        continue
    if akcja == "sprzedaz":
        identifykator = str(input())
        cena_jedn = int(input())
        ilosc_sztuk = int(input())
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
            print(
                "Potwierdzam wprowadzenie sprzedaży -> identyfikator: {}, "
                "cena jednostki: {}, sztuk: {}."
                    .format(identifykator, cena_jedn, ilosc_sztuk)
            )
            magazyn[identifykator] -= ilosc_sztuk
        continue

    elif sys.argv[1] == "magazyn":
        for identifykator in sys.argv[2:]:
            if identifykator in magazyn:
                stan_magazynu = magazyn[identifykator]
            else:
                stan_magazynu = 0
            print("{}: {}".format(identifykator, ilosc_sztuk))
        break

    if sys.argv[2] == "przeglad":
        print("\nHistoria konta:")
        for wpis in konto:
            for element in wpis:
                print(element)
        break

    elif akcja == "konto":
        print(saldo)
        break

    if akcja == "stop":
        print("Koniec wprowadzania danych")
        break

    else:
        print("Wprowadzono nieprawidłową komendę!")
        break

# print("\n {}".format(saldo))
# print("\n {}".format(log))
# print("\n {}".format(magazyn))
