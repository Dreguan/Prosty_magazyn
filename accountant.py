saldo = 0
konto = []
magazyn = {}

while True:
    print("Wprowadź komendę:")
    akcja = input()
    if not akcja:
        break
    if akcja == "saldo":
        print("Wprowadź kwotę w groszach:")
        kwota = int(input())
        saldo += kwota
        print("Wprowadź komentarz:")
        komentarz = str(input())
        if saldo < 0:
            print(
                "Saldo nie może wynosić mniej niż 0! "
                "Wprowadzone saldo -> kwota: {}, komentarz: {} "
                "<- zostaje pominięte!".format(kwota, komentarz)
            )
            continue
        else:
            konto.append([akcja, kwota, komentarz])
            print(
                "Potwierdzam wprowadzenie salda -> kwota: {}, komentarz: {}."
                .format(kwota, komentarz)
            )
            print("Saldo wynosi teraz: {}".format(saldo))
    elif akcja == "zakup":
        print("Wprowadź identyfikator:")
        identifykator = str(input())
        print("Wprowadź cenę jednostkową w groszach:")
        cena_jedn = int(input())
        print("Wprowadź ilość sztuk:")
        ilosc_sztuk = int(input())
        zakup = cena_jedn * ilosc_sztuk
        #print(zakup)
        saldo -= zakup
        print("Saldo wynosi teraz: {}".format(saldo))
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
            konto.append([akcja, identifykator, cena_jedn, ilosc_sztuk])
            print(
                "Potwierdzam wprowadzenie zakupu -> identyfikator: {}, "
                "cena jednostki: {}, sztuk: {}."
                    .format(identifykator, cena_jedn, ilosc_sztuk)
            )
            if identifykator not in magazyn:
                magazyn[identifykator] = 0
            magazyn[identifykator] += ilosc_sztuk
    elif akcja == "sprzedaz":
        print("Wprowadź identyfikator:")
        identifykator = str(input())
        print("Wprowadź cenę jednostkową w groszach:")
        cena_jedn = int(input())
        print("Wprowadź ilość sztuk:")
        ilosc_sztuk = int(input())
        sprzedaz = cena_jedn * ilosc_sztuk
        #print(sprzedaz)
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
            konto.append([akcja, identifykator, cena_jedn, ilosc_sztuk])
            if identifykator not in magazyn:
                print("Nie ma takiego produktu w magazynie!")
            print(
                "Potwierdzam wprowadzenie sprzedaży -> identyfikator: {}, "
                "cena jednostki: {}, sztuk: {}."
                    .format(identifykator, cena_jedn, ilosc_sztuk)
            )
            magazyn[identifykator] -= ilosc_sztuk
    elif akcja == "stop":
        print("Koniec wprowadzania danych")
        break
    else:
        print("Wprowadzono nieprawidłową komendę!")
        break
'''
    elif akcja == "przeglad":
        print("\nHistoria konta:")
        for wpis in konto:
            for element in wpis:
                print(element)
        break
    elif akcja == "konto":
        print(saldo)
        break
'''

print("\n {}".format(saldo))
print("\n {}".format(konto))
print("\n {}".format(magazyn))
