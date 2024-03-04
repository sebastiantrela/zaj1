def kwadrat(x):
    return x**2

def dodaj(x):
    return x + 5

def skladanie(f1, f2):
    return lambda x: f1(f2(x))

liczby = [1, 2, 3, 4, 5]

wynik = list(map(skladanie(kwadrat, dodaj), liczby))
print(f"wynik: {wynik}")



def aplikuj(lista_funkcji, wartosc):
    wynik = wartosc
    for funkcja in lista_funkcji:
        wynik = funkcja(wynik)
    return wynik

def mnozenie(x):
    return x * 3

def dodawanie(x):
    return x + 2

def odejmowanie(x):
    return x - 1

lista_funkcji = [mnozenie, dodawanie, odejmowanie]
wartosc = 10
wynik = aplikuj(lista_funkcji, wartosc)
print(f"wynik: {wynik}")