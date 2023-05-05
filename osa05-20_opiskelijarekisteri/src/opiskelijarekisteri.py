def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    opiskelijat[nimi] = []

def tulosta(opiskelijat: dict, nimi: str):
    if nimi in opiskelijat:
        print(f"{nimi}:")

    if nimi not in opiskelijat:
        print(f"ei löytynyt ketään nimellä {nimi}")

    elif opiskelijat[nimi] == []:
         print(" ei suorituksia")

    else:

        suoritukset = "\n".join([f"  {suoritus[0]} {suoritus[1]}" for suoritus in opiskelijat[nimi]])
        print(f" suorituksia {len(opiskelijat[nimi])} kurssilta:")
        print(suoritukset)


# Keskiarvon lasku
        kokonaispisteet = 0
        for suoritus in opiskelijat[nimi]:
            kokonaispisteet = kokonaispisteet + suoritus[-1]

        print(" keskiarvo", kokonaispisteet/len(opiskelijat[nimi]))

def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):
    arvosana = suoritus[1]
    if arvosana > 0:
        vanha_suoritus = None
        for i, kurssi in enumerate(opiskelijat[nimi]):
            if kurssi[0] == suoritus[0]:
                vanha_suoritus = i
                break

        # Jos samannimistä kurssia ei ole vielä suoritettu, lisää suoritus listaan
        if vanha_suoritus is None:
            opiskelijat[nimi].append(suoritus)
        # Jos uusi suoritus on parempi, korvaa vanha suoritus uudella
        elif arvosana > opiskelijat[nimi][vanha_suoritus][1]:
            opiskelijat[nimi][vanha_suoritus] = suoritus

def kooste(opiskelijat: dict):
    paraskeskiarvo = 0
    print(f"opiskelijoita {len(opiskelijat)}")
    print(f"eniten suorituksia {len(opiskelijat[max(opiskelijat)])} {max(opiskelijat)}")

    eniten_suorituksia = 0
    eniten_suorituksia_opiskelija = None
    for nimi, suoritukset in opiskelijat.items():
        kokonaispisteet = sum(suoritu[1] for suoritu in suoritukset)
        if suoritukset: #löytyykö suorituksia?
            keskiarvo = kokonaispisteet / len(suoritukset)
            if keskiarvo > paraskeskiarvo:
                paraskeskiarvo = keskiarvo
                parasopiskelija = nimi


    print(f"paras keskiarvo {paraskeskiarvo:.1f} {parasopiskelija}")


def main():

    # Lisaa opiskelijat tiedot
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 0))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 2))
    tulosta(opiskelijat, "Pekka")
    tulosta(opiskelijat, "Liisa")
    tulosta(opiskelijat, "Jukka")
    kooste(opiskelijat)


if __name__ == "__main__":
    main()