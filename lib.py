import sys

program = Program()

class Program:
    def __init__(self):
        self.saldo = 0
        self.magazyn = {}
        self.log = []

    @program.zmiana_salda(int(sys.argv[2]), str(sys.argv[3]))
    def zmiana_salda(self, kwota, komentarz):
        with open(sys.argv[1], "r") as plik:
            if self.saldo + kwota < 0:
                print("Za mało środków na koncie.")
                return False
            self.saldo += kwota
            self.log.append(["saldo", kwota, komentarz])
            return True

    def zakup(self, identyfikator, cena_jedn, ilosc_sztuk):
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
        if identyfikator not in self.magazyn:
            self.magazyn[identyfikator] = 0
        self.magazyn[identyfikator] += ilosc_sztuk

    def sprzedaz(self, identyfikator, cena_jedn, ilosc_sztuk):
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
        if identyfikator not in self.magazyn:
            print("Nie ma takiego produktu w magazynie!")
        if self.magazyn[identyfikator] - ilosc_sztuk < 0:
            print("Nie wystarczająca ilość {} na magazynie!".format(identyfikator))
        else:
            self.magazyn[identyfikator] -= ilosc_sztuk

    def przeglad(self):
        print("\nHistoria konta:")
        for wpis in self.log:
            for element in wpis:
                print(element)

    def konto(self):
        print("Konto: {}".format(self.saldo))

    def magazyn_log(self, identyfikator):
        if identyfikator in self.magazyn:
            self.stan_magazynu = self.magazyn[identyfikator]
        else:
            self.stan_magazynu = 0
        print("{}: {}".format(identyfikator, self.stan_magazynu))

    def zapis(self, plik):
        with open(sys.argv[1], "w") as plik:
            for wpis in self.log:
                for element in wpis:
                    plik.write(str(element) + "\n")
            plik.write("stop\n")

    def wczytanie(self, plik):
        with open(plik, "r") as plik:
            while True:
                akcja = plik.readline().rstrip()

                if not akcja:
                    break

                if akcja == "saldo":
                    kwota = int(plik.readline())
                    komentarz = str(plik.readline().rstrip())
                    self.zmiana_salda(kwota, komentarz)

                if akcja == "sprzedaz":
                    identyfikator = str(plik.readline().rstrip())
                    cena_jedn = int(plik.readline())
                    ilosc_sztuk = int(plik.readline())
                    self.sprzedaz(identyfikator, cena_jedn, ilosc_sztuk)

                if akcja == "zakup":
                    identyfikator = str(plik.readline().rstrip())
                    cena_jedn = int(plik.readline())
                    ilosc_sztuk = int(plik.readline())
                    self.zakup(identyfikator, cena_jedn, ilosc_sztuk)

                if akcja == "stop":
                    break
