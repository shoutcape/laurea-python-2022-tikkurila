from datetime import datetime

def onko_validi(hetu: str):
    if len(hetu) != 11:
        return False

    try:
        paiva = int(hetu[0:2])
        kuukausi = int(hetu[2:4])
        vuosi = int(hetu[4:6])
        vuosisadan_merkki = hetu[6]
        yksilonumero = int(hetu[7:10])
        tarkistusmerkki = hetu[10]
        numerot = hetu[0:6] + hetu[7:10]
        indeksi = int(numerot)%31
        tarkiste = '0123456789ABCDEFHJKLMNPRSTUVWXY'[indeksi]

        if paiva < 1 or paiva > 31 or kuukausi < 1 or kuukausi > 12 or vuosisadan_merkki not in ('-','+','A') or tarkistusmerkki != tarkiste:
            return False
        
        vuosisata = 0
        if vuosisadan_merkki == '-':
            vuosisata = 1800
        elif vuosisadan_merkki == '+':
            vuosisata = 1900
        elif vuosisadan_merkki == 'A':
            vuosisata = 2000
        
        syntymavuosi = vuosisata + vuosi

        datetime(syntymavuosi, kuukausi, paiva)

        return True
    except:
        return False
    
if __name__ == "__main__":
    print(onko_validi("230827-906F"))
