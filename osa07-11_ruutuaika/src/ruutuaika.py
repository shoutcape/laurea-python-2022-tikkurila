# tee ratkaisu tänne,
from datetime import datetime, timedelta

if True:
    tiedoston_nimi = input('Tiedoston nimi: ')
    aloituspaiva = input('Aloituspäivä: ')
    paivien_lkm = int(input('Kuinka monta päivää: '))
    print('Kirjoita näytöllä vietetty aika minuutteina joka päivä (TV tietokone matkapuhelin): ')
    aloituspaiva = datetime.strptime(aloituspaiva, '%d.%m.%Y')
    viimeinen_paiva = aloituspaiva + timedelta(days=paivien_lkm)
    
    paivat = []
    ajat = []
    while aloituspaiva < viimeinen_paiva:
        paiva = aloituspaiva.strftime('%d.%m.%Y')
        paivat.append(paiva)
        nayton_aika = input(f'Näytönaika {paiva}: ')
        ajat.append(tuple(nayton_aika.split(' ')))
        aloituspaiva = aloituspaiva + timedelta(days=1)
else:
    # Käytetty kehitysvaiheessa nopeaan testaamiseen.
    tiedoston_nimi = 'late_june.txt'
    aloituspaiva = '24.6.2020'
    paivien_lkm = 5
    print('Kirjoita näytöllä vietetty aika minuutteina joka päivä (TV tietokone matkapuhelin): ')
    aloituspaiva = datetime.strptime(aloituspaiva, '%d.%m.%Y')
    viimeinen_paiva = aloituspaiva + timedelta(days=paivien_lkm)

    ajat = [('60','120','0'), ('0','0','0'), ('180','0','0'), ('25','240','15'), ('45','90','5')]
    paivat = ['24.06.2020', '25.06.2020', '26.06.2020', '27.06.2020', '28.06.2020']

print(f'Tiedot tallennettu tiedostoon {tiedoston_nimi}')
with open(tiedoston_nimi, 'w') as tiedosto:
    tiedosto.write(f'Ajanjakso: {paivat[0]}-{paivat[paivien_lkm-1]}\n')
    kokonaisaika = 0
    for aika in ajat:
        kokonaisaika += int(aika[0]) + int(aika[1]) + int(aika[2])
    tiedosto.write(f'Yht. minuutteja: {kokonaisaika}\n')
    tiedosto.write(f'Keskim. minuutteja: {kokonaisaika/len(ajat)}\n')
    for indeksi, paiva in enumerate(paivat):
        tiedosto.write(f'{paiva}: {ajat[indeksi][0]}/{ajat[indeksi][1]}/{ajat[indeksi][2]}\n')
