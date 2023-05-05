def lukukirja():
    ykköset = ["yksi", "kaksi", "kolme", "neljä", "viisi", "kuusi", "seitsemän", "kahdeksan", "yhdeksän"]
    kirjasto = {}
    toista = "toista"
    kymmentä = "kymmentä"

    o = 1
    kirjasto[0] = "nolla"
    for i in range(1, 100):
        if i < 10:
            kirjasto[i] = ykköset[i-1]

        elif i < 20 and i > 10:
            kirjasto[i] = ykköset[o-1] + toista
            o += 1

        elif i == 10:
            kirjasto[i] = "kymmenen"

        elif i % 10 == 0:
            kirjasto[i] = ykköset[i//10-1] + kymmentä

        else:
            kirjasto[i] = ykköset[i//10-1] + kymmentä + ykköset[i%10-1]

        if o % 10 == 0:
            o = 1
    return kirjasto


if __name__ == "__main__":
    luvut = lukukirja()
    print(luvut[10])
    print(luvut[12])
    print(luvut[45])
    print(luvut[99])
    print(luvut[0])
