import math

"""
Documentacios komment: 
Mehes Adam, 2025.11.08.
Hengeres Hasáb terfogatának akiszamítását elvégző függvény típúsú alprogram keszitesenek emutatása és annak felhasznalasa.
"""
print(__doc__)


while True:
    try:
        r=int(input("Az alaplap sugara: "))
        break
    except:
        pass
while True:
    try:
        h=int(input("A hasab magassága: "))
        break
    except:
        pass

def terfogat(r, h):
    return r**2*3.14*h
eredmeny = terfogat(r,h)

print(f"a hengeres hasáb térfogata: {terfogat(r,h): 8.2f}")
