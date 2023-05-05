def histogrammi(merkkijono: str):
    lista = {}
    for merkki in merkkijono:
        if not merkki in lista:
            lista[merkki] = 0
        lista[merkki] += 1

    for kirjain in lista:
        print(kirjain, 1 * lista[kirjain])


if __name__ == "__main__":
    sana = input("Anna merkkijono: ")
    histogrammi(sana)
