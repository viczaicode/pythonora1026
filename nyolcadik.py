def nyolcadik():
    szoveg = input("Kérem adjon meg egy szót vagy mondatot (legalább 3 karakter hosszú): ")
    while not len(szoveg) >= 3:
        nagybetus_szoveg = szoveg.upper()
        szoveg = input("Kérem adjon meg egy szót vagy mondatot (legalább 3 karakter hosszú): ")
        print("A megadott szó vagy mondat túl rövid. Kérem, adjon meg legalább 3 karakter hosszú szót vagy mondatot ")

    nagybetus_szoveg = szoveg.upper()
    print("A nagybetűs verzió:" + nagybetus_szoveg)
nyolcadik()