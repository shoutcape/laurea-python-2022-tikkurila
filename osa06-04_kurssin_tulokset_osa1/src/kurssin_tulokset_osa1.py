
"""

opiskelijatiedot = input("opiskelijatiedot: ")
tehtavatiedot = input("tehtävätiedot: ")

"""

opiskelijatiedot = "opiskelijat1.csv"
tehtavatiedot = "tehtavat1.csv"

opiskelijat = {}
with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        opiskelijat[osat[0]] = f"{osat[1]} {osat[2].strip()}"

tehtavat = {}
with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        summa = 0
        for i in range(1, 8):
            summa += int(osat[i])
        tehtavat[osat[0]] = summa

for oppilasnumero, nimi in opiskelijat.items():
    print(f"{nimi} {tehtavat[oppilasnumero]}")




"""
def main():
    opiskelijat = input("Opiskelijatiedot: ")
    tehtavat = input("Tehtävätiedot: ")

    with open(opiskelijat) as tiedosto:
        nimet = {}
        for rivi in tiedosto:
            uusirivi = rivi.strip().split(";")
            if uusirivi[0] == "opnro":
                continue
            nimet[uusirivi[0]] = f"{uusirivi[1]} {uusirivi[2]}"
# Nimet = sanakirja nimistä

    with open(tehtavat) as tiedosto:
        tehtavat = {}
        for rivi in tiedosto:
            uusirivi = rivi.strip().split(";")
            if uusirivi[0] == "opnro":
                continue
            tehtavat[uusirivi[0]] = (uusirivi[1:])

    for oppilasnro, tehtavat in tehtavat.items():
        if oppilasnro in nimet:
            yhteensa = 0
            nimi = nimet[oppilasnro]
            for kohta in tehtavat:
                yhteensa += int(kohta)
            print(nimi, yhteensa)

main()"""