"""
Nev:Telepules:Fizetes:Jutalom:Születés:Belépés
filebol szarmazo adatok tarolasara szolgalo osztály
"""
import datetime
class Dolgozo:
    def __init__(self,adatok):
        reszek=adatok.split(":")
        self.nev = reszek[0]
        self.utca = reszek[2]
        self.telepules=reszek[1]
        self.fizetes=int(reszek[3])
        self.jutalom=int(reszek[4])
        #self.szuletes=reszek[4]
        #self.belepes=reszek[5]
        
        # Születési dátum feldolgozása
        reszek2 = reszek[5].split("-")
        self.szuletes = datetime.datetime(int(reszek2[0]), int(reszek2[1]), int(reszek2[2]))

        # Belépési dátum feldolgozása
        reszek3 = reszek[6].split("-")
        self.belepes = datetime.datetime(int(reszek3[0]), int(reszek3[1]), int(reszek3[2]))