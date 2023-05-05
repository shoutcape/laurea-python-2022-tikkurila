luettelo = {}

while True:
    komento = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))

    if komento == 1:
        haku = input("nimi: ")
        if haku in luettelo:
            print(luettelo[haku])
        else:
            print("ei numeroa")


    elif komento == 2:
        lisays = input("Nimi: ")
        luettelo[lisays] = (input("Numero: "))
        print("ok!")

    elif komento == 3:
        print("lopetetaan...")
        break
