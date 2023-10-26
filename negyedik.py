def negyedik():
    szam = int(input("Kérlek adj meg egy számot: "))
    while not (szam % 2 == 0 and szam >= 10 and szam < 100):

        print("A szám nem kétjegyű vagy nem páros.")
        szam = int(input("Kérlek adj meg egy számot: "))
    print("A szám kétjegyű és páros.")

negyedik()