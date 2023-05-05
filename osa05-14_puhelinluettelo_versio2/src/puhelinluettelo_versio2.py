def hae(lista):
    haku = input("Nimi: ")
    if haku in lista:
        for sarake in lista[haku]:
            print(sarake)
    else:
        print("ei numeroa")


def lisaa(lista):
    nimi = input("nimi: ")
    if nimi not in lista:
        lista[nimi] = []
    lista[nimi].append(input("numero: "))
    print("ok!")


def main():
    luettelo = {}
    while True:
        komento = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))

        if komento == 1:
            hae(luettelo)
        elif komento == 2:
            lisaa(luettelo)
        elif komento == 3:
            print("lopetetaan...")
            break


main()
