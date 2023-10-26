
def tizedik():
    osszeg = 0
    darabszam = 0

    szam = int(input("Kérem adjon meg egy egész számot (0 a befejezéshez): "))
    while not szam == 0:
        szam = int(input("Kérem adjon meg egy egész számot (0 a befejezéshez): "))

        osszeg += szam
        darabszam += 1

    if darabszam > 0:
        atlag = osszeg / (darabszam -1)
        print(f"A megadott számok átlaga: {atlag}")
    else:
        print("Nem adott meg számot, nincs átlag számolva.")
tizedik()
