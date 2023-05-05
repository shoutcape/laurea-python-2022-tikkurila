
def suurin():
    with open("luvut.txt") as tiedosto:
        return int(max(tiedosto))

if __name__ == "__main__":
    print(suurin())