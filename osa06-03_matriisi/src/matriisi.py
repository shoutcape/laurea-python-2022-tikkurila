# tee ratkaisu tänne
def summa():
    with open("matriisi.txt", "r") as tiedosto:
        # Lue tiedoston rivit ja tallenna ne matriisi-listaan
        matriisi = []
        for rivi in tiedosto:
            # poista rivinvaihdot ja erota numerot pilkulla
            rivi_lista = [int(arvo.strip("\n")) for arvo in rivi.split(",")]
            for sarake in rivi_lista:
                matriisi.append(sarake)

        return sum(matriisi)

def maksimi():
    with open("matriisi.txt", "r") as tiedosto:
        # Lue tiedoston rivit ja tallenna ne matriisi-listaan
        matriisi = []
        for rivi in tiedosto:
            # poista rivinvaihdot ja erota numerot pilkulla
            rivi_lista = [int(arvo.strip("\n")) for arvo in rivi.split(",")]
            for sarake in rivi_lista:
                matriisi.append(sarake)

        return max(matriisi)

def rivisummat():
    with open("matriisi.txt", "r") as tiedosto:
        # Lue tiedoston rivit ja tallenna ne matriisi-listaan
        matriisi = []
        for rivi in tiedosto:
            # poista rivinvaihdot ja erota numerot pilkulla
            rivi_lista = [int(arvo.strip("\n")) for arvo in rivi.split(",")]
            matriisi.append(sum(rivi_lista))
        return matriisi


if __name__=="__main__":
    print(summa())
    print(maksimi())
    print(rivisummat())