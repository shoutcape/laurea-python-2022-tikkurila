def lue_hedelmat():
    sanakirja = {}
    with open("hedelmat.csv") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.split(";")
            sanakirja[rivi[0]] = float(rivi[1])
    print(sanakirja)
    return sanakirja

if __name__ == "__main__":
    lue_hedelmat()