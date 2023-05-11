import math

def hae_asematiedot(tiedosto: str):
    sanakirja = {}
    with open(tiedosto) as tiedosto:
        for rivi in tiedosto:
            sarakkeet = rivi.split(";")
            if sarakkeet[0] == "Longitude":
                continue
            sanakirja[sarakkeet[3]] = (float(sarakkeet[0]), float(sarakkeet[1]))
    return sanakirja
def etaisyys(asemat: dict, asema1: str, asema2: str):

    for nimi, koordinaatit in asemat.items():
        if nimi == asema1:
            longitude1 = float(koordinaatit[0])
            latitude1 = float(koordinaatit[1])
        if nimi == asema2:
            longitude2 = float(koordinaatit[0])
            latitude2 = float(koordinaatit[1])

    x_kilometreina = (longitude1 - longitude2) * 55.26
    y_kilometreina = (latitude1 - latitude2) * 111.2
    etaisyys = math.sqrt(x_kilometreina ** 2 + y_kilometreina ** 2)

    return float(etaisyys)

def suurin_etaisyys(asemat: dict):
    suurin = 0
    for nimi1 in asemat:
        for nimi2 in asemat:
            if nimi1 != nimi2:
                matka = etaisyys(asemat, nimi1, nimi2)
                if matka > suurin:
                    suurin = matka
                    palautus = nimi1, nimi2, float(suurin)

    return palautus

if __name__ == "__main__":
    asemat = hae_asematiedot('stations1.csv')
    e = etaisyys(asemat, "Designmuseo", "Hietalahdentori")
    print(e)
    e = etaisyys(asemat, "Viiskulma", "Kaivopuisto")
    print(e)
    asema1, asema2, suurin = suurin_etaisyys(asemat)
    print(asema1, asema2, suurin)
