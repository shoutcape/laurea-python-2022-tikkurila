# tee ratkaisu tänne

import csv
import json
from datetime import datetime, timedelta

def hanki_opiskelijoiden_koetiedot() -> dict:
    opiskelijat = {}
    with open('tentin_aloitus.csv') as aloitustiedosto:
        for rivi in csv.reader(aloitustiedosto, delimiter=';'):
            opiskelija = rivi[0]
            aloitus_aika = datetime.strptime(rivi[1], '%H:%M')
            opiskelijat[opiskelija] = {
                'aloitus_aika' : aloitus_aika,
                #'aloitus_aika' : rivi[1],
                'stats' : {
                    'tasks' : [],
                    'points' : [],
                    'submission_times' : []
                }
            }

    with open('palautus.csv') as palautustiedosto:
        for rivi in csv.reader(palautustiedosto, delimiter=";"):
            opiskelija = rivi[0]
            task = int(rivi[1])
            piste = int(rivi[2])
            pal_aika = datetime.strptime(rivi[3], '%H:%M')
            opiskelijat[opiskelija]['stats']['tasks'].append(task)
            opiskelijat[opiskelija]['stats']['points'].append(piste)
            opiskelijat[opiskelija]['stats']['submission_times'].append(pal_aika)
            #opiskelijat[opiskelija]['stats']['submission_times'].append(rivi[3])

    return opiskelijat

def viralliset_pisteet():
    viralliset_pisteet = {}
    data = hanki_opiskelijoiden_koetiedot()
    for opiskelija, info in data.items():
        yht_pisteet = 0
        aloitus_aika = info['aloitus_aika']
        tasks = info['stats']['tasks']
        for task in range(1, 9):
            indices = [i for i, v in enumerate(tasks) if v == task]
            max_pisteet = 0
            for index in indices:
                piste = info['stats']['points'][index]
                pal_aika = info['stats']['submission_times'][index]
                if pal_aika <= (aloitus_aika + timedelta(hours=3)):
                    if piste > max_pisteet:
                        max_pisteet = piste
            yht_pisteet += max_pisteet
        viralliset_pisteet[opiskelija] = yht_pisteet
    return viralliset_pisteet