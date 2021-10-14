def atlag(list):
    darab = len(list)
    osszeg = 0
    for szam in list:
        osszeg += szam
    ave = osszeg / darab
    return ave

szamok = [100,40,75,40,4,18,23,4,55]
atlag = atlag(szamok)
print(f"A szamok atlaga: {atlag}")