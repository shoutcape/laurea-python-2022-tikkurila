# tee ratkaisu tänne
while True:
    with open("sanakirja.txt", "a") as tiedosto:
        print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
        valinta = input("Valinta: ")


        if valinta == "1":
            suomisana = input("Anna sana suomeksi: ")
            englantisana = input("Anna sana englanniksi: ")
            tiedosto.write(suomisana + " - " + englantisana + "\n")
            print("Sanapari lisätty")


        elif valinta == "2":
            hakusana = input("Anna sana: ")
            with open("sanakirja.txt", "r") as tiedosto:
                löydetyt = []
                sisalto = tiedosto.read()
                for rivi in sisalto.split("\n"):
                    if hakusana in rivi:
                        löydetyt.append(rivi)

                if hakusana not in sisalto:
                    print("Sanaa ei löydy!")
                    continue
                for löydetty in löydetyt:
                    print(löydetty)

        elif valinta == "3":
            print("Moi!")
            break