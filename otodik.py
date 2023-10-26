def otodik():
    szam = int(input("Kérlek adj meg egy számot: "))
    while not (szam % 2 == 0 and szam > 0):
        print("A szám nem pozitív vagy nem páros.")
        szam = int(input("Kérlek adj meg egy számot: "))
    print("A szám pozitív és páros.")

otodik()