megfelelo = True
while True:
    nev = input("Név: ")
    for karakter in nev:
        if karakter  in [' ', 'a', 'A']:
            pass
        else:
            print("Na,ne szotakozzál...")
            megfelelo=False
    if megfelelo:
        break
    else:
        continue
