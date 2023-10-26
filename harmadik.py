def harmadik():
    szam = int(input("Kérlek adj meg egy számot: "))
    while szam % 10 != 0:
        szam = int(input("Kérlek adj meg egy számot: "))
        print("A megadott szám nem osztható 10-zel.")
    print("A szám osztható 10-zel.")

harmadik()