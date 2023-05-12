opiskelijatiedot = "opiskelijat1.csv"
tehtavatiedot = "tehtavat1.csv"
koepisteet = "koepisteet1.csv"
kurssin_tiedot = "kurssi1.txt"
"""
opiskelijatiedot = input("opiskelijat1.csv")
tehtavatiedot = input("tehtavat1.csv")
koepisteet = input("koepisteet1.csv")
kurssin_tiedot = input("kurssi1.txt")
"""

def arvosana(pisteet):
    if pisteet < 20:
        return 0
    elif pisteet < 25:
        return 1
    elif pisteet < 30:
        return 2
    elif pisteet < 35:
        return 3
    elif pisteet < 40:
        return 4
    else:
        return 5


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
        osat = rivi.strip().replace(" ","").split(":")
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
        tehtavalista[osat[0]] = osat[1:]
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
    i = [f"{i[0]}, {i[1]} opintopistetta\n"]
    tulostallennus.write(i[0])
    tulostallennus.write("="*(len(i[0])-1)+"\n")
    tulostallennus.write(f"nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana")
    for nro, nimi in opiskelijalista.items():






# for nro, nimi in opiskelijat.items():
#     arvosana = tehtavat[nro]//4 + koepisteet[nro]
#     yth_pist = arvosana
#     if arvosana <= 14:
#         arvosana = 0
#     elif arvosana in range(15,18):
#         arvosana = 1
#     elif arvosana in range(18, 21):
#         arvosana = 2
#     elif arvosana in range(21, 24):
#         arvosana = 3
#     elif arvosana in range(24,28):
#         arvosana = 4
#     elif arvosana >= 28:
#         arvosana = 5
#
#
#     print(f"{nimi:30}{tehtavat[nro]:<10}{tehtavat[nro]//4:<10}{koepisteet[nro]:<10}{yth_pist:<10}{arvosana}")