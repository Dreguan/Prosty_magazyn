
dane = []


while True:
    akcja = input()
    if not akcja:
        break
    if akcja == "saldo":
        kwota = input()
        komentarz = input()
        dane.append([akcja, kwota, komentarz])
        print("Potwierdzam wprowadzenie: {} {}.".format(kwota, komentarz))
        print(dane)
    else:
        print("Wprowadzono nieprawidłową komendę!")
        break