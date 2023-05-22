from random import shuffle

def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    numerot = list(range(alaraja,ylaraja+1))
    shuffle(numerot)
    lottonumerorivi = sorted(numerot[0:maara])
    return  lottonumerorivi

if __name__ == "__main__":
    for numero in lottonumerot(7, 1, 40):
        print(numero)