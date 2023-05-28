# tee ratkaisu tänne
import json

def tulosta_henkilot(tiedoston_nimi: str):
    with open(tiedoston_nimi) as tiedosto:
        data = tiedosto.read()
        henkilot = json.loads(data)
        for henkilo in henkilot:
            nimi = henkilo['nimi']
            ika = str(henkilo['ika']) + ' vuotta'
            harrastukset = '(' + ', '.join(henkilo['harrastukset']) + ')'
            print(f'{nimi} {ika} {harrastukset}')

if __name__ == '__main__':
    tulosta_henkilot('tiedosto1.json')