lista = ["jabłko", "ananas", "pomarańcza", "arbuz", "nektarynka", "awokado"]
slowa = list(filter(lambda slowo: slowo.startswith('a'), lista))

print(f"słowa zaczynające się na 'a': {slowa}")

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kwadraty = list(map(lambda x: x**2, liczby))

print(f"lista liczb: {liczby}")
print(f"lista kwadratów: {kwadraty}")