def hae_nimi(tiedosto: str, hakusana: str):
    palautus = []
    with open(tiedosto) as tiedosto:
        reseptilista = tiedosto.read()


    reseptit = reseptilista.split("\n\n")
    for resepti in reseptit:
        rivit = resepti.split("\n")
        nimi = rivit[0]
        if hakusana in nimi.lower():
            palautus.append(nimi)

    return palautus

def hae_aika(tiedosto: str, aika: int):
    palautus = []
    with open(tiedosto) as tiedosto:
        reseptilista = tiedosto.read()

        reseptit = reseptilista.split("\n\n")
        for resepti in reseptit:
            rivit = resepti.split("\n")
            nimi = rivit[0]
            valmistusaika = int(rivit[1])
            if aika >= valmistusaika:
                palautus.append(f"{nimi}, valmistusaika {valmistusaika} min")

    return palautus

def hae_raakaaine(tiedosto: str, aine: str):
    palautus = []
    with open(tiedosto) as tiedosto:
        reseptilista = tiedosto.read()

        reseptit = reseptilista.split("\n\n")
        for resepti in reseptit:
            rivit = resepti.split("\n")
            nimi = rivit[0]
            valmistusaika = int(rivit[1])
            raakaaineet = rivit[2:]

            if aine in raakaaineet:
                palautus.append(f"{nimi}, valmistusaika {valmistusaika} min")
    return palautus

if __name__ == "__main__":
    löydetyt = hae_nimi("reseptit2.txt", "ka")
    for löytö in löydetyt:
        print(löytö)

    löydetyt = hae_aika("reseptit1.txt", 20)

    for resepti in löydetyt:
        print(resepti)

    löydetyt = hae_raakaaine("reseptit1.txt", "maito")

    for resepti in löydetyt:
        print(resepti)