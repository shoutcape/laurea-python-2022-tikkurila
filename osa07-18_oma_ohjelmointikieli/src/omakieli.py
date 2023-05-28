# tee ratkaisu tänne
# Write your solution here
from string import ascii_uppercase

def aloitusmuuttujat(muuttujat: dict):
    for kirjain in ascii_uppercase:
        muuttujat[kirjain] = 0

def paata_arvo(syote: str, muuttujat: dict) -> int:
    if syote in ascii_uppercase:
        return muuttujat[syote]
    else:
        return int(syote)

def suorita(ohjelma: list):
    tulosta_lista = []
    muuttujat = {}
    aloitusmuuttujat(muuttujat)

    sijainnit = []
    for indeksi, komento in enumerate(ohjelma):
        if ':' in komento:
            location = komento[:-1]
            sijainnit.append((location, indeksi))

    i = 0
    while i < len(ohjelma):
        ins = ohjelma[i]
        osat = ins.split(' ')
        toiminto = osat[0]
        if toiminto == 'PRINT':
            tulostus = osat[1]
            tulostus = paata_arvo(tulostus, muuttujat)
            tulosta_lista.append(tulostus)
        elif toiminto == 'MOV':
            var = osat[1]
            liikuta = osat[2]
            liikuta = paata_arvo(liikuta, muuttujat)
            muuttujat[var] = liikuta
        elif toiminto == 'ADD':
            var = osat[1]
            lisaa = osat[2]
            lisaa = paata_arvo(lisaa, muuttujat)
            muuttujat[var] += lisaa
        elif toiminto == 'SUB':
            var = osat[1]
            vahenna = osat[2]
            vahenna = paata_arvo(vahenna, muuttujat)
            muuttujat[var] -= vahenna
        elif toiminto == 'MUL':
            var = osat[1]
            monista = osat[2]
            monista = paata_arvo(monista, muuttujat)
            muuttujat[var] *= monista
        elif toiminto == 'JUMP':
            hyppaa = osat[1]
            for loc in sijainnit:
                if loc[0] == hyppaa:
                    i = loc[1]
        elif toiminto == 'IF':
            ensimmainen = osat[1]
            ensimmainen = str(paata_arvo(ensimmainen, muuttujat))
            operaattori = osat[2]
            toinen = osat[3]
            toinen = str(paata_arvo(toinen, muuttujat))
            result = eval(ensimmainen + operaattori + toinen)
            if result:
                hyppaa = osat[5]
                for loc in sijainnit:
                    if loc[0] == hyppaa:
                        i = loc[1]
        elif toiminto == 'END':
            return tulosta_lista

        i += 1
    return tulosta_lista