def lisaa_oikeaan(lisays: list):
    with open("oikeat.csv", "w") as tiedosto:
        lisataan = ""
        for kohta in lisays:
            lisataan += f"{kohta}\n"
        tiedosto.write(lisataan)

def lisaa_vaaraan(lisays: list):
    with open("vaarat.csv","w") as tiedosto:
        lisataan = ""
        for kohta in lisays:
            lisataan += f"{kohta}\n"
        tiedosto.write(lisataan)

def suodata_laskut():

    oikein = []
    vaarin = []
    with open("laskut.csv") as tiedosto:
        laskut = tiedosto.read()

    lista = laskut.split("\n")
    for osat in lista:
        if osat:
            lasku = osat.split(";")

        if "-" in lasku[1]:
            laskutoimitus = lasku[1].split("-")
            yhteensa = int(laskutoimitus[0]) - int(laskutoimitus[1])
            if str(yhteensa) == lasku[2]:
                oikein.append(osat)
            else:
                vaarin.append(osat)

        else:
            laskutoimitus = lasku[1].split("+")
            yhteensa = int(laskutoimitus[0]) + int(laskutoimitus[1])
            if str(yhteensa) == lasku[2]:
                oikein.append(osat)
            else:
                vaarin.append(osat)

    lisaa_oikeaan(oikein)
    lisaa_vaaraan(vaarin)

if __name__ == "__main__":
    suodata_laskut()