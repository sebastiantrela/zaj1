global globalna

def funkcja(lokalna):
    globalna = 5
    print(f"zmienna lokalna: {lokalna}")
    print(f"zmienna globalna przed zmianą: {globalna}")

    globalna = 15
    print(f"zmienna globalna po zmianie: {globalna}")

funkcja(50)