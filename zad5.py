def parzyste(lista):
    parzyste = []
    for liczba in lista:
        if liczba % 2 == 0:
            parzyste.append(liczba)
    return parzyste

pole = lambda a, b: a * b

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("liczby parzyste: ", parzyste(liczby))

a, b = 3, 15
print("pole prostokąta: ", pole(a, b))

