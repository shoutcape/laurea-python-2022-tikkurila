# tee ratkaisu tänne
def uusi_henkilo(nimi: str, ika: int):

        if nimi == "" or len(nimi) > 40 or " " not in nimi[1:-1] or ika < 0 or ika > 150:
            raise ValueError("Nimen pituus ei ole sallittu")

        return (nimi, ika)


if __name__ == "__main__":
    print(uusi_henkilo("nik las", 14))