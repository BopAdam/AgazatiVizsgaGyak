osszesen = 0
db = 0
while db < 5:
    try:
        jegy = int(input(f"{db+1}, : "))
        if jegy>= 1 and jegy<=5:
            osszesen += jegy 
            db += 1
        else:
            print("Rossz erdemjegy!")
            continue
    except:
        continue

atlag = osszesen//db
print(f"MAtematika dolgozat atlaga:{atlag} ")