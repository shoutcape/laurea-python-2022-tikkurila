# tee ratkaisu tänne
def hae_sanat(hakusana: str):
    with open("sanat.txt", "r") as tiedosto:
        löytölista = []
        sanakirja = tiedosto.read()
        sanakirja = sanakirja.split("\n")
        for sana in sanakirja:
            if hakusana == sana:
                löytölista.append(sana)
            if hakusana[-1] == "*":
                if sana.startswith(hakusana[:-1]) and len(sana) >= (len(hakusana)):
                    löytölista.append(sana)
            if hakusana[0] == "*":
                if sana.endswith(hakusana[1:]) and len(sana) >= (len(hakusana)):
                    löytölista.append(sana)

            if "." in hakusana:
                indeksi = hakusana.index(".")
                if len(sana) == len(hakusana):
                    i = 0
                    for kirjain in sana:
                        if kirjain == hakusana[i] or hakusana[i] == ".":
                            i += 1
                            if i == len(hakusana):
                                löytölista.append(sana)

    return löytölista


if __name__ == "__main__":
    print(hae_sanat("pir*"))

###mikä on regex?


# startswith(*)
# endswith()
