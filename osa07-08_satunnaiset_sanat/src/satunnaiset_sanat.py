def sanat(n: int, alku: str):
    from random import sample
    with open("sanat.txt") as tiedosto:
        sanalista = [sana.strip() for sana in tiedosto.readlines() if sana.startswith(alku)]
        print(sanalista)
        return sample(sanalista, n)
      
if __name__ == "__main__":
    lista = sanat(2, "az")
    for sana in lista:
        print(sana)