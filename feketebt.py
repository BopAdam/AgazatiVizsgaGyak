#M.Adam - 2025.11.08
import dolgozo
from dolgozo import Dolgozo
file = open("feketeBt.txt", mode="r", encoding="utf8")
for sor in file:
    #print(sor.strip())
    dolgozo= Dolgozo(sor.strip())
    Dolgozo.append(dolgozo)

file.close()
print(Dolgozo)