# tee ratkaisu tänne
omistettu = input("Kenelle teos omistetaan: ")
tiedosto = input("Mihin kirjoitetaan: ")
#tiedosto = "omistettu.txt"
with open(tiedosto, "w") as kirjoitus:
    kirjoitus.write("Hei " + omistettu + ", toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")
