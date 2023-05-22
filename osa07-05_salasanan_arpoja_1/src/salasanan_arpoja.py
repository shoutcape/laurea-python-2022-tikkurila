from random import choice
from string import ascii_lowercase

def luo_salasana(pituus: int):
    salasana = ""
    for i in range(pituus):
        salasana += choice(ascii_lowercase)
    
    return salasana
    
        
if __name__ == "__main__":
  
    for i in range (3):
        print(luo_salasana(3))