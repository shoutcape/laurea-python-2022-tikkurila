# tee ratkaisu tänne
def suodata_virheelliset():
    with open("lottonumerot.csv") as tiedosto:
        virheelliset = []
        oikeat = []
        for rivi in tiedosto:
            osat = rivi.split(";")
            viikko = osat[0].split(" ")
            viikko = viikko[1]
            numerot = osat[1].strip().split(",")

            if len(numerot) == 7 and viikko.isdigit():
                for numero in numerot:
                    if not numero.isdigit() or int(numero) < 1 or int(numero) > 40:
                        virheelliset.append(rivi)
                if rivi not in virheelliset:
                    oikeat.append(rivi)

    with open("korjatut_numerot.csv", "w") as tiedosto:
        for rivi in oikeat:
            tiedosto.write(rivi)


if __name__ == "__main__":
    suodata_virheelliset()