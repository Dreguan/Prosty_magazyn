saldo = 0
konto = []
magazyn = []

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
            print("Saldo nie może wynosić mniej niż 0! "
                  "Wprowadzone saldo -> kwota: {}, komentarz: {} "
                  "<- zostaje pominięte!".format(kwota, komentarz))
            continue
        else:
            konto.append([akcja, kwota, komentarz])
            print("Potwierdzam wprowadzenie salda -> kwota: {}, komentarz: {}."
                  .format(kwota, komentarz))
            print("Saldo wynosi teraz: {}".format(saldo))
    elif akcja == "zakup":
        print("Wprowadź identyfikator:")
        identifykator = str(input())
        print("Wprowadź cenę jednostkową w groszach:")
        cena_jedn = int(input())
        print("Wprowadź ilość sztuk:")
        ilosc_sztuk = int(input())
        zakup = cena_jedn * ilosc_sztuk
        print(zakup)
        saldo -= zakup
        print("Saldo wynosi teraz: {}".format(saldo))
        if saldo < 0:
            print("Saldo nie może wynosić mniej niż 0! "
                  "Wprowadzone saldo -> kwota: {}, komentarz: {} "
                  "<- zostaje pominięte!".format(kwota, komentarz))
            continue
        elif cena_jedn < 0:
            print("Cena jednostkowa nie może wynosić mniej niż 0! "
                  "Wprowadzone saldo -> kwota: {}, komentarz: {} "
                  "<- zostaje pominięte!".format(kwota, komentarz))
            continue
        elif ilosc_sztuk < 0:
            print("Ilość sztuk nie może wynosić mniej niż 0! "
                  "Wprowadzone saldo -> kwota: {}, komentarz: {} "
                  "<- zostaje pominięte!".format(kwota, komentarz))
            continue
        elif identifykator == "raspberry":
            if not magazyn:
                magazyn.append([identifykator, cena_jedn, ilosc_sztuk])
                print("Potwierdzam wprowadzenie zakupu -> identyfikator: {}, "
                      "cena jednostki: {}, sztuk: {}."
                      .format(identifykator, cena_jedn, ilosc_sztuk))
                print("...ILOŚĆ RASPBERRY TERAZ: {}".format(ilosc_sztuk))
            else:
                magazyn[0][2] += ilosc_sztuk
                print("Potwierdzam wprowadzenie zakupu -> identyfikator: {}, "
                      "cena jednostki: {}, sztuk: {}."
                      .format(identifykator, cena_jedn, ilosc_sztuk))
                print("ILOŚĆ RASPBERRY TERAZ: {}".format(magazyn[0][2]))
            print("Saldo wynosi teraz: {}".format(saldo))
    elif akcja == "sprzedaz":
        print("Wprowadź identyfikator:")
        identifykator = str(input())
        print("Wprowadź cenę jednostkową w groszach:")
        cena_jedn = int(input())
        print("Wprowadź ilość sztuk:")
        ilosc_sztuk = int(input())
        sprzedaz = cena_jedn * ilosc_sztuk
        print(sprzedaz)
        saldo += sprzedaz
        if saldo < 0:
            print("Saldo nie może wynosić mniej niż 0! "
                  "Wprowadzone saldo -> kwota: {}, komentarz: {} "
                  "<- zostaje pominięte!".format(kwota, komentarz))
            continue
        elif identifykator == "raspberry":
            magazyn[0][2] -= ilosc_sztuk
            print("ILOŚĆ RASPBERRY TERAZ: {}".format(magazyn[0][2]))
        else:
            magazyn.append([identifykator, cena_jedn, ilosc_sztuk])
            print("Potwierdzam wprowadzenie sprzedaży -> identyfikator: {},"
                  "cena jednostki: {}, sztuk: {}."
                  .format(identifykator, cena_jedn, ilosc_sztuk))
            print("Saldo wynosi teraz: {}".format(saldo))
    elif akcja == "stop":
        print("Koniec wprowadzania danych")
        break
    else:
        print("Wprowadzono nieprawidłową komendę!")
        break

print("\nHistoria konta:")
for element in konto:
    print(element)

print("\nStan magazynu:")
for element in magazyn:
    print(magazyn)
