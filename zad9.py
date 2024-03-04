from functools import reduce

lista_liczb = [25, 65, 32, 64, 12, 56, 87, 20, 71, 44]
najwieksza_liczba = reduce(lambda x, y: x if x > y else y, lista_liczb)

print(f"największa liczba w liśćie to: {najwieksza_liczba}")

def srednia(lista_liczb):
    suma = reduce(lambda x, y: x + y, lista_liczb)
    srednia = suma / len(lista_liczb)
    return srednia

wynik = srednia(lista_liczb)
print(f"średnia z listy liczb: {wynik}")