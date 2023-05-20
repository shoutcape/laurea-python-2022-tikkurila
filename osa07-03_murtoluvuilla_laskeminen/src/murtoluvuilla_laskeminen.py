from fractions import Fraction

def jaa_palasiksi(maara: int):
    testi = [(Fraction(1, maara)) for x in range(maara)]
    return testi

if __name__ == "__main__":
    
    for p in jaa_palasiksi(3):
        print(p)
        
    print()
    
    print(jaa_palasiksi(5))
    