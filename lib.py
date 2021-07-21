

class Program:
    def __init__(self):
        self.saldo = 0
        self.magazyn = {}
        self.log = []

    def zmiana_salda(self, kwota, komentarz):
        with open("in.txt") as plik:
            if self.saldo + kwota < 0:
                print("Za mało środków na koncie.")
                return False
            self.saldo += kwota
            self.log.append(["saldo", kwota, komentarz])
            print(self.saldo)
            return True

    def zakup(self, identyfikator, cena_jedn, ilosc_sztuk):
        with open("in.txt") as plik:
            zakup = cena_jedn * ilosc_sztuk
            self.saldo -= zakup
            if self.saldo < 0:
                print("Saldo nie może wynosić mniej niż 0!")
                return False
            if cena_jedn < 0 or ilosc_sztuk < 0:
                if cena_jedn < 0:
                    bledne_pole = "Cena jednostkowa"
                elif ilosc_sztuk < 0:
                    bledne_pole = "Ilość sztuk"
                print(
                    "{} nie może wynosić mniej niż 0! "
                    "Wprowadzone saldo -> kwota: {}, komentarz: {} "
                    "<- zostaje pominięte!".format(bledne_pole, zakup, identyfikator)
                )
                return False
            self.log.append(["zakup", identyfikator, cena_jedn, ilosc_sztuk])
            print(self.saldo)

            '''
            if identyfikator not in self.magazyn:
                self.magazyn[identyfikator] = 0
                return True
            self.magazyn[identyfikator] += ilosc_sztuk
            for wpis in self.log:
                for element in wpis:
                    print(element)
                return True
            '''

    def sprzedaz(self, identyfikator, cena_jedn, ilosc_sztuk):
        with open("in.txt") as plik:
            sprzedaz = cena_jedn * ilosc_sztuk
            self.saldo += sprzedaz
            if cena_jedn < 0 or ilosc_sztuk < 0:
                if cena_jedn < 0:
                    bledne_pole = "Cena jednostkowa"
                elif ilosc_sztuk < 0:
                    bledne_pole = "Ilość sztuk"
                print(
                    "{} nie może wynosić mniej niż 0! "
                    "Wprowadzone saldo -> kwota: {}, komentarz: {} "
                    "<- zostaje pominięte!".format(bledne_pole, sprzedaz, identyfikator)
                )
                return False
            self.log.append(["sprzedaz", identyfikator, cena_jedn, ilosc_sztuk])
            print(self.saldo)


            '''
            if identyfikator not in magazyn:
                print("Nie ma takiego produktu w magazynie!")
            magazyn[identifykator] -= ilosc_sztuk
        for wpis in log:
            for element in wpis:
                print(element)
        continue
            '''
