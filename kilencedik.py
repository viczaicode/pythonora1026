def kilencedik():
    szoveg = input("Kérem adjon meg egy szót vagy mondatot (4 karakter hosszú): ")
    nagybetus_szoveg = szoveg.upper()
    while not len(szoveg) == 4 and nagybetus_szoveg:
        nagybetus_szoveg = szoveg.upper()
        szoveg = input("Kérem adjon meg egy szót vagy mondatot (4 karakter hosszú): ")
        print("A megadott szó vagy mondat túl rövid, vagy túl hosszú. Kérem, adjon meg 4 karakter hosszú szót vagy mondatot ")

    print("KÉSZ")
kilencedik()