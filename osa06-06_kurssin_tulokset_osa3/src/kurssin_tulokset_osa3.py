"""
opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koetiedot = input("Koepisteet: ")
"""
opiskelijatiedot = "opiskelijat1.csv"
tehtavatiedot = "tehtavat1.csv"
koetiedot = "koepisteet1.csv"


opiskelijat = {}
with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.strip().split(";")
        if osat[0] == "opnro":
            continue
        opiskelijat[osat[0]] = f"{osat[1]} {osat[2]}"


tehtavat = {}
with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.strip().split(";")
        summa = 0
        if osat[0] == "opnro":
            continue
        for i in range(1, 8):
            summa += int(osat[i])
        tehtavat[osat[0]] = summa


koepisteet = {}
with open(koetiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.strip().split(";")
        if osat[0] == "opnro":
            continue
        yhteensa = 0
        for m in range(1, 4):
            yhteensa += int(osat[m])
        koepisteet[osat[0]] = yhteensa

otsikko = ["nimi", "teht_lkm", "teht_pist", "koe_pist", "yht_pist", "arvosana"]
for osa in otsikko:
    if osa == "nimi":
        print(f"{osa:30}", end="")
        continue
    print(f"{osa:10}", end="")
    if osa == "arvosana":
        print()

for nro, nimi in opiskelijat.items():
    arvosana = tehtavat[nro]//4 + koepisteet[nro]
    yth_pist = arvosana
    if arvosana <= 14:
        arvosana = 0
    elif arvosana in range(15,18):
        arvosana = 1
    elif arvosana in range(18, 21):
        arvosana = 2
    elif arvosana in range(21, 24):
        arvosana = 3
    elif arvosana in range(24,28):
        arvosana = 4
    elif arvosana >= 28:
        arvosana = 5


    print(f"{nimi:30}{tehtavat[nro]:<10}{tehtavat[nro]//4:<10}{koepisteet[nro]:<10}{yth_pist:<10}{arvosana}")