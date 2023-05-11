with open("paivakirja.txt", "a") as tiedosto:
    while True:
        print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
        komento = input("Valinta: ")

        if komento == "1":
            merkinta = input("Anna merkintä: ")
            tiedosto.write(f"{merkinta}\n")
            print("Päiväkirja tallennettu")
        elif komento == "2":
            with open("paivakirja.txt", "r") as tiedosto2:
                lista = tiedosto2.read()
                print("Merkinnät")
                print(lista)
        elif komento == "0":
            print("Heippa!")
            break
        else:
            print("väärä komento")
