import datetime

def paivat_vuosituhan_vaihtumiseen(paiva: int, kuukausi: int, vuosi: int):
    syntymaaika = datetime.date(vuosi, kuukausi, paiva)
    vuosituhan_vaihtuminen = datetime.date(1999, 12, 31)
    if syntymaaika > vuosituhan_vaihtuminen:
        return "Et ollut syntynyt, kun vuosituhat vaihtui."
    else:
        paivien_maara = (vuosituhan_vaihtuminen - syntymaaika).days
        return f"Olit {paivien_maara} päivää vanha, kun vuosituhat vaihtui."

paiva = int(input("Päivä: "))
kuukausi = int(input("Kuukausi: "))
vuosi = int(input("Vuosi: "))
print(paivat_vuosituhan_vaihtumiseen(paiva, kuukausi, vuosi))