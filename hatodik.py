def hatodik():
    szam = int(input("Kérlek adj meg egy számot: "))
    while not (szam % 3 == 0 or (szam ** 0.5)):
        print("A szám nem osztható 3al vagy négyzetszám.")
        szam = int(input("Kérlek adj meg egy számot: "))
    print("A szám osztható hárommal vagy négyzetszám.")


hatodik()