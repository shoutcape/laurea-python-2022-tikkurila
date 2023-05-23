from random import choice, shuffle
from string import ascii_lowercase, digits

def luo_hyva_salasana(pituus: int, numerot: bool, erikois: bool):
    erikoismerkit = "!?=+-()#"
    merkit = ascii_lowercase
    salasana = [choice(merkit)] 

    if numerot:
        merkit += digits
        salasana.append(choice(digits)) 
    if erikois:
        merkit += erikoismerkit
        salasana.append(choice(erikoismerkit)) 
    while len(salasana) < pituus: 
        salasana.append(choice(merkit))

    shuffle(salasana) 
    
    return ''.join(salasana)
    
if __name__ == "__main__":
    for i in range(10):
        print(luo_hyva_salasana(8, True, True))
