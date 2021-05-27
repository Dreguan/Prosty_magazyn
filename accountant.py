
dane = []

while True:
    akcja = input()
    if not akcja:
        break
    if akcja == "saldo":
        kwota = input()
        komentarz = input()
        dane.append([akcja, kwota, komentarz])
        print("Potwierdzam wprowadzenie salda -> kwota: {}, komentarz: {}.".format(kwota, komentarz))
        #print(dane)
    elif akcja == "zakup":
        identifykator = input()
        cena_jedn = input()
        ilosc_sztuk = input()
        dane.append([identifykator, cena_jedn, ilosc_sztuk])
        print("Potwierdzam wprowadzenie zakupu -> identyfikator: {}, cena jednostki: {}, sztuk: {}.".format(identifykator, cena_jedn, ilosc_sztuk))
        #print(dane)
    elif akcja == "sprzedaz":
        identifykator = input()
        cena_jedn = input()
        ilosc_sztuk = input()
        dane.append([identifykator, cena_jedn, ilosc_sztuk])
        print("Potwierdzam wprowadzenie sprzedaży -> identyfikator: {}, cena jednostki: {}, sztuk: {}.".format(identifykator, cena_jedn, ilosc_sztuk))
    elif akcja == "stop":
        print("Koniec wprowadzania danych")
        break
    else:
        print("Wprowadzono nieprawidłową komendę!")
        break

