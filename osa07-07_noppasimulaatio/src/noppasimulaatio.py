def heita(noppa: str):
    from random import choice

    NOPAT = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
            }

    return choice(NOPAT[noppa])
    
def pelaa(noppa1: str, noppa2: str, kertaa: int):
    pisteet1 = 0
    pisteet2 = 0
    tasapeli = 0
    
    for i in range(kertaa):
        noppa1_tulos = heita(noppa1)
        noppa2_tulos = heita(noppa2)
        
        if noppa1_tulos > noppa2_tulos:
            pisteet1 += 1
        elif noppa1_tulos < noppa2_tulos:
            pisteet2 += 1
        elif noppa1_tulos == noppa2_tulos:
            tasapeli += 1
    
    return pisteet1, pisteet2, tasapeli
    
    
    
    
if __name__ == "__main__":
    for i in range(20):
        print(heita("A"), " ", end="")
    print()
    for i in range(20):
        print(heita("B"), " ", end="")
    print()
    for i in range(20):
        print(heita("C"), " ", end="")
        
    tulos = pelaa("A", "C", 1000)
    print(tulos)
    tulos = pelaa("B", "B", 1000)
    print(tulos)