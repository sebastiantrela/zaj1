def f1():
    print("to jest pierwsza funkcja")

def f2(funkcja):
    print("to jest funkcja, która została wywołana w pierwszej funkcji")
    funkcja()

f2(f1)