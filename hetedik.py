#Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!

def hetedik():

    a = float(input("Kérem, adja meg az 'a' oldal hosszát: "))
    b = float(input("Kérem, adja meg a 'b' oldal hosszát: "))
    c = float(input("Kérem, adja meg a 'c' oldal hosszát: "))
    while not (a + b > c and a + c > b and b + c > a):
        print("A háromszög nem megszerkeszthető")
        a = float(input("Kérem, adja meg az 'a' oldal hosszát: "))
        b = float(input("Kérem, adja meg a 'b' oldal hosszát: "))
        c = float(input("Kérem, adja meg a 'c' oldal hosszát: "))

    print("Ezek az oldalhosszak alkothatnak egy háromszöget.")

hetedik()
