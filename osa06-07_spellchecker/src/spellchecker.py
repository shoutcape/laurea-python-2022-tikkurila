sana = input("Write text: ")
#sana = "This is me"
uusisana = sana.split(" ")
tarkistussana = sana.lower().split(" ")

with open("wordlist.txt", "r") as tiedosto:
    sanakirja = [rivi.strip() for rivi in tiedosto]
    i = 0
    for kohta in uusisana:
        tarkistussana[i] = kohta
        if tarkistussana[i].lower() in sanakirja:
            print(kohta, end=" ")
        if tarkistussana[i].lower() not in sanakirja:
            print(f"*{kohta}*", end= " ")
        i += 1
