import string

def jaa_merkkeihin(merkkijono: str):
    osa1 = ""
    osa2 = ""
    osa3 = ""
    for x in merkkijono:
        if x in string.ascii_letters:
            osa1 += x
        elif x in string.punctuation:
            osa2 += x
        else:
            osa3 += x
            
    return (osa1, osa2, osa3)
    
if __name__ == "__main__":
    
    osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
    print(osat[0])
    print(osat[1])
    print(osat[2])