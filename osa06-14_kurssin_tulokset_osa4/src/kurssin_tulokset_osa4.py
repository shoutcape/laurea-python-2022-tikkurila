opiskelijatiedot = "opiskelijat1.csv"
tehtavatiedot = "tehtavat1.csv"
koepisteet = "koepisteet1.csv"
kurssin_tiedot = "kurssi1.txt"
"""
opiskelijatiedot = input("opiskelijatiedot: ")
tehtavatiedot = input("tehtävätiedot: ")
koepisteet = input("koepisteet: ")
kurssin_tiedot = input("kurssin tiedot: ")
print("Tulokset talletettu tiedostoihin tulos.txt ja tulos.csv")
"""

def arvosana(pisteet):
    a = 0
    rajat = [15, 18, 21, 24, 28]
    while a < 5 and pisteet >= rajat[a]:
        a += 1
    return a


def tallenna_tulokset(tiedostonimi, viikkopisteet):
    with open(tiedostonimi, "w") as tiedosto:
        for nimi, lista in viikkopisteet.items():
            summa = sum(lista)
            tiedosto.write(f"{nimi};{summa};{arvosana(summa)}\n")


def hae_arvosana(haettava, viikkopisteet):
    for nimi, lista in viikkopisteet.items():
        if nimi == haettava:
            return arvosana(sum(lista))


with open(opiskelijatiedot) as opiskelijat, open(tehtavatiedot) as tehtavat, open(koepisteet) as koe_pst, open(
        kurssin_tiedot) as kurssit:
    kurssi = {}
    for rivi in kurssit:
        osat = rivi.strip().split(": ")
        kurssi[osat[0]] = osat[1]

    opiskelijalista = {}
    for rivi in opiskelijat:
        osat = rivi.strip().split(";")
        if osat[0] == "opnro":
            continue
        opiskelijalista[osat[0]] = f"{osat[1]} {osat[2]}"
    # lista opiskelijoista

    tehtavalista = {}
    for rivi in tehtavat:
        osat = rivi.strip().split(";")
        if osat[0] == "opnro":
            continue
        summa = 0
        for i in range(1, 8):
            summa += int(osat[i])
        tehtavalista[osat[0]] = summa
    # lista tehtävistä jotka tehty

    koepisteet = {}
    for rivi in koe_pst:
        osat = rivi.strip().split(";")
        if osat[0] == "opnro":
            continue
        yhteensa = 0
        for m in range(1, 4):
            yhteensa += int(osat[m])
        koepisteet[osat[0]] = yhteensa
    # yhteensälasketut koepisteet

# Luodaan tulos.txt tiedosto, johon tulostuu esteettinen lista eri tiedoista
with open("tulos.txt", "w") as tulostallennus:
    i = []
    for tieto, arvo in kurssi.items():
        i.append(arvo)
    i = [f"{i[0]}, {i[1]} opintopistettä\n"]
    tulostallennus.write(i[0])
    tulostallennus.write("=" * (len(i[0]) - 1) + "\n")
    tulostallennus.write(f"nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana\n")
    for opiskelijanro, nimi in opiskelijalista.items():
        pisteet = tehtavalista[opiskelijanro] // 4 + koepisteet[opiskelijanro]
        kurssiarvosana = (arvosana(pisteet))
        tulostallennus.write(f"{nimi:30}{tehtavalista[opiskelijanro]:<10}{tehtavalista[opiskelijanro]//4:<10}{koepisteet[opiskelijanro]:<10}{pisteet:<10}{kurssiarvosana}\n")

with open("tulos.csv", "w") as tulostilasto:
    for opiskelijanro, nimi in opiskelijalista.items():
        pisteet = tehtavalista[opiskelijanro] // 4 + koepisteet[opiskelijanro]
        kurssiarvosana = (arvosana(pisteet))
        tulostilasto.write(f"{opiskelijanro};{nimi};{kurssiarvosana}\n")