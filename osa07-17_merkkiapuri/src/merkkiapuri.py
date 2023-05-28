# tee ratkaisu tänne

from string import ascii_lowercase, ascii_uppercase, digits


def vaihda_koko(alkup_merkkijono: str):
    uusi_merkkijono = ''
    pohjoismaiset_p = 'äöå'
    pohjoismaiset_i = 'ÄÖÅ'
    for kirjain in alkup_merkkijono:
        if kirjain in ascii_uppercase or kirjain in pohjoismaiset_i:
            uusi_merkkijono += kirjain.lower()
        elif kirjain in ascii_lowercase or kirjain in pohjoismaiset_p:
            uusi_merkkijono += kirjain.upper()
        else:
            uusi_merkkijono += kirjain
    return uusi_merkkijono
    
def puolita(alkup_merkkijono: str):
    length = len(alkup_merkkijono)
    keskikohta = length//2
    ensimmainen = alkup_merkkijono[:keskikohta]
    viimeinen = alkup_merkkijono[keskikohta:]
    return (ensimmainen, viimeinen)

def poista_erikoismerkit(alkup_merkkijono: str):
    uusi_merkkijono = ''
    pohjoismaiset_p = 'äöå'
    pohjoismaiset_i = 'ÄÖÅ'
    for merkki in alkup_merkkijono:
        if merkki == ' ' or merkki in ascii_lowercase or merkki in ascii_uppercase or merkki in digits or merkki in pohjoismaiset_p or merkki in pohjoismaiset_i:
            uusi_merkkijono += merkki
    return uusi_merkkijono