megfelelo = True
while True:
    nev = input("Név: ")
    for karakter in nev:
        if karakter  in [' ', 'a', 'A','á','Á']:
            pass
        else:
            print("Na,ne szotakozzál...")
            megfelelo=False
    if megfelelo:
        break
    else:
        megfelelo = True
        continue


#mehhhhhgoldás2

megfelelok="AaÁáBb..zZ"
listaM = []
for m in megfelelok:
    listaM.append(m)

szotarM={}
ekezetes="áÁéÉíÍóÓöÖőŐúÚúÚűŰ"
