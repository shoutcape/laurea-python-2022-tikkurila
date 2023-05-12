def tallenna_henkilo(henkilo: tuple):
    with open("henkilot.csv", "a") as tiedosto:
        tiedosto.write(";".join(str(x) for x in henkilo))
        tiedosto.write("\n")




if __name__ == "__main__":
    nimi = "Ville"
    ika = 45
    pituus = 160.0 
    henkilo = (nimi, ika, pituus)
    tallenna_henkilo(henkilo)