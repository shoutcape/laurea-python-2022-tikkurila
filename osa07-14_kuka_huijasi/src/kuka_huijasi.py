# tee ratkaisu tänne
import csv
from datetime import datetime, timedelta

def get_students_exam_data() -> dict:
    oppilaat = {}
    with open('tentin_aloitus.csv') as aloitus:
        for rivi in csv.reader(aloitus, delimiter=';'):
            oppilas = rivi[0]
            aloitusaika = datetime.strptime(rivi[1], '%H:%M')
            oppilaat[oppilas] = {
                'aloitusaika' : aloitusaika,
                #'aloitusaika' : rivi[1],
                'stats' : {
                    'tasks' : [],
                    'points' : [],
                    'submission_times' : []
                }
            }

    with open('palautus.csv') as palautus:
        for rivi in csv.reader(palautus, delimiter=";"):
            oppilas = rivi[0]
            task = int(rivi[1])
            point = int(rivi[2])
            sub_time = datetime.strptime(rivi[3], '%H:%M')
            oppilaat[oppilas]['stats']['tasks'].append(task)
            oppilaat[oppilas]['stats']['points'].append(point)
            oppilaat[oppilas]['stats']['submission_times'].append(sub_time)
            #oppilaat[student]['stats']['submission_times'].append(rivi[3])

    return oppilaat

def huijarit():
    data = get_students_exam_data()
    huijarit = []
    for student, info in data.items():
        aloitusaika = info['aloitusaika']
        submission_times = info['stats']['submission_times']
        for time in submission_times:
            if time > (aloitusaika + timedelta(hours=3)):
                huijarit.append(student)
                break
    return huijarit

if __name__ == "__main__":
    print(huijarit())