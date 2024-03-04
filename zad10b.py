def czytaj_plik(nazwa):
    with open(nazwa, 'r') as plik:
        for linia in plik:
            yield linia.rstrip('\n')

nazwa_pliku = "plik.txt"
generator = czytaj_plik(nazwa_pliku)

for linia in generator:
    print(linia)